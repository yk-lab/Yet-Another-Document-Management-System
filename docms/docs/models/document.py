from django.conf import settings
from django.db import models
from model_utils.fields import MonitorField
from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel
from django.utils.translation import ugettext_lazy as _


class Document(UUIDModel, TimeStampedModel, SoftDeletableModel):
    removed = MonitorField(monitor='is_removed')
    title = models.CharField(
        verbose_name=_('title'),
        db_index=True,
        max_length=512)
    summary = models.TextField(
        verbose_name=_('summary'), blank=True)
    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
        related_name='documents',
        verbose_name=_('registered by'))
    tags = models.ManyToManyField(
        'docs.Tag',
        related_name='documents',
        verbose_name=_('tags'))
