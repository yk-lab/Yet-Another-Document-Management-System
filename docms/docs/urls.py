from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UploadView
from .viewsets import DocumentViewSet, TagViewSet

router = SimpleRouter()
router.register('documents', DocumentViewSet)
router.register('tags', TagViewSet)

urlpatterns = format_suffix_patterns([
    path('upload/', UploadView.as_view()),
]) + router.urls
