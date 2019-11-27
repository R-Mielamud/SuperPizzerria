from django.test import TestCase

class MainTestCase(TestCase):
    def setUp(self):
        pass
    
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData()

    def test_index_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_page_output(self):
        response = self.client.get("/")
        self.assertContains(response, 'Maybe, you searching <a href="./all_pizzas/">all our pizzas</a>')