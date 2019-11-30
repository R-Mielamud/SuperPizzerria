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
    description = TextField(max_length=1000, default="")

    def __str__(self):
        return self.name

class Order(Model):
    client = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    pizzas = ManyToManyField("Pizza", related_name="orders")
    price = DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return "Order from {}".format(self.client.username)

    def calculate_price(self):
        self.price = sum([p.price for p in self.pizzas.all()])

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)

        self.calculate_price()
        return super().save(*args, **kwargs)