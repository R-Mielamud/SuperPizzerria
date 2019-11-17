from django.contrib import admin
from Orders.models import NamedItem, Client, Order, Ingredient, InstanceDish

class DishAdmin(admin.ModelAdmin):
    filter_horizontal = ["ingredients"]

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ["dishes"]

admin.site.register(NamedItem)
admin.site.register(Client)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient)
admin.site.register(InstanceDish, DishAdmin)