from django.conf import settings
from django.db import models
from model_utils.fields import MonitorField
from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel
from django.utils.translation import ugettext_lazy as _


class Fileset(UUIDModel, TimeStampedModel, SoftDeletableModel):
    removed = MonitorField(monitor='is_removed')
    document = models.ForeignKey(
        'docs.Document',
        models.CASCADE,
        related_name='filesets',
        verbose_name=_('document'))
    name = models.CharField(
        verbose_name=_('name'),
        db_index=True,
        max_length=256)
    summary = models.TextField(
        verbose_name=_('summary'), blank=True)
    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
        related_name='filesets',
        verbose_name=_('registered by'))
