from django.views.generic import FormView, UpdateView, base
from orders.forms import AddOrderForm, ModifyOrderForm
from orders.models import Order, InstancePizza, Pizza


class AddOrderView(FormView):
    form_class = AddOrderForm
    template_name = "modify_order.html"
    success_url = "/orders/cart/"

    def form_valid(self, form):
        form.create_order()
        return super().form_valid(form)


class ModifyOrderView(UpdateView):
    form_class = ModifyOrderForm
    model = Order
    template_name = "modify_order.html"
    success_url = "/orders/cart/"

    def get(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.modified_object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.modify_order(self.modified_object)
        return super().form_valid(form)


class CartView(base.TemplateView):
    template_name = "cart.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["orders"] = Order.objects.filter(client__username=self.request.user.username)
        return context
