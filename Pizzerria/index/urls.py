from django.shortcuts import render
from django.conf.urls import url
from index.views import IndexView

urlpatterns = [
    url(r"^$", IndexView.as_view()),
]