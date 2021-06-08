from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()   #equivalent to driver.find_element_by_link_text("Shop")
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

# for test_HomePage.py test case

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)
