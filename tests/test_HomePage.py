import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("getData")
class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)  # creating an object for HomePage class
        log = self.getLogger()

        homePage.getName().send_keys(getData["name"])
        log.info("first name is" + getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getCheck().click()
        self.select(homePage.getGender(), getData["gender"])
        homePage.getSubmit().click()

        alertText = homePage.getAlert().text
        assert "Success" in alertText
        self.driver.refresh()

    # @pytest.fixture(params= HomePageData.test_HomePage_data)  # to obtain params from the class
    # to obtain params from excel use as follows:
    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param
