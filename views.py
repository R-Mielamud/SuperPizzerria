from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from AllOurPizzas.forms import PizzaPriceUpdateForm
from AllOurPizzas.models import Pizza

class PizzaPriceUpdateView(UpdateView):
    model = Pizza
    form_class = PizzaPriceUpdateForm
    success_url = "/all_pizzas/"
    template_name = "update_pizza.html"

    def get_queryset(self):
        return super().get_queryset()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PizzasListView(ListView):
    model = Pizza
    template_name = "view_pizzas.html"
    context_object_name = "pizzas"

    def get_queryset(self):
        select_field_name = "ordering"

        if self.request.GET.get(select_field_name):
            order = self.request.GET.get(select_field_name)
            context = Pizza.objects.all().order_by(order)
            return context

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        select_field_name = "ordering"

        if self.request.GET.get(select_field_name):
            ordering = self.request.GET.get(select_field_name)
            context["pizzas"] = Pizza.objects.all().order_by(ordering)
            context["ordering"] = ordering
            
        context["pizzas_count"] = self.model.objects.all().count()
        return context