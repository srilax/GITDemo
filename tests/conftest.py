import pytest
from selenium import webdriver

# To pass browser names at runtime in command line:
def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setUp(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
    elif browser_name == "IE":
        print("IE")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver                 # To pass the driver variable to class from this fixture.
    yield
    driver.close()