from django.conf.urls import url
from Orders.views import OrderView

urlpatterns = [
    url(r'^addorder/$', OrderView.as_view())
]