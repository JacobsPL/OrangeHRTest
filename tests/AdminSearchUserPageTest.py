from selenium.webdriver.common.by import By
from time import sleep
from BaseTest import BaseTest
from tests.LoginPageTest import LoginPageObject


class AdminSearchUserPage(BaseTest):


        def loginAndGoToAdminUserSearchPage(self):
            self.setUp()
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

        def verifyUserSearchResults(self, listOfWebElements, searchedPhrase, ):
            for i in listOfWebElements:
                username = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")[2].text[i]
                if username == searchedPhrase:
                    pass
                else:
                    return False
            return True

        def getBinIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-trash']")

        def getEditIconOfElement(self, webElement):
            return webElement.self.driver.find_element(By.CSS_SELECTOR, "i[class='oxd-icon bi-pencil-fill']")

class AdminSearchUserPageTest(BaseTest):


    def test001SearchByUsername(self):
        adminSearchUserPage = AdminSearchUserPage()
        adminSearchUserPage.loginAndGoToAdminUserSearchPage()
        sleep(3)
        userinput = adminSearchUserPage.getUserInput()
        searchedPchrase = "Admin"
        userinput.send_keys(searchedPchrase)
        adminSearchUserPage.getSubmitButton().click()
        listOfSearchResult = adminSearchUserPage.getSearchResults()

        #going though list of results and compare name of the resulted record with searched phrase
        #as the search engine works in the way that it only search by the exact phrase, this is the same mechanism
        #I implemented in my test. If at least one name is diferent from the searchresult, the whole test fails
        self.assertTrue(adminSearchUserPage.verifyUserSearchResults(listOfSearchResult, searchedPchrase))

    def test002SearchByEmployeeName(self):
        adminSearchUserPage = AdminSearchUserPage()
        adminSearchUserPage.loginAndGoToAdminUserSearchPage()

        nameInput = adminSearchUserPage.getEmployeeNameInput()
        searchedPchrase = "Placeholder"
        nameInput.send_keys(searchedPchrase)
        adminSearchUserPage.getSubmitButton().click()
        listOfSearchResult = adminSearchUserPage.getSearchResults()

        self.assertTrue(adminSearchUserPage.verifyUserSearchResults(listOfSearchResult, searchedPchrase))

        #self.assertTrue(page.verifySearchResults())


