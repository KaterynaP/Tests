import unittest
from selenium import webdriver

import time

# strona główna,
# strona produktów typu art,
# strona produktów typu clothes,
# strona produktów typu accessories,
# strona logowania

class LostHatSmokeTests(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.art_products_url = self.base_url + '9-art'
        self.clothes_products_url = self.base_url + '3-clothes'
        self.accessories_products_url = self.base_url + '6-accessories'
        self.login_url = self.base_url + 'login'
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_title(self, url, expected_title):
        """Comparing expected title with current webpage title

           :param driver: webdriver instance
           :param actual_title: current webpage title found
           :param expected_title: title what we expecting to be found
           :return: None
        """
        actual_title = self.get_page_title(url)
        print(f'Actual title: {actual_title}')
        self.assertEqual(actual_title, expected_title,
                         f'Expected title differ from actual on page: {url}')


    def test_check_mainpage_title(self):

        expected_title = 'Lost Hat'
        self.assert_element_title(self.base_url, expected_title)

    def test_check_subpage_products_art_title(self):

        expected_title = 'Art'
        self.assert_element_title(self.art_products_url, expected_title)

    def test_check_subpage_products_clothes_title(self):

        expected_title = 'Clothes'
        self.assert_element_title(self.clothes_products_url, expected_title)

    def test_check_subpage_products_accessories_title(self):

        expected_title = 'Accessories'
        self.assert_element_title(self.accessories_products_url, expected_title)



    def test_check_subpage_loginpage_title(self):

        expected_title = 'Login'
        self.assert_element_title(self.login_url, expected_title)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()