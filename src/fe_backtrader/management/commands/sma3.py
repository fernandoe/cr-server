import math
import os
from datetime import datetime

import backtrader as bt
import pandas as pd
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from fe_backtrader.engine.strategies.sma3 import SMA3
from fe_cr.models import Strategy, StrategyExecution, Ticker, TickerData


class Command(BaseCommand):
    def handle(self, *args, **options):
        cerebro = bt.Cerebro()
        cerebro.broker.setcash(100.0)
        # Add a strategy
        cerebro.addstrategy(SMA3)

        data = (
            TickerData.objects.filter(
                ticker__name="PETR4",
                date__gte="2023-01-01",
            )
            .order_by("date")
            .values("date", "open", "high", "low", "close", "volume")
        )

        df = pd.DataFrame(list(data), columns=["date", "open", "high", "low", "close", "volume"])
        df.set_index("date", inplace=True)
        df.index = pd.to_datetime(df.index, format="%Y-%m-%d", utc=True)
        feed = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(feed)

        cerebro.addanalyzer(bt.analyzers.TimeDrawDown, _name="drawdown")
        cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name="annualreturn")
        cerebro.addanalyzer(bt.analyzers.Returns, _name="returns")
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
        cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
        cerebro.addanalyzer(bt.analyzers.PyFolio, _name="pyfolio")
        cerebro.addobserver(bt.observers.DrawDown)

        print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")
        results = cerebro.run()
        final_cash = cerebro.broker.getvalue()
        print(f"Final Portfolio Value: {final_cash}")

        sqn = results[0].analyzers.sqn.get_analysis()
        ta = results[0].analyzers.ta.get_analysis()
        drawdown = results[0].analyzers.drawdown.get_analysis()
        annualreturn = results[0].analyzers.annualreturn.get_analysis()
        returns = results[0].analyzers.returns.get_analysis()
        pyfoliozer = results[0].analyzers.pyfolio.get_analysis()

        sqn_score = sqn.get("sqn", 0)
        mdd = drawdown.get("maxdrawdown", 0)
        mdd_period = drawdown.get("maxdrawdownperiod", 0)
        total_compound_return = returns.get("rtot", 0)
        num_trades = ta.get("total", {}).get("total", 0)
        num_win = ta.get("won", {}).get("total", 0)
        win_pnl = ta.get("won", {}).get("pnl", {}).get("average", 0)
        lose_pnl = ta.get("lost", {}).get("pnl", {}).get("average", 0)
        net_pnl = ta.get("pnl", {}).get("net", {}).get("average", 0)

        win_rate = num_win / num_trades if num_trades > 0 else 0

        data = [
            [
                f"{math.floor(cerebro.broker.get_value()):,} ({total_compound_return:.2%})",
                f"{sqn_score:.2f}",
                f"{mdd:.2f}%",
                mdd_period,
            ],
        ]

        print(f"data: {data}")
        print(f"win_rate: {win_rate}")
        print(f"num_trades: {num_trades}")
        print(f"num_win: {num_win}")

        user = User.objects.get(username="fernandoe")
        strategy = Strategy.objects.get(pk="bce729cf-a2b0-422e-a023-32ea87781c82")
        ticker = Ticker.objects.get(name="PETR4")
        StrategyExecution.objects.create(
            user=user,
            strategy=strategy,
            ticker=ticker,
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 1, 1),
            initial_cash=100.0,
            final_cash=final_cash,
            total_return=0,
            num_trades=num_trades,
            num_win=num_win,
        )

        cerebro.plot(style="candlestick")
