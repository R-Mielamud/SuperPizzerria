from django.forms import *
from Orders.models import Order

class AddOrderForm(ModelForm):
    def save_order(self):
        data = self.cleaned_data

        order = Order(
            id = (Order.objects.last().id if Order.objects.last() else 0) + 1,
            client = data["client"]
        )

        order.save()
        order.dishes.set(data["dishes"])
        order.save()

    class Meta:
        fields = ["client", "dishes"]
        model = Order