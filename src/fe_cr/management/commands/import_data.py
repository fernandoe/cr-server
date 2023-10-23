import os

import yfinance as yf
from django.core.management.base import BaseCommand

from fe_cr.models import Ticker, TickerData


class Command(BaseCommand):
    def handle(self, *args, **options):
        tickers = Ticker.objects.filter(is_enabled=True)
        for ticker in tickers:
            print(f"Ticker: {ticker}")
            data = yf.download(f"{ticker.name}.SA", progress=False, rounding=True)
            for i, row in data.iterrows():
                ticker_data = TickerData.objects.create(
                    ticker=ticker,
                    date=i.date(),
                    open=row["Open"],
                    high=row["High"],
                    low=row["Low"],
                    close=row["Close"],
                    volume=row["Volume"],
                )
