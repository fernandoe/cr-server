import backtrader as bt

from .base import BaseSignalStrategy


class SMA3(BaseSignalStrategy):
    params = dict(sma=3, print_log=True, use_filter=False, filter=21)

    def __init__(self):
        self.sma3_up = bt.ind.SMA(self.data.high, period=self.params.sma)
        self.sma3_down = bt.ind.SMA(self.data.low, period=self.params.sma)
        self.sma_filter = bt.ind.SMA(period=self.params.filter)

        self.cheating = self.cerebro.p.cheat_on_open

    # def next(self):
    def operate(self, fromopen):
        price_open = self.data.open[0]
        price_high = self.data.high[0]
        price_low = self.data.low[0]
        price_close = self.data.close[0]
        sma3_up = self.sma3_up[0]
        sma3_down = self.sma3_down[0]
        position = self.position
        operation_filter = self.sma_filter[0]

        self.log(
            f"O: {price_open:.2f} - H: {price_high:.2f} - L: {price_low:.2f} - C: {price_close:.2f} - "
            f"sma3_up: {sma3_up:.2f} - sma3_down: {sma3_down:.2f} - position.size: {position.size} - "
            f"operation: {operation_filter:.2f}"
        )

        if not position:
            use_filter = self.params.use_filter
            if (use_filter is False or (price_open > operation_filter)) and price_low <= sma3_down:
                self.log(f"Buy created: {sma3_down:.2f}")
                self.buy(price=sma3_down, exectype=bt.Order.StopLimit)
        else:
            if price_high >= sma3_up:
                self.log(f"Sell Created: {sma3_up:.2f}")
                self.sell(price=sma3_up, exectype=bt.Order.Limit)

    def next(self):
        self.log("{} next, open {} close {}".format(self.data.datetime.date(), self.data.open[0], self.data.close[0]))
        if self.cheating:
            return
        self.operate(fromopen=False)

    def next_open(self):
        if not self.cheating:
            return
        self.operate(fromopen=True)
