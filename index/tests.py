from django.test import TestCase

class IndexPageTest(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData()

    def test_browser_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "<h1>Hello!</h1>")
        self.assertContains(response, '<h3><a href="./cart/">See cart</a></h3>')
        self.assertContains(response, '<h3><a href="./cart/addorder/">Place order</a></h3>')