from django.conf.urls import url
from django.urls import path
from Orders.views import AddOrderView, CartView, EditOrderView

urlpatterns = [
    url(r"^addorder/$", AddOrderView.as_view()),
    url(r"^$", CartView.as_view()),
    path("order/<int:pk>/edit/", EditOrderView.as_view())
]