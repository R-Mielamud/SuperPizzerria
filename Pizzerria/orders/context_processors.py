from orders.models import Order

def get_context(response):
    return {
        "separator": "---------------------------------------------------",
        "title_part_1": "Pizzerria|",
        "page_header": "Pizzerria",
    }