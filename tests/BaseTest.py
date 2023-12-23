import unittest
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.fullscreen_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()

    def test001LoginHappyPath(self):
        self.login("Admin", "admin123")
        dashBoardTitle = self.driver.find_element(By.CSS_SELECTOR, "h6[class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
        self.assertEqual(dashBoardTitle, "Dashboard")

    def test002LoginNoPasswordNoLogin(self):
        self.login("", "")
        requriedMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requriedMessagesList),2)
        self.assertEqual(requriedMessagesList[0].text,"Required")
        self.assertEqual(requriedMessagesList[1].text,"Required")

    def test003LoginNoLogin(self):
        self.login("", "admin123")
        requredMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requredMessagesList), 1)
        self.assertEqual(requredMessagesList[0].text, "Required")

    def test004LoginNoPassword(self):
        self.login("Admin", "")
        requredMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requredMessagesList), 1)
        self.assertEqual(requredMessagesList[0].text, "Required")

    def test005LoginWrongLogin(self):
        self.login("WrongAdmin", "admin123")
        wrongCridentialsAlert = self.driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.assertEqual(wrongCridentialsAlert.text,"Invalid credentials")

    def test006LoginWrongPassword(self):
        self.login("Admin", "wrongPassword")
        wrongCridentialsAlert = self.driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.assertEqual(wrongCridentialsAlert.text,"Invalid credentials")

    def login(self,login,password):
        inputLogin = self.driver.find_element(By.CSS_SELECTOR, "input[name=username]")
        inputPassword = self.driver.find_element(By.CSS_SELECTOR, "input[name=password]")
        loginButton = self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
        inputPassword.send_keys(password)
        inputLogin.send_keys(login)
        loginButton.send_keys(password)
        loginButton.click()
