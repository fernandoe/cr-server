import yfinance as yf
from django.http import HttpResponse
from django.shortcuts import render

from fe_cr.models import Ticker, TickerData


def search(request):
    query = request.GET.get("q")
    if query:
        tickers = Ticker.objects.filter(name__icontains=query)
    else:
        tickers = Ticker.objects.all()

    context = {"tickers": tickers}
    return render(request, "htmx/tickers/list.html", context)


def get_data(request):
    tickers = Ticker.objects.filter(is_enabled=True, name="TRAD3")

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

    return HttpResponse("OK")
