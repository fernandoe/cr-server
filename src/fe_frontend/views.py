from django.shortcuts import render

from fe_cr.models import StrategyExecution, Ticker


def index(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "tickers": tickers,
    }
    return render(request, "index.html", data)


def strategies(request):
    return render(request, "main/strategies.html")


def results(request):
    results = StrategyExecution.objects.all()
    data = {
        "results": results,
    }
    return render(request, "main/results.html", data)
