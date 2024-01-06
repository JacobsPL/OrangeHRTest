import unittest
from selenium.webdriver.common.by import By
from BaseTest import BaseTest


class LoginPageObject:

    def __init__(self, driver):
        super().__init__()  # Call the constructor of the BaseTest class
        self.driver = driver

    def get_dashboard_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "h6[class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text

    def login(self, login, password):
        inputLogin = self.driver.find_element(By.CSS_SELECTOR, "input[name=username]")
        inputPassword = self.driver.find_element(By.CSS_SELECTOR, "input[name=password]")
        loginButton = self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
        inputPassword.send_keys(password)
        inputLogin.send_keys(login)
        loginButton.send_keys(password)
        loginButton.click()


class LoginPageTest(BaseTest, LoginPageObject):

    def test001_happy_path(self):
        self.login("Admin", "admin123")
        dashBoardTitle = self.get_dashboard_title()
        self.assertEqual(dashBoardTitle, "Dashboard")

    def test002_no_password_no_login(self):
        self.login("", "")
        requriedMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requriedMessagesList),2)
        self.assertEqual(requriedMessagesList[0].text,"Required")
        self.assertEqual(requriedMessagesList[1].text,"Required")

    def test003_no_login(self):
        self.login("", "admin123")
        requredMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requredMessagesList), 1)
        self.assertEqual(requredMessagesList[0].text, "Required")

    def test004_no_password(self):
        self.login("Admin", "")
        requredMessagesList = self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        self.assertEqual(len(requredMessagesList), 1)
        self.assertEqual(requredMessagesList[0].text, "Required")

    def test005_wrong_login(self):
        self.login("WrongAdmin", "admin123")
        wrongCridentialsAlert = self.driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.assertEqual(wrongCridentialsAlert.text,"Invalid credentials")

    def test006_wrong_password(self):
        self.login("Admin", "wrongPassword")
        wrongCridentialsAlert = self.driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.assertEqual(wrongCridentialsAlert.text,"Invalid credentials")

