from rest_framework import viewsets

from ..models.tag import Tag
from ..serializers.tag import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing Tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
