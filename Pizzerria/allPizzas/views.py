from django.shortcuts import render
from django.views.generic import ListView
from allPizzas.models import Pizza

class AllPizzasView(ListView):
    model = Pizza
    context_object_name = "all_pizzas"
    template_name = "all_pizzas_list.html"