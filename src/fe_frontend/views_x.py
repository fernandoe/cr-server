from django.shortcuts import render

from fe_cr.models import StrategyExecution, Ticker


def x_results_list(request):
    results = StrategyExecution.objects.all()
    data = {
        "results": results,
    }
    return render(request, "htmx/results/list.html", data)
