import datetime
import os

import yfinance as yf
from django.core.management.base import BaseCommand

from fe_cr.models import Ticker, TickerData


class Command(BaseCommand):
    def handle(self, *args, **options):
        tickers = Ticker.objects.filter(is_enabled=True).order_by("name")  # [0:3]
        for ticker in tickers:
            print(f"Ticker: {ticker}")
            ticker_data = TickerData.objects.filter(ticker=ticker).order_by("-date").first()
            start_date = ticker_data.date - datetime.timedelta(days=5)
            data = yf.download(f"{ticker.name}.SA", start=start_date, progress=False, rounding=True)

            for i, row in data.iterrows():
                date = i.date()
                ticker_open = row["Open"]
                high = row["High"]
                low = row["Low"]
                close = row["Close"]
                volume = row["Volume"]
                try:
                    ticker_data = TickerData.objects.get(ticker=ticker, date=date)
                    ticker_data.update_if_changed(ticker_open, high, low, close, volume)
                except TickerData.DoesNotExist:
                    print(f"Creating {ticker.name} - {date}")
                    TickerData.objects.create(
                        ticker=ticker,
                        date=i.date(),
                        open=row["Open"],
                        high=row["High"],
                        low=row["Low"],
                        close=row["Close"],
                        volume=row["Volume"],
                    )
