from django.conf.urls import url
from index.views import IndexView
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r"^$", cache_page(60 * 60 * 24 * 2)(IndexView.as_view())),
]
