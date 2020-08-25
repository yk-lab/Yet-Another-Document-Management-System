from rest_framework import serializers

from ..models.file import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        queryset = File.objects.filter(is_removed=False).order_by('created')
        model = File
        fields = [
            'id',
            'file',
            'filename',
            'fileset',
            'memo',
            'is_removed',
            'created',
            'modified']
        read_only_fields = [
            'id',
            'file',
            'filename',
            'fileset',
            'registered_by']
