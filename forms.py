from django.forms import *
from AllOurPizzas.models import Pizza

class PizzaPriceUpdateForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ["price"]