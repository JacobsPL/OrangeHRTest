from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseTest import BaseTest
from BaseTest import mainPage
from tests.LoginPageTest import LoginPageObject




class AdminSearchUserPage:

        def __init__(self, driver):
            super().__init__()  # Call the constructor of the BaseTest class
            self.driver = driver

        def login_and_go_to_admin_user_search_page(self):
            LoginPageObject.login(LoginPageObject(self.driver), "Admin", "admin123")
            sleep(3)
            admin = mainPage.getMenuElement(mainPage(self.driver),"Admin")
            admin.click()

        def get_user_input(self):
            list = self.driver.find_elements(By.CSS_SELECTOR, "input[class='oxd-input oxd-input--active']")
            return list[1]

        def det_user_role_dropdown(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-select-text oxd-select-text--active']")[0]

        def get_employee_name_input(self):
            return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        def get_status_dropdown(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-select-text oxd-select-text--active']")[1]

        def get_submit_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        def get_reest_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--ghost']")

        def get_add_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")

        def get_search_results(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-table-row oxd-table-row--with-border']")

        def get_checkbox_from_record(self, row_element):
            return row_element.find_element(By.CSS_SELECTOR, "div[class='oxd-checkbox-wrapper']")

        def get_username_from_record(self, webelement):
            return webelement.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[1].text

        def get_employee_name_input(self):
            return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")

        def get_employee_name_input_hint(self):
            return self.driver.find_element(By.CSS_SELECTOR, "div[class='oxd-autocomplete-dropdown --positon-bottom']")

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
                data = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[numberForInfo].text
                if data == searchedPhrase:
                    pass
                else:
                    return False

            if not listOfWebElements:
                return False

            return True

        def get_bin_icon_of_element(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-trash']")

        def get_edit_icon_of_element(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-pencil-fill']")

        def get_dropdown_option(self, option):
            listOfInput = self.driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
            return listOfInput[option]

        def get_delete_all_users_button(self):
            return self.driver.find_element(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")

        def get_yes_delete_button(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")

        def delete_row(self, webelement):
            webelement.find_element(By.CSS_SELECTOR, "button[class='oxd-icon-button oxd-table-cell-action-space']").click()
            self.driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()



class AdminSearchUserPageTest(BaseTest, AdminSearchUserPage):


    def test001_search_by_username(self):

        #I need to somehow move it to some kind of "before test" method or something
        self.login_and_go_to_admin_user_search_page()
        sleep(3)
        userinput = self.get_user_input()
        searchedPchrase = "Admin"
        userinput.send_keys(searchedPchrase)
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()

        #going though list of results and compare name of the resulted record with searched phrase
        #as the search engine works in the way that it only search by the exact phrase, this is the same mechanism
        #I implemented in my test. If at least one name is diferent from the searchresult, the whole test fails
        self.assertTrue(self.verify_user_search_results(list_of_search_result, searchedPchrase, 1))



    def test02_search_by_user_role(self):

        self.login_and_go_to_admin_user_search_page()
        sleep(3)
        self.det_user_role_dropdown().click()
        self.get_dropdown_option(1).click()
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        searchedPchrase = "Admin"
        self.assertTrue(self.verify_user_search_results(list_of_search_result, searchedPchrase, 2))

    def test003_search_by_employee_name(self):

        self.login_and_go_to_admin_user_search_page()

        #As this is a live test system, userbase can change so fixed name is not the best solution
        #Need to pull a database before all tests or create a few users before testing to have this work
        searchedPchrase = "Sandip chole"
        self.get_employee_name_input().send_keys(searchedPchrase)
        sleep(3)
        self.get_dropdown_option(0).click()
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, searchedPchrase, 3))

    def test004_search_by_status(self):
        self.login_and_go_to_admin_user_search_page()
        self.get_status_dropdown().click()
        self.get_dropdown_option(1).click()
        searchedPchrase = "Enabled"
        list_of_search_result = self.get_search_results()
        self.assertTrue(self.verify_user_search_results(list_of_search_result, searchedPchrase, 4))

    def test005_delete_user_from_list(self):
        self.login_and_go_to_admin_user_search_page()
        searchedPchrase = "test employee 2"
        self.get_employee_name_input().send_keys(searchedPchrase)
        sleep(3)
        self.get_dropdown_option(0).click()
        self.get_submit_button().click()
        list_of_search_result = self.get_search_results()
        self.delete_row(list_of_search_result[0])
        list_of_search_result_after = self.get_search_results()
        sleep(3)
        self.assertTrue(list_of_search_result_after < list_of_search_result)
        sleep(3)


    def test999_delete_all_users(self):

        self.login_and_go_to_admin_user_search_page()
        list_of_search_result = self.get_search_results()
        self.get_checkbox_from_record(list_of_search_result[0]).click()
        self.get_delete_all_users_button().click()
        self.get_yes_delete_button().click()
