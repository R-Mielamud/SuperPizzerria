from django.shortcuts import render
from Orders.forms import OrderForm
from django.views.generic import FormView

class OrderView(FormView):
    form_class = OrderForm
    success_url = "/"
    template_name = "addorder.html"

    def form_valid(self, form):
        form.save_order()
        return super().form_valid(form)