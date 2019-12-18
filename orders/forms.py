from django.forms import *
from orders.models import Order


class ModifyOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "pizzas", "address", "telephone"]

    @property
    def get_pizzas(self):
        return self.cleaned_data["pizzas"]

    def create_order(self):
        new_order = Order(
            client=self.cleaned_data["client"],
            address=self.cleaned_data["address"],
            telephone=self.cleaned_data["telephone"]
        )

        new_order.save()
        new_order.pizzas.set(self.cleaned_data["pizzas"])
        new_order.calculate_price(self.cleaned_data["pizzas"])
        new_order.save()
