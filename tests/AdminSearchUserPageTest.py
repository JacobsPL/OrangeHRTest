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

        def loginAndGoToAdminUserSearchPage(self):
            LoginPageObject.login(LoginPageObject(self.driver), "Admin", "admin123")
            sleep(3)
            admin = mainPage.getMenuElement(mainPage(self.driver),"Admin")
            admin.click()

        def getUserInput(self):
            list = self.driver.find_elements(By.CSS_SELECTOR, "input[class='oxd-input oxd-input--active']")
            return list[1]

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

            if not listOfWebElements:
                return False

            return True

        def getBinIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-trash']")

        def getEditIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-pencil-fill']")

class AdminSearchUserPageTest(BaseTest, AdminSearchUserPage):


    def test001SearchByUsername(self):

        #I need to somehow move it to some kind of "before test" method or something
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
        #As this is a live test system, userbase can change so fixed name is not the best solution
        #Need to pull a database before all tests or create a few users before testing to have this work
        searchedPchrase = "Alice Duval"
        nameInput.send_keys(searchedPchrase)
        sleep(3)
        self.getEmployeeNameInputHint().click()
        self.getSubmitButton().click()
        listOfSearchResult = self.getSearchResults()
        self.assertTrue(self.verifyUserSearchResults(listOfSearchResult, searchedPchrase,3))



