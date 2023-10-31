import django_tables2 as tables

from .models import StrategyExecution


class StrategyExecutionTable(tables.Table):
    class Meta:
        model = StrategyExecution
        fields = (
            "ticker",
            "start_date",
            "end_date",
            "initial_cash",
            "final_cash",
            "total_return",
            "num_trades",
            "num_win",
        )
        show_header = True
        template_name = "tables/strategy-execution.html"
