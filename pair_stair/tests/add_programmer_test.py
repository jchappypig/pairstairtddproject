from django import test
from django.test.client import Client

class TestAddProgrammer(test.TestCase):
    def test_got_to_add_programmer_page(self):
        response = Client().get("/addProgrammer")
        self.assertEqual(response.status_code, 200)