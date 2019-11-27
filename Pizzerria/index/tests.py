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