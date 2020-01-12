from django.db.models import *
from django.contrib.auth.models import User


class Ingredient(Model):
    name = CharField(default="", max_length=50)
    price = DecimalField(default=0, decimal_places=2, max_digits=4)

    def __str__(self):
        return "Ingredient {}".format(self.name)

class Pizza(Model):
    ingredients = ManyToManyField("Ingredient", related_name="pizzas")
    price = DecimalField(default=0, max_digits=10, decimal_places=2)
    name = CharField(default="", max_length=50)
    description = TextField(blank=True, null=True)

    def __str__(self):
        return "Pizza {}".format(self.name)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save()

        price = sum([ingredient.price for ingredient in self.ingredients.all()])
        print("Price of pizza {} is {}".format(self.name, price))
        self.price = price
        return super().save(*args, **kwargs)

class InstancePizza(Model):
    related_order_id = IntegerField()
    pizza = ForeignKey(Pizza, related_name="instances", on_delete=CASCADE)
    count = IntegerField(default=0)

    def __str__(self):
        return "Instance of pizza {}".format(self.pizza.name)

class Order(Model):
    client = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    pizzas = ManyToManyField("InstancePizza", related_name="orders")
    price = DecimalField(default=0, max_digits=10, decimal_places=2)
    address = CharField(default="", max_length=200)
    telephone = CharField(default="", max_length=30)
    time_deliver = TimeField()

    def __str__(self):
        return "Order from user {}".format(self.client.username)

    def calculate_price(self, pizzas=[]):
        price = sum([pizza_data.pizza.price * pizza_data.count for pizza_data in self.pizzas.all()])
        self.save(price=price)

    def save(self, price=0, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)

        self.price = price
        return super().save(*args, **kwargs)
