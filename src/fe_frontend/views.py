import base64
from io import BytesIO

import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from fe_cr.models import StrategyExecution, Ticker, TickerData
from fe_cr.tables import StrategyExecutionTable
from fe_frontend.filters import StrategyExecutionFilter

plt.switch_backend("AGG")


def index(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "tickers": tickers,
    }
    return render(request, "index.html", data)


def tickers(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "active_tickers": "active",
        "tickers": tickers,
    }
    return render(request, "main/tickers.html", data)


def strategies(request):
    data = {
        "active_strategies": "active",
        "tickers": tickers,
    }
    return render(request, "main/strategies.html", data)


def results(request):
    data = {
        "active_results": "active",
    }
    return render(request, "main/results.html", data)


def graphics(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "active_graphics": "active",
        "tickers": tickers,
    }
    return render(request, "main/graphics.html", data)


def graphics_tickers_search(request):
    query = request.GET.get("q")
    if query:
        tickers = Ticker.objects.filter(name__icontains=query)
    else:
        tickers = Ticker.objects.all()
    context = {"tickers": tickers}
    return render(request, "htmx/graphics/tickers.html", context)


def graphics_image(request, ticker_name):
    ticker = Ticker.objects.get(name=ticker_name)
    data = TickerData.objects.filter(ticker=ticker, date__gte="2023-07-01").order_by("date")
    df = pd.DataFrame(list(data.values("date", "open", "high", "low", "close", "volume")))
    df.set_index("date", inplace=True)
    df.index = pd.to_datetime(df.index, format="%Y-%m-%d", utc=True)

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(int)

    img = BytesIO()
    mpf.plot(df, type="candle", volume=True, savefig=img)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode("utf8")
    mpf_data = plot_url
    return render(request, "htmx/graphics/img.html", {"mpf_data": mpf_data})


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class StrategyExecutionTableView(SingleTableMixin, FilterView):
    table_class = StrategyExecutionTable
    queryset = StrategyExecution.objects.all()
    filterset_class = StrategyExecutionFilter
    paginate_by = 10
    paginator_class = CustomPaginator

    def get_template_names(self):
        if self.request.htmx:
            template_name = "main/results_partial.html"
        else:
            template_name = "main/results.html"
        return template_name
