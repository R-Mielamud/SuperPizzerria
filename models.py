from django.db.models import *

class Client(Model):
    login = CharField(max_length = 20, default = "")
    password = CharField(max_length = 20, default = "")
    email = EmailField(max_length = 40, default = "")
    first_name = CharField(max_length = 20, default = "")
    last_name = CharField(max_length = 20, default = "")
    about = TextField(max_length = 1000, blank = True, null = True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class NamedItem(Model):
    name = CharField(max_length = 50, default = "")

    def __str__(self):
        return str(self.name)

class Ingredient(NamedItem):
    price = DecimalField(max_digits = 4, decimal_places = 2, default = 0)

class InstanceDish(NamedItem):
    ingredients = ManyToManyField("Ingredient", related_name = "dishes")
    price = DecimalField(max_digits = 5, decimal_places = 2, default = 0)

Почему появляется
IntegrityError at /addorder/
FOREIGN KEY constraint failed ?

Мой Order:

class Order(Model):
    id = IntegerField(primary_key = True, default = 1)
    client = ForeignKey(Client, on_delete = CASCADE)
    dishes = ManyToManyField("InstanceDish", related_name = "orders")
    price = DecimalField(max_digits = 20, decimal_places = 2, default = 0)
