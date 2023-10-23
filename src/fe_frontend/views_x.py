from django.shortcuts import render

from fe_cr.models import StrategyExecution, Ticker


def x_results_list(request):
    results = StrategyExecution.objects.all()
    data = {
        "results": results,
    }
    return render(request, "htmx/results/list.html", data)


def x_results_graphic(request, uuid):
    item = StrategyExecution.objects.get(uuid=uuid)
    data = {"image": item.chart_data.decode("utf-8")}
    return render(request, "htmx/results/graphic.html", data)
