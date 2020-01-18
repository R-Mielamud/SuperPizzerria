from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.task import periodic_task
from celery.decorators import task
from celery.task.schedules import crontab
from pizzerria.parsing import parse_and_log_pizzas


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzerria.settings")
app = Celery("pizzerria")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

@task(name="add_pizza_to_order")
def add_pizza_to_order(username, order_time_deliver, pizza_name):
    order = Order.objects.get(time_deliver=order_time_deliver, client__username=username)
    inst_pizza = InstancePizza.objects.get(pizza__name=pizza_name, related_order_id=order.pk)
    inst_pizza.count += 1
    inst_pizza.save()

@periodic_task(
    run_every=(crontab(hour="*/1")),
    name="parse_pizzas",
    ignore_result=True
)
def parse_pizzas():
    parse_and_log_pizzas()
