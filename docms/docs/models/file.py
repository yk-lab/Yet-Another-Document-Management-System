from django.conf import settings
from django.db import models
from model_utils.fields import MonitorField
from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel
from django.utils.translation import ugettext_lazy as _


class File(UUIDModel, TimeStampedModel, SoftDeletableModel):
    removed = MonitorField(monitor='is_removed')
    fileset = models.ForeignKey(
        'docs.Fileset',
        models.CASCADE,
        related_name='files',
        verbose_name=_('file'))
    file = models.FileField(
        verbose_name=_('file'),
        editable=False)
    filename = models.CharField(
        verbose_name=_('filename'),
        max_length=256)
    memo = models.TextField(
        verbose_name=_('memo'), blank=True)
    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
        related_name='files',
        verbose_name=_('registered by'))
