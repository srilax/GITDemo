from selenium.webdriver.common.by import By


class CheckoutPage:

    productTitle = (By.CSS_SELECTOR, ".card-title a")

    productFooter = (By.CSS_SELECTOR, ".card-footer button")


    def __init__(self, driver):
        self.driver = driver

    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.productTitle)
# since cardTitle is class variable, use classname.variablename

    def getProductFooters(self):
        return self.driver.find_elements(*CheckoutPage.productFooter)
