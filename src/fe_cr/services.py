import yfinance as yf

from .models import TickerData


def update_tickers(tickers):
    for ticker in tickers:
        print(f"Ticker: {ticker}")
        data = yf.download(f"{ticker.name}.SA", progress=False, rounding=True)
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
