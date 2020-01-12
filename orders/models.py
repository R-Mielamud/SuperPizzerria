from django.db.models import *
from django.contrib.auth.models import User


class Ingredient(Model):
    name = CharField(max_length=30, default="")
    price = DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(Model):
    name = CharField(max_length=30, default="")
    price = DecimalField(max_digits=10, decimal_places=2)
    ingredients = ManyToManyField("Ingredient", related_name="pizzas")
    description = TextField(max_length=1000, default="")

    def __str__(self):
        return self.name

    def calculate_price(self):
        self.price = sum([i.price for i in self.ingredients.all()])
        self.save(calculate=False)

    def save(self, calculate=True):
        if self.pk is None:
            super().save()

        if calculate:
            self.calculate_price()
        else:
            return super().save()


class Order(Model):
    client = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    pizzas = ManyToManyField("Pizza", related_name="orders")
    price = DecimalField(max_digits=100, decimal_places=2, default=0)
    address = CharField(max_length=300, default="")
    telephone = CharField(max_length=20, default="")

    def __str__(self):
        return "Order from {}".format(self.client.username)

    def calculate_price(self, pizzas=None, save=True):
        if self.pk is None:
            super().save()

        if pizzas is not None:
            self.price = price = sum([pizza.price for pizza in pizzas.all()])

        if save:
            self.save(set_price=False, price=price)
        else:
            return self.price

    def save(self, set_price=True, price=0.00):
        if set_price:
            self.price = self.calculate_price(save=False)
        else:
            self.price = price
            return super().save()
