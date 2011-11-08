from selenium import webdriver

import unittest
from selenium.webdriver.common.by import By

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

        self.assertEqual(4, len(self.driver.find_elements(By.CSS_SELECTOR, '.name')))
        self.assertEqual(1, len(self.driver.find_elements(By.CSS_SELECTOR, '.pair_count')))

        #TODO add function to mark pairs
        self.assertEqual('0', self.driver.find_element(By.CSS_SELECTOR, '.pair_count').text)

    def tearDown(self):
        self.driver.close()


