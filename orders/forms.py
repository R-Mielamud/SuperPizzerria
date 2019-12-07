from django.forms import *
from orders.models import Order

class ModOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "pizzas", "address", "telephone"]