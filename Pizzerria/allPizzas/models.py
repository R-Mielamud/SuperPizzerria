from django.db.models import *

class Ingredient(Model):
    name = CharField(max_length=30, default="")
    price = DecimalField(max_digits=4, decimal_places=2, default=0)
    description = TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Pizza(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=30, default="")
    ingredients = ManyToManyField("Ingredient", related_name="orders")
    price = DecimalField(max_digits=6, decimal_places=2, default=0)
    description = TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.price = sum([ingredient.price for ingredient in self.ingredients.all()])
        return super().save(*args, **kwargs)