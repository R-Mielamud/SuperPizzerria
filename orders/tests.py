from django.test import TestCase
from orders.models import Ingredient, Pizza, Order
from django.contrib.auth.models import User

class OrdersPagesTest(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        order1 = Order(
            price=0.00,
            address="abc",
            telephone="012 345 67 89"
        )

        user = User()
        user.save()
        order1.client = user
        order1.save()
        return super().setUpTestData()

    def test_cart_browser_code(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)

    def test_cart_page_content(self):
        response = self.client.get("/cart/")
        self.assertContains(response, '<h3><a href="./addorder/">Let\'s place order!</a></h3>')

    def test_addorder_browser_code(self):
        response = self.client.get("/cart/addorder/")
        self.assertEqual(response.status_code, 200)

    def test_addorder_page_content(self):
        response = self.client.get("/cart/addorder/")
        self.assertContains(response, "Address")
        self.assertContains(response, "Telephone")
        self.assertContains(response, "Client")
        self.assertContains(response, "Pizzas")

    def test_editorder_browser_code(self):
        response = self.client.get("/cart/order/1/edit/")
        self.assertEqual(response.status_code, 200)

    def test_editorder_page_content(self):
        response = self.client.get("/cart/order/1/edit/")
        self.assertContains(response, "Address")
        self.assertContains(response, "Telephone")
        self.assertContains(response, "Client")
        self.assertContains(response, "Pizzas")