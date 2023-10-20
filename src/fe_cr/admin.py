import decimal
import os

from django.contrib import admin

from .models import Strategy, StrategyExecution, Ticker, TickerData


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


@admin.register(StrategyExecution)
class StrategyExecutionMA(admin.ModelAdmin):
    list_display = (
        "get_uuid",
        "created_at",
        "updated_at",
        "user",
        "strategy",
        "ticker",
        "start_date",
        "end_date",
        "initial_cash",
        "final_cash",
        "total_return",
        "num_trades",
        "num_win",
        "scheme_image_tag",
    )
    readonly_fields = ("scheme_image_tag",)
