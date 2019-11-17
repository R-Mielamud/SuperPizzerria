from django.forms import *
from Orders.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "dishes"]

    def save_order(self):
        dishes_price = sum([dish.price for dish in self.cleaned_data["dishes"].all()])

        order = Order(
            client = self.cleaned_data["client"],
            price = dishes_price
        )

        order.dishes.set(self.cleaned_data["dishes"])
        order.save()

