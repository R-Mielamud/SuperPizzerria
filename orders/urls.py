from django.conf.urls import url
from django.urls import path
from orders.views import AddOrderView, EditOrderView, CartView
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r"^cart/addorder/$", cache_page(60 * 60 * 24)(AddOrderView.as_view())),
    path("cart/order/<int:pk>/edit/", cache_page(5)(EditOrderView.as_view())),
    url(r"^cart/$", cache_page(5)(CartView.as_view())),
]