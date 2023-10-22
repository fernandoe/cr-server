from django.shortcuts import render

from fe_cr.models import StrategyExecution, Ticker


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
