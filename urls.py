from api.views import AllPizzasViewSet, FilteredByNamePizzasViewSet, CartPizzasViewSet, AddPizzaToOrderViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r"get_all_pizzas", AllPizzasViewSet, basename="Pizza")
router.register(r"get_filtered_by_name_pizzas", FilteredByNamePizzasViewSet, basename="Pizza")
router.register(r"get_cart", CartPizzasViewSet, basename="Order")
router.register(r"add_pizza", AddPizzaToOrderViewSet, basename="Pizza")

urlpatterns = [
    path("", include(router.urls)),
]
