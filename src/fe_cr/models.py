from django.db import models

from commons.base_models import UUIDModel


class Ticker(UUIDModel):
    name = models.CharField(max_length=10)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TickerData(UUIDModel):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ("ticker", "date")


class Strategy(UUIDModel):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
