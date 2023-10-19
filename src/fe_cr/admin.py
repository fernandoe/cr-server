import decimal
import os

from django.contrib import admin

from .models import Ticker, TickerData

# Register your models here.


@admin.register(Ticker)
class TickerMA(admin.ModelAdmin):
    search_fields = ("name", "is_enabled")
    list_display = ("get_uuid", "created_at", "updated_at", "name", "is_enabled")


@admin.register(TickerData)
class TickerDataMA(admin.ModelAdmin):
    search_fields = ("ticker__name", "date", "open", "high", "low", "close", "volume")
    list_display = (
        "get_uuid",
        "created_at",
        "updated_at",
        "ticker",
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume",
    )
