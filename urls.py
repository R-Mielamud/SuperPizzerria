from django.conf.urls import url
from django.urls import path
from AllOurPizzas.views import PizzaPriceUpdateView, PizzasListView

urlpatterns = [
    url(r'^all_pizzas/$', PizzasListView.as_view()),
    path("pizza/<int:pk>/edit/", PizzaPriceUpdateView.as_view())
]