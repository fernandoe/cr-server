import backtrader as bt


class BaseSignalStrategy(bt.SignalStrategy):
    params = {"print_log": True}

    def log(self, txt, dt=None, do_print=False):
        if self.params.print_log or do_print:
            dt = dt or self.datas[0].datetime.date(0)
            print(f"{dt.isoformat()} - {txt}")

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"Buy Executed - Price: {order.executed.price:.2f} - Cost: {order.executed.value:.2f}")
            else:  # Sell
                self.log(f"Sell Executed - Price: {order.executed.price:.2f} - Cost: {order.executed.value:.2f}")

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("Order Canceled/Margin/Rejected")

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f"Operation Profit, Gross {trade.pnl:.2f} - NET {trade.pnlcomm:.2f}")
