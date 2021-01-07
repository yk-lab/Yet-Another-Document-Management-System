from rest_framework import serializers

from ..models.fileset import Fileset
from .file import FileSerializer


class FilesetSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    # latest_file = FileSerializer(
    #     queryset=File.objects.filter(is_removed=False).latest('created'))

    class Meta:
        model = Fileset
        fields = ['id', 'name', 'files']
        read_only_fields = ['id']
