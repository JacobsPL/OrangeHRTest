from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseTest import BaseTest
from tests.LoginPageTest import LoginPageObject
from AdminSearchUserPageTest import AdminSearchUserPage



class AdminCreateUserPage:
    def __init__(self, driver):
        super().__init__()  # Call the constructor of the BaseTest class
        self.driver = driver

    def loginAndGoToCreateUserPage(self):
        AdminSearchUserPage.login_and_go_to_admin_user_search_page(AdminSearchUserPage(self.driver))
        addUserButton = self.driver.find_element(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        addUserButton.click()

    def getUserRoleInputOption(self,role):
        listOfInput = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
        return listOfInput[role]

    def get_dropdown_option(self,option):
        listOfInput = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
        return listOfInput[option]

    def getUserRoleDropDown(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"div[class='oxd-select-text-input']")[0]

    def getStatusDropDown(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"div[class='oxd-select-text-input']")[1]

    def get_password_input(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"input[type='password']")[0]

    def get_confirm_password_input(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"input[type='password']")[1]

    def get_employee_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")

    def get_username_input(self):
        return self.driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[1]

    def get_save_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

    def get_cancel_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")


class AdminCreateUserTest(BaseTest, AdminCreateUserPage):

    def test001_create_user_happy_path(self):
        self.loginAndGoToCreateUserPage()
        self.getUserRoleDropDown().click()
        self.get_dropdown_option(1).click()
        self.getStatusDropDown().click()
        self.get_dropdown_option(1).click()
        self.get_password_input().send_keys("password123")
        self.get_confirm_password_input().send_keys("password123")
        self.get_employee_name().send_keys("T")
        #Need to add explicit wait later
        sleep(3)
        self.get_dropdown_option(0).click()
        self.get_username_input().send_keys("Jacobs002")
        self.get_save_button().click()

        #TO DO:
        #Add the assertion that correct message is displayed and that user can be found in user list
        sleep(3)


