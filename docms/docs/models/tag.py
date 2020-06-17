from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel
from django.utils.translation import ugettext_lazy as _


class Tag(UUIDModel, TimeStampedModel):
    code = models.CharField(
        verbose_name=_("code"),
        max_length=256)
