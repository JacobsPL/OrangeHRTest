import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):

    # def setUp(self): #does not work on Mac M2 :(
    #     self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     self.driver.implicitly_wait(10)

    def set_up(self): #for M2 Apple silicon
        cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=cService)
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def tear_down(self):
        self.driver.quit()
    def check_exists_by_css(self,css_selector):
        try:
            self.driver.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
             return False
        return True

    def check_exists_by_xpath(self,xpath_selector):
        try:
            self.driver.find_element(By.XPATH, xpath_selector)
        except NoSuchElementException:
             return False
        return True


class mainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_list_of_tabs(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a[class='oxd-main-menu-item']")

    def get_menu_element(self, element):
        for i in self.get_list_of_tabs():
            if i.text == element:
                return i

    def get_logged_user_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, "li[class='oxd-userdropdown']")

    def get_logged_user_menu_dropdown_options(self):
        return self.driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']/li")

    def get_about_option(self):
        return self.get_logged_user_menu_dropdown_options()[0]

    def get_support_option(self):
        return self.get_logged_user_menu_dropdown_options()[1]

    def get_change_password_option(self):
        return self.get_logged_user_menu_dropdown_options()[2]

    def get_logout_option(self):
        return self.get_logged_user_menu_dropdown_options()[3]