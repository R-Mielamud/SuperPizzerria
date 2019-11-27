from django.test import TestCase
from allPizzas.models import Pizza

class MainTestsCase(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        Pizza.objects.create(
            id = 1,
            name = "First Test Pizza",
            price = 100
        )

        Pizza.objects.create(
            id = 2,
            name = "Second Test Pizza",
            price = 200
        )

        return super().setUpTestData()

    def test_all_pizzas_url(self):
        response = self.client.get("/all_pizzas/")
        self.assertEqual(response.status_code, 200)

    def test_pizzas_output(self):
        response = self.client.get("/all_pizzas/")
        self.assertContains(response, "Our available pizzas:")