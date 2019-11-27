from django.conf.urls import url
from allPizzas.views import AllPizzasView

urlpatterns = [
    url(r"^all_pizzas/$", AllPizzasView.as_view()),
]