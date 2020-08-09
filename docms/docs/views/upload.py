import json
import uuid
from logging import getLogger
from pathlib import Path

import boto3
from boto3.session import Session
from botocore.config import Config
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from docs.models import File, Fileset

logger = getLogger(__name__)


class UploadView(APIView):
    renderer_classes = [JSONRenderer]

    bucket_name = settings.DOCUMENT_FILE_BUCKET_NAME
    endpoint_url = settings.AWS_ENDPOINT_URL

    def post(self, request, format=None):
        file_name = Path(request.data['file_name'])\
            if request.data.get('file_name') else ''
        ext = file_name and file_name.suffix or ''
        if len(file_name.name) > 256:
            file_name.name = file_name.name[:256]

        file_rename, presigned_info = self.get_presigned_url(ext=ext)

        fileset = request.data.get('fileset_id')\
            and get_object_or_404(Fileset, pk=request.data.get('fileset_id'))\
            or Fileset.objects.create(
                name=file_name, registered_by=request.user)
        File.objects.create(
            fileset=fileset,
            file=file_rename,
            filename=file_name,
            registered_by=request.user,
        )

        return Response({
            'action': presigned_info['url'],
            'fields': presigned_info['fields'],
            # TODO 将来的には URL にする (ex. serializers.HyperlinkedModelSerializer
            'url': fileset.id,
        })

    def get_presigned_url(self, ext=''):
        session = Session(**self.get_sts())
        s3 = session.client(
            's3',
            config=Config(signature_version='s3v4'),
            endpoint_url=self.endpoint_url)
        file_name = f'{uuid.uuid4().hex}{ext}'
        return file_name, s3.generate_presigned_post(
            self.bucket_name,
            file_name,
            ExpiresIn=60,
        )

    def get_sts(self):
        sts_kwargs = {
            'endpoint_url': self.endpoint_url,
            'config': Config(
                signature_version='v4',
            ),
        }
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": [
                        "s3:GetObject",
                        "s3:PutObject"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        f"arn:aws:s3:::{self.bucket_name}/*"
                    ],
                    "Sid": "Stmt1"
                }
            ]
        }

        client = boto3.client('sts', **sts_kwargs)
        resp = client.assume_role(
            RoleArn='arn:xxx:xxx:xxx:xxxx',
            RoleSessionName='anything',
            Policy=json.dumps(policy, separators=(',', ':')),
            DurationSeconds=900,
        )
        # TODO エラーハンドリング
        return {
            'aws_access_key_id': resp['Credentials']['AccessKeyId'],
            'aws_secret_access_key': resp['Credentials']['SecretAccessKey'],
            'aws_session_token': resp['Credentials']['SessionToken']}
