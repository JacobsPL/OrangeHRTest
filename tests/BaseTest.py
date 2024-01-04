import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


class mainPage:

    def __init__(self, driver):
        super().__init__()  # Call the constructor of the BaseTest class
        self.driver = driver

    def getListOfTabs(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a[class='oxd-main-menu-item']")

    def getMenuElement(self, element):
        for i in self.getListOfTabs():
            if i.text == element:
                return i