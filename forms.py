from django.forms import ModelForm, IntegerField, CharField
from orders.models import Order, InstancePizza, Pizza


class ModifyOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["telephone", "address", "client"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for pizza in InstancePizza.objects.all():
            self.fields[pizza.pizza.name] = IntegerField()

    @property
    def get_pizzas(self):
        data = self.cleaned_data
        pizzas = []

        for pizza in Pizza.objects.all():
            new_pizza_inst = InstancePizza(
                pizza=pizza,
                count=data[pizza.name],
                price=0
            )

            new_pizza_inst.save()
            pizzas.append(new_pizza_inst)

        return pizzas

    def save_order(self):
        pizzas = self.get_pizzas
        client = self.cleaned_data["client"]
        address = self.cleaned_data["address"]
        telephone = self.cleaned_data["telephone"]

        new_order = Order(
            client=client,
            address=address,
            telephone=telephone
        )

        new_order.save(set_price=False)
        new_order.pizzas.set(pizzas)
        new_order.calculate_price(pizzas=pizzas, save=True)

# Здравствуйте. Сейчас работаю над сайтом пиццерии. Есть несколько пицц и model-форма для заказа (Order). Подскажите, пожалуйста, как добавить к форме заказа поля, названные как пиццы, если неизвестно, сколько есть пицц.
# Как добавить в ModelForm несколько полей, если их имена хранятся в виде строк, а количество - неизвестно?