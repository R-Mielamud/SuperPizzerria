from django.db.models import *

class Pizza(Model):
    id = IntegerField(default = 1, primary_key = True)
    name = CharField(max_length = 30, default = "pizza")
    price = DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    description = TextField(max_length = 1000, blank = True, null = True)

    def __str__(self):
        return "{}. {}".format(self.id, self.name)