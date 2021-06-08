import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')  # to specify the file location to store logs use 'fileHandler'
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def explicitWait(self, text):
        expWait = WebDriverWait(self.driver, 8)
        expWait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

# for Select dropdown in test_HomePage.py
    def select(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)