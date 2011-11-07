from django import test
from django.test.client import Client
from pair_stair.models import Programmer, Pair
from pair_stair.views import add_programmer

class TestAddProgrammer(test.TestCase):
    def test_got_to_add_programmer_page(self):
        response = Client().get("/addProgrammer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_programmer.html')

    def test_add_programmer(self):
        previous_num_of_programmers = Programmer.objects.count()

        programmer1_name = "Wang Qian"
        add_programmer(programmer1_name)

        current_num_of_programmers = Programmer.objects.count()

        self.assertEqual(current_num_of_programmers - previous_num_of_programmers, 1)
        self.assertIn(Programmer.objects.get(name = programmer1_name), Programmer.objects.all())

    def test_add_pair(self):
        previous_num_of_pairs = Pair.objects.count()

        programmer1_name = "Wang Qian"
        programmer2_name = "Huan Huan"
        add_programmer(programmer1_name)
        add_programmer(programmer2_name)

        current_num_of_pairs = Pair.objects.count()

        self.assertEqual(current_num_of_pairs - previous_num_of_pairs, previous_num_of_pairs * 2 + 1)

    def test_add_programmer_through_page(self):

        previous_num_of_programmers = Programmer.objects.count()

        programmer_name = "Wang Qian"
        Client().post("/addProgrammer/", {"programmer_name_tb": programmer_name})

        current_num_of_programmers = Programmer.objects.count()

        self.assertEqual(current_num_of_programmers - previous_num_of_programmers, 1)
        self.assertIn(Programmer.objects.get(name = programmer_name), Programmer.objects.all())


    def test_got_to_pair_stair_page(self):
        response = Client().get("/pairStair/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pairStair.html')
