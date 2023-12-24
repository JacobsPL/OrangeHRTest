from selenium.webdriver.common.by import By

from tests import LoginPageTest
import unittest
from selenium import webdriver
from tests.BaseTest import BaseTest


class LoginPageObject:


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
