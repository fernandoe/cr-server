from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from commons.base_models import UUIDModel

User = get_user_model()


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

    def update_if_changed(self, ticker_open, high, low, close, volume):
        # print(f"Comparing {self.ticker.name} - {self.date}")
        # print(f"Comparing {self.open} - {ticker_open}")
        # print(f"Comparing {self.high} - {high}")
        # print(f"Comparing {self.low} - {low}")
        # print(f"Comparing {self.close} - {close}")
        # print(f"Comparing {self.volume} - {volume}")
        if (
            float(self.open) != float(ticker_open)
            or float(self.high) != float(high)
            or float(self.low) != float(low)
            or float(self.close) != float(close)
            or int(self.volume) != int(volume)
        ):
            print(f"Updating {self.ticker.name} - {self.date}")
            self.open = ticker_open
            self.high = high
            self.low = low
            self.close = close
            self.volume = volume
            self.save()

    class Meta:
        unique_together = ("ticker", "date")


class Strategy(UUIDModel):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StrategyExecution(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    initial_cash = models.DecimalField(max_digits=10, decimal_places=2)
    final_cash = models.DecimalField(max_digits=10, decimal_places=2)
    total_return = models.DecimalField(max_digits=10, decimal_places=2)
    num_trades = models.IntegerField()
    num_win = models.IntegerField()
    chart_data = models.BinaryField(blank=True, null=True)
    # win_pnl = models.DecimalField(max_digits=10, decimal_places=2)
    # sqn_score = models.DecimalField(max_digits=10, decimal_places=2)
    # mdd = models.DecimalField(max_digits=10, decimal_places=2)
    # mdd_period = models.IntegerField()
    # total_compound_return = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)

    def scheme_image_tag(self):
        from base64 import b64encode

        from django.utils.safestring import mark_safe

        return mark_safe(
            '<img src="data: image/png; base64, {}" width="200" height="100">'.format(
                # self.chart_data.tobytes().decode("utf8")
                self.chart_data.decode("utf8")
            )
        )

    scheme_image_tag.short_description = "Image"
    scheme_image_tag.allow_tags = True
