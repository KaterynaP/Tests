import unittest
from selenium import webdriver
import time


class MainTests(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def test_demo_login(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_pulpit(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
                         f'Expected title differs from actual for page url: {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def test_demo_main_page_title_text_check(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.find_element_by_xpath('//h1[@class="wborder"]')
        title_text = title.text
        print(f'Title text: {title_text}')
        self.assertEqual('Wersja demonstracyjna serwisu demobank', title_text,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_main_page_next_button_state_check_when_input_is_empty(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        ident_text_field = driver.find_element_by_id('login_id')
        ident_text_field.clear()
        button = driver.find_element_by_xpath('//*[@id="login_next"]')
        button_state = button.get_property('disabled')
        self.assertEqual(True, button_state,
                         f'Expected button state differs from actual for page url: {url}')

    def test_demo_main_page_check_warning_when_input_is_too_short(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        ident_text_field = driver.find_element_by_id('login_id')
        ident_text_field.send_keys(12345)
        question_mark = driver.find_element_by_xpath('//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
        question_mark.click()
        time.sleep(3)
        warning = driver.find_element_by_xpath('//*[@class="error"]')
        warning_text = warning.text
        self.assertEqual("identyfikator ma min. 8 znaków", warning_text,
                         f'Expected warning message differs from actual for page url: {url}')

    def test_demo_main_page_check_respond_when_input_is_ok(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        ident_text_field = driver.find_element_by_id('login_id')
        ident_text_field.send_keys(12345678)
        login_next = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_next.click()
        time.sleep(3)
        login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
        new_login_button_text = login_next_button_element.text
        self.assertEqual('zaloguj się', new_login_button_text,
                         f'Expected login button text: zaloguj się , differ from actual {new_login_button_text}')

    def test_demo_main_page_check_message_after_remind_identifier_click(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        identifier_remind_button = driver.find_element_by_id('ident_rem')
        identifier_remind_button.click()
        time.sleep(3)
        identifier_remind_message_element = driver.find_element_by_xpath('//*[@class="shadowbox-content contact-popup"]')
        identifier_remind_message_element_text = identifier_remind_message_element.text
        identifier_remind_message_element_close_button = driver.find_element_by_xpath('//i[@class="shadowbox-close"]')
        identifier_remind_message_element_close_button.click()
        self.assertEqual("ta funkcja jest niedostępna", identifier_remind_message_element_text,
                         f'Expected message differs from actual for page url: {url}')

    def test_demo_main_page_check_if_loged_in_after_correct_login_and_password_input(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        driver.get(url)
        identifier_text_field = driver.find_element_by_id('login_id')
        identifier_text_field.send_keys(12345678)
        password_text_field = driver.find_element_by_id('login_password')
        password_text_field.send_keys(87654321)
        login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_next_button_element.click()
        time.sleep(3)
        new_page_element = driver.find_element_by_xpath('//div[@class="category active"]//*[@class="show-page-loader"]')
        new_page_element_text = new_page_element.text
        self.assertEqual("mój pulpit", new_page_element_text,
                         f'Expected new element text differs from actual for page url: {url}')


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
