from django.conf.urls import url
from api.views import AllPizzas, OrderedPizzas, AddPizza, Cart


urlpatterns = [
    url(r"^get_all_pizzas/$", AllPizzas.as_view()),
    url(r"^get_ordered_pizzas/$", OrderedPizzas.as_view()),
    url(r"^get_cart/$", Cart.as_view()),
    url(r"^add_pizza/$", AddPizza.as_view()),
]
