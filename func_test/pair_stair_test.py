from selenium import webdriver

import unittest

class TestPairStair(unittest.TestCase):

    def add_programmer(self, programmer_name):
        programmer_name_textbox = self.driver.find_element_by_id('programmer_name_tb')
        programmer_name_textbox.send_keys(programmer_name)
        submit_button = self.driver.find_element_by_id('add_programmer_btn')
        submit_button.click()


    def test_create_pair_stair_table(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/addProgrammer')
        self.assertEqual(self.driver.title, 'Add Programmer')

        self.add_programmer("Wang Qian")
        self.add_programmer("Huan Huan")

        self.driver.get('http://localhost:8000:/pairStair')
        self.assertEqual(self.driver.title, 'Show PairStair')

        #TODO
        #show pair stair








    def tearDown(self):
        self.driver.close()


