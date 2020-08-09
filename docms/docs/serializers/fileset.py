from rest_framework import serializers

from ..models.fileset import Fileset


class FilesetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fileset
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']
