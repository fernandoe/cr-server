import decimal
import os

from django.contrib import admin

from .models import Strategy, Ticker, TickerData


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


@admin.register(Strategy)
class StrategyMA(admin.ModelAdmin):
    search_fields = ("name", "is_enabled")
    list_display = ("get_uuid", "created_at", "updated_at", "name", "is_enabled")
