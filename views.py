from django.shortcuts import render
from orders.forms import ModOrderForm
from django.views.generic import FormView, UpdateView, base
from orders.models import Order

class AddOrderView(FormView):
    form_class = ModOrderForm
    template_name = "add_order.html"
    success_url = "/cart/"

    def get(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.modified_object.calculate_price(form.get_pizzas)
        return super().form_valid(form)

class EditOrderView(UpdateView):
    form_class = ModOrderForm
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
        self.modified_object.calculate_price(form.get_pizzas)
        return super().form_valid(form)

class CartView(base.TemplateView):
    template_name = "cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(client__username=self.request.user.username)
        return context