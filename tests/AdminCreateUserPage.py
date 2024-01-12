from selenium.webdriver.common.by import By
from time import sleep
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseTest import BaseTest, mainPage
from AdminSearchUserPageTest import AdminSearchUserPage
from DataFactory import DataFactory
from tests.LoginPageTest import LoginPageObject


class AdminCreateUserPage:
    def __init__(self, driver):
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

    def get_password_error_message(self):
        password_area = self.driver.find_element(By.CSS_SELECTOR, "div[class='oxd-grid-item oxd-grid-item--gutters user-password-cell']")
        return password_area.find_element(By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text

    def get_password_strength_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span[class^='oxd-chip oxd-chip--default orangehrm-password-chip']").text

    def get_username_error_message(self):
        username_area = self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-grid-item oxd-grid-item--gutters']")
        return username_area[3].find_element(By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text

    def create_user(self,user_name, password, conf_password):
        self.get_user_role_dropDown().click()
        self.get_dropdown_option(1).click()
        self.get_status_drop_down().click()
        self.get_dropdown_option(1).click()
        self.get_employee_name().send_keys("T")
        WebDriverWait(self.driver,10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div[class='oxd-autocomplete-dropdown --positon-bottom']"),"Searching...."))

        self.get_dropdown_option(0).click()
        self.get_username_input().send_keys(user_name)
        self.get_password_input().send_keys(password)
        self.get_confirm_password_input().send_keys(conf_password)
        self.get_save_button().click()

    def create_initial_users(self):

        database = DataFactory
        users = database.get_all_users(database)

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

            user_name = DataFactory.get_user_name_from_record(database,i)
            self.get_username_input().send_keys(user_name)

            password = DataFactory.get_password_from_record(database, i)
            self.get_password_input().send_keys(password)
            self.get_confirm_password_input().send_keys(password)

            self.get_save_button().click()
            self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']").click()

    def add_random_number_to_string(self,string,ran_min,ran_max):
        random_int = random.randint(ran_min, ran_max)
        return str(string) + str(random_int)




class AdminCreateUserTest(BaseTest, AdminCreateUserPage):

    def setUp(self):
        super().set_up()
        self.login_and_go_to_create_user_page()

    def test001_create_user_happy_path(self):
        self.create_user(self.add_random_number_to_string("Jacobs",100,999),"password123","password123")

        #TO DO:
        #Add the assertion that correct message is displayed and that user can be found in user list
        sleep(3)

    def test002_all_fields_are_required(self):
        self.get_save_button().click()
        error_messages = self.driver.find_elements(By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        all_fields = self.driver.find_elements(By.CSS_SELECTOR, "div[class^='oxd-grid-item oxd-grid-item--gutters']")
        self.assertEqual(len(error_messages),len(all_fields))

        for i in error_messages:
            self.assertEqual(i.text, "Required")

    def test003_password_different_from_confirm_password(self):
        self.create_user(self.add_random_number_to_string("Jacobs",100,999),"password123","wrong_one")
        WebDriverWait(self.driver,10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"),"Should be at least 5 characters"))
        error_message = self.driver.find_element(By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertEqual(error_message, "Passwords do not match")

    def test004_username_below_5_characters(self):
        self.create_user(self.add_random_number_to_string("J",100,999),"password123", "password123")
        self.assertEqual(self.get_username_error_message(), "Should be at least 5 characters")

    def test005_password_below_7_characters(self):
        self.create_user(self.add_random_number_to_string("Jacobs",100,999), "123456", "123456")
        self.assertEqual(self.get_password_error_message(), "Should have at least 7 characters")

    def test006_password_no_number(self):
        self.create_user(self.add_random_number_to_string("Jacobs",100,999), "password", "password")
        self.assertEqual(self.get_password_error_message(), "Your password must contain minimum 1 number")

    def test007_very_weak_password(self):
        self.get_password_input().send_keys("password123")
        sleep(1.5)
        self.assertEqual(self.get_password_strength_message(), "Very Weak")

    def test008_weak_password(self):
        self.get_password_input().send_keys("password106")
        sleep(1.5)
        self.assertEqual(self.get_password_strength_message(), "Weak")

    def test009_better_password(self):
        self.get_password_input().send_keys("passwordd106")
        sleep(1.5)
        self.assertEqual(self.get_password_strength_message(), "Better")

    def test0010_strong_password(self):
        self.get_password_input().send_keys("passwordddd106")
        sleep(1.5)
        self.assertEqual(self.get_password_strength_message(), "Strong")

    def test0011_strong_password(self):
        self.get_password_input().send_keys("NotSoWeak666")
        sleep(1.5)
        self.assertEqual(self.get_password_strength_message(), "Strongest")

    def test0012_login_new_user(self):
        self.get_user_role_dropDown().click()
        self.get_dropdown_option(1).click()
        self.get_status_drop_down().click()
        self.get_dropdown_option(1).click()
        self.get_employee_name().send_keys("T")
        WebDriverWait(self.driver,10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div[class='oxd-autocomplete-dropdown --positon-bottom']"),"Searching...."))
        self.get_dropdown_option(0).click()
        jacobs_username = self.add_random_number_to_string("Jacobs",100,999)
        self.get_username_input().send_keys(jacobs_username)
        self.get_password_input().send_keys("password123")
        self.get_confirm_password_input().send_keys("password123")
        self.get_save_button().click()

        sleep(5)
        main_page = mainPage(self.driver)
        main_page.get_logged_user_menu().click()
        main_page.get_logout_option().click()

        login_page = LoginPageObject(self.driver)
        login_page.login(jacobs_username,"password123")

        dashBoardTitle = login_page.get_dashboard_title()
        self.assertEqual(dashBoardTitle, "Dashboard")

    def test999_input_users_from_database_to_system(self):
        self.create_initial_users()

