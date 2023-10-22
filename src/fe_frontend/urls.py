"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import index, results, strategies, tickers
from .views_x import x_results_list

urlpatterns = [
    path("", index, name="index"),
    path("strategies/", strategies, name="strategies"),
    path("tickers/", tickers, name="tickers"),
    path("results/", results, name="results"),
    path("x/results/list/", x_results_list, name="x_results_list"),
]
