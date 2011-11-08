import os
from django import test
from django.test.client import Client
from pair_stair.models import Programmer, Pair
from pair_stair.views import add_programmer

class TestAddProgrammer(test.TestCase):
    def test_got_to_add_programmer_page(self):
        response = Client().get("/addProgrammer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_programmer.html')

    def test_got_to_pair_stair_page(self):
        response = Client().get("/pairStair/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pairStair.html')

    def test_go_to_remove_all_programmers_page(self):
        response = Client().get("/removeAllProgrammers/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'remove_all_programmers.html')

    def test_add_programmer_through_page(self):

        previous_num_of_programmers = Programmer.objects.count()

        programmer_name = "Wang Qian"
        Client().post("/addProgrammer/", {"programmer_name_tb": programmer_name})

        current_num_of_programmers = Programmer.objects.count()

        self.assertEqual(current_num_of_programmers - previous_num_of_programmers, 1)
        self.assertIn(Programmer.objects.get(name = programmer_name), Programmer.objects.all())

    def test_add_one_programmer(self):
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

    def test_should_redirect_to_add_programmer_page_after_add_programmer(self):
        response = Client().post("/addProgrammer/", {'programmer_name_tb':'Huan Huan'})
        self.assertEqual(response.status_code, 200)

    def test_removed_all_programmers(self):
        self.add_two_programmers_to_db("Wang Qian", "Huan Huan")

        Client().get("/removeAllProgrammers/")

        num_of_programmers = Programmer.objects.count()
        num_of_pairs = Pair.objects.count()

        self.assertEqual(num_of_programmers, 0)
        self.assertEqual(num_of_pairs, 0)

    def test_mark_pair(self):
        pair, programmer1, programmer2 = self.add_two_programmers_to_db("Wang Qian", "Huan Huan")
        Client().get(os.path.join("/pairStair", str(programmer1.id), str(programmer2.id)))
        pair = Pair.objects.get(programmer1=programmer1, programmer2=programmer2)
        self.assertEqual(pair.count, 1)

    def add_two_programmers_to_db(self, programmer1_name, programmer2_name):
        programmer1 = Programmer(name=programmer1_name)
        programmer1.save()
        programmer2 = Programmer(name=programmer2_name)
        programmer2.save()
        pair = Pair(programmer1=programmer1, programmer2=programmer2, count=0)
        pair.save()
        return pair, programmer1, programmer2



