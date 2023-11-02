import django_filters

from fe_cr.models import StrategyExecution


class StrategyExecutionFilter(django_filters.FilterSet):
    # id = django_filters.NumberFilter(label="")
    # name = django_filters.CharFilter(label="", lookup_expr="istartswith")
    # category = django_filters.CharFilter(label="", lookup_expr="istartswith")
    # price = django_filters.NumberFilter(label="", method="filter_decimal")
    # cost = django_filters.NumberFilter(label="", method="filter_decimal")
    # status = django_filters.ChoiceFilter(label="", choices=Product.Status.choices)
    ticker = django_filters.CharFilter(field_name="ticker__name")

    class Meta:
        model = StrategyExecution
        # fields = ["final_cash", "num_trades"]
        fields = []

    # def filter_decimal(self, queryset, name, value):
    #     # For price and cost, filter based on
    #     # the following property:
    #     # value <= result < floor(value) + 1
    #
    #     lower_bound = "__".join([name, "gte"])
    #     upper_bound = "__".join([name, "lt"])
    #
    #     upper_value = math.floor(value) + Decimal(1)
    #
    #     return queryset.filter(**{lower_bound: value,gg
    #                               upper_bound: upper_value})
