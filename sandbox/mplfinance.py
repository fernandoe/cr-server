import mplfinance as mpf
import pandas as pd

from fe_cr.models import Ticker, TickerData

ticker = Ticker.objects.get(name="PETR4")

data = (
    TickerData.objects.filter(
        ticker=ticker,
        date__gte="2023-03-01",
    )
    .order_by("date")
    .values("date", "open", "high", "low", "close", "volume")
)

df = pd.DataFrame(list(data), columns=["date", "open", "high", "low", "close", "volume"])
df.set_index("date", inplace=True)
df.index = pd.to_datetime(df.index, format="%Y-%m-%d", utc=True)
df["open"] = df["open"].astype(float)
df["high"] = df["high"].astype(float)
df["low"] = df["low"].astype(float)
df["close"] = df["close"].astype(float)
df["volume"] = df["volume"].astype(int)
mpf.plot(df)
