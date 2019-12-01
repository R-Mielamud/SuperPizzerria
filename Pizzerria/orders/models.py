from django.db.models import *
from django.contrib.auth.models import User

class Client(User):
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)

class Ingredient(Model):
    name = CharField(max_length=50, default="")
    price = DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)

class Dish(Model):
    id = IntegerField(primary_key=True)
    ingredients = ManyToManyField("Ingredient", related_name="dishes")
    name = CharField(max_length=50, default="")
    price = DecimalField(max_digits=10, decimal_places=2, default=0)
    description = TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return "{} ( {} )".format(self.name, self.id)

    def save(self, *args, **kwargs):
        price = sum([ingredient.price for ingredient in self.ingredients.all()])
        self.price = price
        return super().save(*args, **kwargs)

class Order(Model):
    id = IntegerField(primary_key = True)
    client = ForeignKey(Client, on_delete=CASCADE, related_name="orders")
    dishes = ManyToManyField("Dish", related_name="orders")
    price = DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return "Order"

    def save(self, *args, **kwargs):
        price = sum([dish.price for dish in self.dishes.all()])
        self.price = price
        return super().save(*args, **kwargs)