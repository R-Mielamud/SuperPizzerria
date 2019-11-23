from django.contrib import admin
from orders.models import Client, Dish, Ingredient, Order

class DishAdmin(admin.ModelAdmin):
    readonly_fields = ["price"]

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ["dishes"]

admin.site.register(Client)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Order, OrderAdmin)