from django.shortcuts import render

from fe_cr.models import Ticker


def index(request):
    tickers = Ticker.objects.all()
    data = {
        "tickers": tickers,
    }
    return render(request, "index.html", data)
