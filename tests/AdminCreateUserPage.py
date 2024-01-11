from selenium.webdriver.common.by import By
from time import sleep
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseTest import BaseTest
from AdminSearchUserPageTest import AdminSearchUserPage
from DataFactory import DataFactory


class AdminCreateUserPage:
    def __init__(self, driver):
        super().__init__()  # Call the constructor of the BaseTest class
        self.driver = driver

    def login_and_go_to_create_user_page(self):
        AdminSearchUserPage.login_and_go_to_admin_user_search_page(AdminSearchUserPage(self.driver))
        add_user_button = self.driver.find_element(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        add_user_button.click()

    def get_user_role_input_option(self,role):
        list_of_input = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
        return list_of_input[role]

    def get_dropdown_option(self,option):
        list_of_input = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
        return list_of_input[option]

    def get_user_role_dropDown(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"div[class='oxd-select-text-input']")[0]

    def get_status_drop_down(self):
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

    def create_initial_users(self):

        database = DataFactory
        users = database.get_all_users(database)
        self.login_and_go_to_create_user_page()

        for i in users:
            self.get_user_role_dropDown().click()
            if DataFactory.get_user_role_from_record(database,i) == "Admin":
                self.get_dropdown_option(1).click()
            else:
                self.get_dropdown_option(2).click()

            self.get_status_drop_down().click()
            if DataFactory.get_status_from_record(database,i) == "Enabled":
                self.get_dropdown_option(1).click()
            else:
                self.get_dropdown_option(2).click()

            employee_name = DataFactory.get_employee_name_from_record(database,i)
            self.get_employee_name().send_keys(employee_name)
            sleep(3)
            self.get_dropdown_option(0).click()

            #WTF ???
            user_name = DataFactory.get_user_name_from_record(database,i)
            self.get_username_input().send_keys(user_name)

            password = DataFactory.get_password_from_record(database, i)
            self.get_password_input().send_keys(password)
            self.get_confirm_password_input().send_keys(password)

            self.get_save_button().click()
            self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']").click()


class AdminCreateUserTest(BaseTest, AdminCreateUserPage):

    def test001_create_user_happy_path(self):
        self.login_and_go_to_create_user_page()
        self.get_user_role_dropDown().click()
        self.get_dropdown_option(1).click()
        self.get_status_drop_down().click()
        self.get_dropdown_option(1).click()
        self.get_password_input().send_keys("password123")
        self.get_confirm_password_input().send_keys("password123")
        self.get_employee_name().send_keys("T")
        #Need to add explicit wait later
        sleep(3)
        self.get_dropdown_option(0).click()
        jacobs = "Jacobs003"
        self.get_username_input().send_keys(jacobs)
        self.get_save_button().click()

        #TO DO:
        #Add the assertion that correct message is displayed and that user can be found in user list
        sleep(3)

    def test999_input_users_from_database_to_system(self):
        self.create_initial_users()

