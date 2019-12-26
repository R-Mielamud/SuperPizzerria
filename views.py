from django.shortcuts import render
from orders.forms import ModifyOrderForm
from django.views.generic import FormView, UpdateView, base
from orders.models import Order
from django.core.cache import cache


class AddOrderView(FormView):
    form_class = ModifyOrderForm
    template_name = "add_order.html"
    success_url = "/cart/"    

    def form_valid(self, form):
        if not cache.get("ipaddr"):
            cache.set("ipaddr", self.request.META["REMOTE_ADDR"], 120)
        else:
            if not (cache.get("ipaddr") == self.request.META["REMOTE_ADDR"]):
                print("Another IP address!")

        form.save_order()
        return super().form_valid(form)


class EditOrderView(UpdateView):
    form_class = ModifyOrderForm
    model = Order
    template_name = "edit_order.html"
    success_url = "/cart/"
    modified_object = None

    def get(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if not cache.get("ipaddr"):
            cache.set("ipaddr", self.request.META["REMOTE_ADDR"], 120)
        else:
            if not (cache.get("ipaddr") == self.request.META["REMOTE_ADDR"]):
                print("Another IP address!")

        self.modified_object.calculate_price(form.get_pizzas)
        return super().form_valid(form)


class CartView(base.TemplateView):
    template_name = "cart.html"
    
    def get_context_data(self, **kwargs):
        if not cache.get("ipaddr"):
            cache.set("ipaddr", self.request.META["REMOTE_ADDR"], 120)
        else:
            if not (cache.get("ipaddr") == self.request.META["REMOTE_ADDR"]):
                print("Another IP address!")

        context = super().get_context_data(**kwargs)

        context["orders"] = Order.objects.filter(
            client__username=self.request.user.username
        )

        return context
