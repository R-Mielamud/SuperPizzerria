from django.http import JsonResponse
from django.views.generic import View
from orders.models import Pizza, Order, InstancePizza
from api.serializers import convert_pizza_to_dict, convert_order_to_dict


class AllPizzas(View):
    def get(self, request):
        try:
            all_pizzas = Pizza.objects.all()
            all_pizzas_dict = []

            for i in range(len(all_pizzas)):
                all_pizzas_dict.append(convert_pizza_to_dict(all_pizzas[i]))

            return JsonResponse({
                "success": True,
                "pizzas": all_pizzas_dict
            })
        except:
            return JsonResponse({
                "success": False,
                "pizzas": []
            })


class OrderedPizzas(View):
    def get(self, request):
        try:
            order_by = request.GET.get("order_by")
            reverse = bool(request.GET.get("reverse"))
            all_pizzas = Pizza.objects.order_by(order_by)
            all_pizzas_dict = []

            for i in range(len(all_pizzas)):
                all_pizzas_dict.append(convert_pizza_to_dict(all_pizzas[i]))

            if reverse:
                all_pizzas_dict.reverse()

            return JsonResponse({
                "success": True,
                "pizzas": all_pizzas_dict
            })
        except:
            return JsonResponse({
                "success": False,
                "pizzas": []
            })


class Cart(View):
    def get(self, request):
        try:
            username = request.GET.get("username")
            all_orders = Order.objects.filter(client__username=username)
            all_orders_dict = []

            for i in range(len(all_orders)):
                all_orders_dict.append(convert_order_to_dict(all_orders[i]))

            return JsonResponse({
                "success": True,

                "cart": {
                    "orders": all_orders_dict
                }
            })
        except:
            return JsonResponse({
                "success": False,

                "cart": {
                    "orders": []
                }
            })


class AddPizza(View):
    def get(self, request):
        try:
            order_time_deliver = request.GET.get("order_time_deliver")
            pizza_name = request.GET.get("pizza_name")
            username = request.GET.get("username")
            order = Order.objects.get(time_deliver=order_time_deliver, client__username=username)
            inst_pizza = InstancePizza.objects.get(pizza__name=pizza_name, related_order_id=order.pk)
            inst_pizza.count += 1
            inst_pizza.save()
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"success": False})
