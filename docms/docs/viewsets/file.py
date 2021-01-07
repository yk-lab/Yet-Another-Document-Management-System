from rest_framework import viewsets

from ..models.fileset import Fileset
from ..serializers.fileset import FilesetSerializer


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    """A simple ViewSet for viewing Files."""

    queryset = Fileset.objects.all()
    serializer_class = FilesetSerializer
