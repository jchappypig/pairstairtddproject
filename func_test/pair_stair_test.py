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

        programmer1_name = "Wang Qian"
        programmer2_name = "Huan Huan"
        self.add_programmer(programmer1_name)
        self.add_programmer(programmer2_name)

        #TODO
        #Go to pair stair page






    def tearDown(self):
        self.driver.close()


