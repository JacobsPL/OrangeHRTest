from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseTest import BaseTest
from BaseTest import mainPage
from tests.DataFactory import DataFactory
from tests.LoginPageTest import LoginPageObject


class AdminSearchUserPage:

        def __init__(self, driver):
            self.driver = driver

        def login_and_go_to_admin_user_search_page(self):
            LoginPageObject.login(LoginPageObject(self.driver), "Admin", "admin123")
            sleep(3)
            admin = mainPage.get_menu_element(mainPage(self.driver), "Admin")
            admin.click()

        def get_username_input(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "input[class='oxd-input oxd-input--active']")[1]

        def det_user_role_dropdown(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-select-text oxd-select-text--active']")[0]

        def get_dropdown_option(self, option):
            listOfInput = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
            return listOfInput[option]

        def get_employee_name_input(self):
            return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")

        def get_employee_name_input_hint(self):
            return self.driver.find_element(By.CSS_SELECTOR, "div[class='oxd-autocomplete-dropdown --positon-bottom']")

        def get_status_dropdown(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-select-text oxd-select-text--active']")[1]

        def get_submit_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        def get_reset_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--ghost']")

        def get_add_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")

        def get_search_results(self):
            sleep(2)
            #WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='oxd-table-cell oxd-padding-cell']")))
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-table-row oxd-table-row--with-border']")

        def get_checkbox_from_record(self, record):
            return record.find_element(By.CSS_SELECTOR, "div[class='oxd-checkbox-wrapper']")

        def get_username_from_record(self, record):
            return record.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[1].text

        def get_bin_icon_of_row(self, row):
            return row.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-trash']")

        def get_edit_icon_of_row(self, row):
            return row.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-pencil-fill']")

        def get_delete_all_users_button(self):
            return self.driver.find_element(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")

        def get_yes_delete_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")

        def delete_row(self, row):
            self.get_bin_icon_of_row(row).click()
            self.driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()

        #THIS NEEDS TO BE VERIFIED AS I SUSPECT THAT IT RETURNS FALSE POSITIVE
        def verify_user_search_results(self, listOfWebElements, searchedPhrase, numberForInfo):
            #numberForInfo explained - pass one of this number to verify searched phrase against corresponding data
            #0-checkbox
            #1-Username
            #2-User Role
            #3-Employee Name
            #4-Status
            #5-Delete
            #6-Edit
            for i in listOfWebElements:
                data = i.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[numberForInfo].text
                print(data)
                if data == searchedPhrase:
                    pass
                else:
                    return False

            if  len(listOfWebElements) == 0:
                return False

            return True

class AdminSearchUserPageTest(BaseTest, AdminSearchUserPage):

    def setUp(self):
        super().set_up()
        self.login_and_go_to_admin_user_search_page()

    def test001_search_by_username(self):
        database = DataFactory
        test_user = DataFactory.get_user_by_id(database,1)
        username = DataFactory.get_username_from_record(database,test_user)

        userinput = self.get_username_input()
        userinput.send_keys(username)
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, username, 1))

    def test02_search_by_user_role(self):
        database = DataFactory
        test_user = DataFactory.get_user_by_id(database,2)
        role = DataFactory.get_user_role_from_record(database,test_user)

        self.det_user_role_dropdown().click()
        self.get_dropdown_option(DataFactory.get_role_option(database,role)).click()
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, role, 2))

    def test003_search_by_employee_name(self):
        database = DataFactory
        test_user = DataFactory.get_user_by_id(database,3)
        employee_name = DataFactory.get_employee_name_from_record(database,test_user)

        self.get_employee_name_input().send_keys(employee_name)
        sleep(3)
        self.get_dropdown_option(0).click()
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, employee_name, 3))

    def test004_search_by_status(self):
        database = DataFactory
        test_user = DataFactory.get_user_by_id(database,4)
        status = DataFactory.get_status_from_record(database,test_user)

        self.get_status_dropdown().click()
        self.get_dropdown_option(DataFactory.get_status_option(database,status)).click()
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, status, 4))

    def test005_delete_user_from_list(self):

        database = DataFactory
        test_user = DataFactory.get_user_by_id(database,5)
        username = DataFactory.get_username_from_record(database,test_user)

        self.get_username_input().send_keys(username)
        self.get_submit_button().click()

        list_of_search_result = self.get_search_results()
        self.delete_row(list_of_search_result[1])
        list_of_search_result_after = self.get_search_results()
        sleep(3)
        self.assertTrue(list_of_search_result_after < list_of_search_result)
        sleep(3)


    def test999_delete_all_users(self):

        list_of_search_result = self.get_search_results()
        self.get_checkbox_from_record(list_of_search_result[0]).click()
        self.get_delete_all_users_button().click()
        self.get_yes_delete_button().click()

    def test_for_test(self):
        search_results = self.get_search_results()

        for i in search_results:
            data = i.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[3].text
            print(data)