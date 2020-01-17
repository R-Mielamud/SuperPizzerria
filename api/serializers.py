def convert_pizza_to_dict(pizza):
    return {
        "name": pizza.name,
        "price": pizza.price
    }

def convert_order_to_dict(order):
    return {
        "client": {
            "username": order.client.username
        },

        "pizzas": [
            {"name": pizza_data.pizza.name} for pizza_data in order.pizzas.all()
        ],

        "address": order.address,
        "telephone": order.telephone,
        "time_deliver": order.time_deliver,
        "price": order.price
    }