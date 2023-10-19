from django.shortcuts import render

from fe_cr.models import Ticker


def index(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "tickers": tickers,
    }
    return render(request, "index.html", data)
