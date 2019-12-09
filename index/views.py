from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.cache import cache

class IndexView(TemplateView):
    template_name = "index_page.html"

    def get_context_data(self, **kwargs):
        if not cache.get("ipaddr"):
            cache.set("ipaddr", self.request.META["REMOTE_ADDR"])
        else:
            if not (cache.get("ipaddr") == self.request.META["REMOTE_ADDR"]):
                print("Another IP address!")

        return super().get_context_data(**kwargs)