from rest_framework import viewsets

from ..models.document import Document
from ..serializers.document import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing Documents."""

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(registered_by=self.request.user)
