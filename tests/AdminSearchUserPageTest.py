import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AdminSearchUserPageTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.fullscreen_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        self.login()
        

    def test001SearchByUsername(self):
        userInput = self.driver.find_element(By.CSS_SELECTOR, "input[class='oxd-input oxd-input--active']")
        userInput.send_keys("test")
        sleep(10)

