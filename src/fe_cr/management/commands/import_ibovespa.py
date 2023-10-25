import csv
import os

import yfinance as yf
from django.core.management.base import BaseCommand

from fe_cr.models import Ticker, TickerData


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ibovespa.csv")
        with open(csv_file_path, "r", encoding="ISO-8859-1") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if (
                    row[0].startswith("IBOV")
                    or row[0].startswith("Código")
                    or row[0].startswith("Quantidade")
                    or row[0].startswith("Redutor")
                ):
                    continue
                ticker_name = row[0].split(";")[0]
                print(f"Importing {ticker_name}")
                Ticker.objects.get_or_create(name=ticker_name)
