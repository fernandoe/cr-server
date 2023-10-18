from django.db import models

from commons.base_models import UUIDModel


class Ticker(UUIDModel):
    name = models.CharField(max_length=10)
    is_enabled = models.BooleanField(default=True)
