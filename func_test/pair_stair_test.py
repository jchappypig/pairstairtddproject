from meld3.example import element
from selenium import webdriver

import unittest
from selenium.common.exceptions import NoSuchElementException
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

    def test_mark_pair(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/addProgrammer')
        self.add_programmer("Wang Qian")
        self.add_programmer("Huan Huan")

        self.driver.get('http://localhost:8000:/pairStair')
        mark_pair_link = self.driver.find_element(By.CSS_SELECTOR, '.pair_count')
        self.assertEqual('0', mark_pair_link.text)

        mark_pair_link.click()
        self.assertEqual(self.driver.title, 'Show PairStair')

        mark_pair_link = self.driver.find_element(By.CSS_SELECTOR, '.pair_count')
        self.assertEqual('1', mark_pair_link.text)

    def test_navigate_between_add_programmer_page_and_pair_stair_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/pairStair')
        add_programmer_link = self.driver.find_element_by_id('add_programmer_link')
        add_programmer_link.click()
        self.assertEqual(self.driver.title, 'Add Programmer')
        pair_stair_link = self.driver.find_element_by_id('pair_stair_link')
        pair_stair_link.click()
        self.assertEqual(self.driver.title, 'Show PairStair')

    def test_indicate_not_enough_programmer_on_pair_stair_page_with_one_programmer(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/removeAllProgrammers')
        self.driver.get('http://localhost:8000:/addProgrammer')
        self.add_programmer("Wang Qian")
        
        self.driver.get('http://localhost:8000:/pairStair')
        try:
            self.driver.find_element_by_id('no_programmer_msg')
            pass
        except NoSuchElementException:
            self.fail('Unexpected exception thrown: NoSuchElementException')

    def test_indicate_not_enough_programmer_on_pair_stair_page_with_no_programmer(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/removeAllProgrammers')
        self.driver.get('http://localhost:8000:/pairStair')
        try:
            self.driver.find_element_by_id('no_programmer_msg')
            pass
        except NoSuchElementException:
            self.fail('Unexpected exception thrown: NoSuchElementException')

    def tearDown(self):
        self.driver.get('http://localhost:8000:/removeAllProgrammers')
        self.driver.close()


