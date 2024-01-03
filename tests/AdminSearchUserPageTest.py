from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseTest import BaseTest
from tests.LoginPageTest import LoginPageObject


class AdminSearchUserPage:

        def __init__(self, driver):
            super().__init__()  # Call the constructor of the BaseTest class
            self.driver = driver

        def loginAndGoToAdminUserSearchPage(self):
            strona = LoginPageObject(self.driver)
            strona.login("Admin", "admin123")
            sleep(3)
            admin = self.getMenuElement("Admin")
            admin.click()

            #systemUsersDropdown = self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-caret-down-fill']")
            #systemUsersDropdown.click()

        def getUserInput(self):
            list = self.driver.find_elements(By.CSS_SELECTOR, "input[class='oxd-input oxd-input--active']")
            return list[1]

        def getListOfTabs(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "a[class='oxd-main-menu-item']")

        def getMenuElement(self, element):
            for i in self.getListOfTabs():
                if i.text == element:
                    return i

        def getSubmitButton(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        def getReestButton(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--ghost']")

        def getAddButton(self):
            return self.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")

        def getSearchResults(self):
            return self.driver.find_elements(By.CSS_SELECTOR, "div[class='oxd-table-card']")

        def getUsernameFromRecord(self, webelement):
            return webelement.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[1].text

        def getEmployeeNameInput(self):
            return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")

        def getEmployeeNameInputHint(self):
            return self.driver.find_element(By.CSS_SELECTOR, "div[class='oxd-autocomplete-dropdown --positon-bottom']")

        def verifyUserSearchResults(self, listOfWebElements, searchedPhrase, numberForInfo):
            #numberForInfo explained - pass one of this number to verify searched phrase against corresponding data
            #0-checkbox
            #1-Username
            #2-User Role
            #3-Employee Name
            #4-Status
            for i in listOfWebElements:
                data = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[numberForInfo].text
                if data == searchedPhrase:
                    pass
                else:
                    return False
            return True

        def getBinIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-trash']")

        def getEditIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-pencil-fill']")

class AdminSearchUserPageTest(BaseTest, AdminSearchUserPage):


    def test001SearchByUsername(self):
        self.loginAndGoToAdminUserSearchPage()
        sleep(3)
        userinput = self.getUserInput()
        searchedPchrase = "Admin"
        userinput.send_keys(searchedPchrase)
        self.getSubmitButton().click()
        listOfSearchResult = self.getSearchResults()

        #going though list of results and compare name of the resulted record with searched phrase
        #as the search engine works in the way that it only search by the exact phrase, this is the same mechanism
        #I implemented in my test. If at least one name is diferent from the searchresult, the whole test fails
        self.assertTrue(self.verifyUserSearchResults(listOfSearchResult, searchedPchrase, 1))

    def test002SearchByEmployeeName(self):

        self.loginAndGoToAdminUserSearchPage()

        nameInput = self.getEmployeeNameInput()
        searchedPchrase = "Alice Duval"
        nameInput.send_keys(searchedPchrase)
        sleep(1)
        self.getEmployeeNameInputHint().click()
        self.getSubmitButton().click()
        listOfSearchResult = self.getSearchResults()
        self.assertTrue(self.verifyUserSearchResults(listOfSearchResult, searchedPchrase,3))

        #self.assertTrue(self.verifySearchResults())


