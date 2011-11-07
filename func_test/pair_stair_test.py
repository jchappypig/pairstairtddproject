from selenium import webdriver

import unittest

class TestPairStair(unittest.TestCase):
    def test_create_pair_stair_table(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000:/addProgrammer')
        self.assertEqual(self.driver.title, 'Add Programmer')

        #TODO
        #Add programmer

    def tearDown(self):
        self.driver.close()


