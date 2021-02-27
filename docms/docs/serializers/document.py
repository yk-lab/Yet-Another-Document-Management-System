from logging import getLogger
from typing import Dict, List

from rest_framework import serializers

from .fileset import FilesetSerializer
from ..models import Document, Fileset, Tag
from .tag import TagSerializer

logger = getLogger(__name__)


class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    filesets = FilesetSerializer(many=True)

    class Meta:
        model = Document
        fields = [
            'id',
            'title',
            'summary',
            'tags',
            'filesets',
            'created',
            'modified',
            'registered_by']
        read_only_fields = ['id', 'created', 'modified', 'registered_by',
                            'is_removed', 'removed']

    def validate_tags(self, values):
        return [self.__get_tag(value) for value in self.initial_data['tags']]

    def validate_filesets(self, values):
        return [Fileset.objects.get(pk=value['id']) for value in self.initial_data['filesets']]

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        filesets: List[Fileset] = validated_data.pop('filesets')
        document = Document.objects.create(**validated_data)
        for tag in tags:
            document.tags.add(tag)
        for fileset in filesets:
            fileset.document = document
            # TODO クエリ最適化
            fileset.save(update_fields=['document_id'])
        return document

    def __get_tag(self, value) -> Tag:
        tag, _ = Tag.objects.get_or_create(code=value['code'])
        return tag
