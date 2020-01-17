from rest_framework.serializers import ModelSerializer
from orders.models import Order, Pizza, Ingredient, InstancePizza, User


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name", "price"]


class PizzaSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ["name", "price", "ingredients"]


class InstancePizzaSerializer(ModelSerializer):
    pizza = PizzaSerializer()

    class Meta:
        model = InstancePizza
        fields = ["pizza", "count"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class OrderSerializer(ModelSerializer):
    pizzas = InstancePizzaSerializer(many=True)
    client = UserSerializer()

    class Meta:
        model = Order
        fields = ["client", "pizzas", "address", "telephone", "time_deliver"]
