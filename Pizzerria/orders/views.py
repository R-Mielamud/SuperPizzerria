from django.shortcuts import render
from django.views.generic import FormView, ListView, UpdateView
from Orders.forms import AddOrderForm
from Orders.models import Order

class AddOrderView(FormView):
    form_class = AddOrderForm
    success_url = "/"
    template_name = "modorder.html"

    def form_valid(self, form):
        form.save_order()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Add"
        return context

class CartView(ListView):
    model = Order
    context_object_name = "orders"
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["full_price"] = sum([order.price for order in Order.objects.all()])
        return context 

class EditOrderView(UpdateView):
    model = Order
    form_class = AddOrderForm
    success_url = "/"
    template_name = "modorder.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Edit"
        return context