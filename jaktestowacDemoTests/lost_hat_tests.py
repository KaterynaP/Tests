import unittest
from selenium import webdriver
import time


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def test_check_title_existance_on_login_page(self):
        expected_text = 'Log in to your account'
        driver = self.driver
        driver.get(self.login_url)
        header_element = driver.find_element_by_xpath('//header[@class="page-header"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def test_login_success_with_prepared_account(self):
        driver = self.driver
        driver.get(self.login_url)

        user_email = 'bratslavcity@gmail.com'
        user_pass = '12345678'

        login_field_element = driver.find_element_by_xpath('//*[@name="email" and @class="form-control"]')
        login_field_element.send_keys(user_email)
        password_field_element = driver.find_element_by_xpath('//*[@name="password" and @class="form-control js-child-focus js-visible-password"]')
        password_field_element.send_keys(user_pass)
        sign_in_button_element = driver.find_element_by_id('submit-login')
        sign_in_button_element.click()
        time.sleep(3)
        h1_title_element = driver.find_element_by_xpath('//h1')
        h1_title_element_text = h1_title_element.text
        self.assertEqual('POPULAR PRODUCTS', h1_title_element_text,
                         f'Expected title differs from actual')

    def test_check_product_name_and_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)

        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        expected_product_price = 'PLN23.52'

        product_name_element = driver.find_element_by_xpath('//h1')
        product_name_element_text = product_name_element.text
        product_price_element = driver.find_element_by_xpath('//span[@itemprop="price"]')
        product_price_element_text = product_price_element.text
        self.assertEqual(expected_product_name, product_name_element_text,
                         f'Expected title differs from actual')
        self.assertEqual(expected_product_price, product_price_element_text,
                         f'Expected title differs from actual')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()