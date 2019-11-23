import unittest
from selenium import webdriver

import time

from helpers import functional_helpers


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")


    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

           :param driver: webdriver instance
           :param xpath: xpath to element with text to be observed
           :param expected_text: text what we expecting to be found
           :return: None
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')


    def test_check_title_existance_on_login_page(self):
        driver = self.driver
        driver.get(self.login_url)

        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        self.assert_element_text(driver, xpath, expected_text)

    def test_login_success_with_prepared_account(self):
        driver = self.driver
        driver.get(self.login_url)

        user_email = 'bratslavcity@gmail.com'
        user_pass = '12345678'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        expected_text = 'TestName TestSurname'

        functional_helpers.user_login(driver, user_email, user_pass)
        time.sleep(3)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_login_authorization_failed__with_incorrect_email_and_pass(self):
        driver = self.driver
        driver.get(self.login_url)

        user_email = 'bratslavcity1@gmail.com'
        user_pass = '123456789'
        alert_xpath = '//*[@class="alert alert-danger"]'
        authentication_failed_msg = 'Authentication failed.'

        functional_helpers.user_login(driver, user_email, user_pass)
        time.sleep(3)
        self.assert_element_text(driver, alert_xpath, authentication_failed_msg)



    def test_check_product_name(self):
        driver = self.driver
        driver.get(self.sample_product_url)

        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'

        self.assert_element_text(driver, name_xpath, expected_product_name)


    def test_check_product_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)

        expected_product_price = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'

        self.assert_element_text(driver, price_xpath, expected_product_price)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()