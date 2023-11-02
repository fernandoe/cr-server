from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from fe_cr.models import StrategyExecution, Ticker
from fe_cr.tables import StrategyExecutionTable
from fe_frontend.filters import StrategyExecutionFilter


def index(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "tickers": tickers,
    }
    return render(request, "index.html", data)


def tickers(request):
    tickers = Ticker.objects.all().order_by("name")
    data = {
        "active_tickers": "active",
        "tickers": tickers,
    }
    return render(request, "main/tickers.html", data)


def strategies(request):
    data = {
        "active_strategies": "active",
        "tickers": tickers,
    }
    return render(request, "main/strategies.html", data)


def results(request):
    data = {
        "active_results": "active",
    }
    return render(request, "main/results.html", data)


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class StrategyExecutionTableView(SingleTableMixin, FilterView):
    table_class = StrategyExecutionTable
    queryset = StrategyExecution.objects.all()
    filterset_class = StrategyExecutionFilter
    paginate_by = 10
    paginator_class = CustomPaginator

    def get_template_names(self):
        if self.request.htmx:
            template_name = "main/results_partial.html"
        else:
            template_name = "main/results.html"
        return template_name
