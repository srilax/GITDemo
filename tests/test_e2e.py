from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log = self.getLogger()

        log.info("Obtaining the product details")
        # checkoutPage = CheckoutPage(self.driver)  # creating an object for CheckoutPage
        products = checkoutPage.getProductTitles()

        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getProductFooters()[i].click()
                # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()

        self.driver.find_element_by_xpath("//li[@class='nav-item active']/a").click()
        # or by css selector as a[class*='btn-primary']

        assert self.driver.find_element_by_xpath("//h4[@class='media-heading']/a").text == "Blackberry"

        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        log.info("Entering 'In' as input for countries filed.")
        self.driver.find_element_by_css_selector("#country").send_keys("In")

        self.explicitWait("suggestions")   # added explicit wait code in base class and calling the method here.

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[class*='btn-lg']").click()
        successMsg = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        log.info("Text received from the app:" + successMsg)
        assert "Success!" in successMsg

        # To get a screenshot use the following command:
        self.driver.get_screenshot_as_file("screenshot.png")


