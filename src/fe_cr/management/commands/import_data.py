import os

from django.core.management.base import BaseCommand

from fe_cr.models import Ticker


class Command(BaseCommand):
    def handle(self, *args, **options):
        tickers = Ticker.objects.filter(is_enabled=True)
        for ticker in tickers:
            print(f"- {ticker.name} is enabled")
