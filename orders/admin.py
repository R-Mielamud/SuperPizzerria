from django.contrib import admin
from orders.models import Order, Pizza, Ingredient


def reg(*models):
    for model in models:
        admin.site.register(model)


reg(Order, Ingredient, Pizza)
