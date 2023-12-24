import unittest
from selenium.webdriver.common.by import By
from BaseTest import BaseTest
from loginPage import LoginPageObject


class LoginPageTest(BaseTest, LoginPageObject):

    def test001LoginHappyPath(self):
        self.login("Admin", "admin123")
        dashBoardTitle = self.get_dashboard_title()
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

