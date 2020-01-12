from orders.models import Pizza, Order, InstancePizza
from api.serializers import PizzaSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet


class AllPizzasViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class FilteredByNamePizzasViewSet(ModelViewSet):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name")
        queryset = Pizza.objects.filter(name=name)
        return queryset


class CartPizzasViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username")
        queryset = Order.objects.filter(client__username=username)
        return queryset


class AddPizzaToOrderViewSet(ModelViewSet):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username")
        order_time_deliver = self.request.query_params.get("time_deliver")
        pizza_name = self.request.query_params.get("pizza_name")

        order = Order.objects.get(time_deliver=order_time_deliver, client__username=username)
        inst_pizza = InstancePizza.objects.get(pizza__name=pizza_name, related_order_id=order.pk)
        inst_pizza.count += 1
        inst_pizza.save()

        queryset = Pizza.objects.get(name=pizza_name)
        return [queryset]
