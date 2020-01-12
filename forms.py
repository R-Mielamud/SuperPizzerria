from django.forms import *
from orders.models import Order, InstancePizza, Pizza


class OrderFormMixin(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "address", "telephone", "time_deliver"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for pizza in Pizza.objects.all():
            self.fields[pizza.name] = IntegerField()


class AddOrderForm(OrderFormMixin):
   def create_order(self):
        new_instances = []

        new_order = Order(
            client=self.cleaned_data["client"],
            address=self.cleaned_data["address"],
            telephone=self.cleaned_data["telephone"],
            time_deliver=self.cleaned_data["time_deliver"]
        )

        new_order.save()

        for pizza in Pizza.objects.all():
            new_instance = InstancePizza(
                related_order_id=new_order.pk,
                pizza=pizza,
                count=self.cleaned_data[pizza.name]
            )

            new_instance.save()
            new_instances.append(new_instance)

        new_order.pizzas.add(*new_instances)
        new_order.calculate_price(pizzas=new_instances)


class ModifyOrderForm(OrderFormMixin):
    def modify_order(self, modified_order):
        searching_pk = modified_order.pk
        instances_for_modified_order_dict = {}
        instances_for_modified_order_list = []

        for inst_pizza in InstancePizza.objects.all():
            if inst_pizza.related_order_id == searching_pk:
                instances_for_modified_order_dict[inst_pizza.pizza.name] = inst_pizza

        for pizza in Pizza.objects.all():
            instance = instances_for_modified_order_dict[pizza.name]
            instance.count = self.cleaned_data[pizza.name]
            instance.save()
            instances_for_modified_order_list.append(instance)

        modified_order.calculate_price(pizzas=instances_for_modified_order_list)
