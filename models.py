from django.db.models import *
from django.contrib.auth.models import User
from dishes import models

class Pizza(models.Pizza):
    pass

class Order(Model):
    client = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    pizzas = ManyToManyField("Pizza", related_name="orders")
    price = DecimalField(max_digits=100, decimal_places=2, default=0)
    address = CharField(max_length=300, default="")
    telephone = CharField(max_length=20, default="")

    def __str__(self):
        return "Order from {}".format(self.client.username)

    def calculate_price(self):
        # self.save(calculate=False)
        self.price = sum([p.price for p in self.pizzas.all()])
        self.save(calculate=False)

    def save(self, calculate=True):
        if self.pk is None:
            super().save()

        if calculate:
            self.calculate_price()
        else:
            return super().save()