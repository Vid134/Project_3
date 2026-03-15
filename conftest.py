# import pytest library
import pytest

# import driver factory to create browser instance
from utils.driver_factory import DriverFactory

## import Login page for actions and validations
from pages.login_page import LoginPage

#import capture screenshot to create browser instance
from utils.screenshot_helper import capture_screenshot


@pytest.fixture(scope="function")
def driver():
    """
    PyTest fixture to initialize and close browser
    """

    # create browser driver using DriverFactory
    driver = DriverFactory.get_driver()

    # open SauceDemo website
    driver.get("https://www.saucedemo.com/")

    # yield driver to test cases
    yield driver

    # after test execution close the browser
    driver.quit()



@pytest.fixture
def login(driver):

    # create login page object
    login_page = LoginPage(driver)

    # login using valid credentials
    login_page.login("standard_user", "secret_sauce")

    # return driver after login
    yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("login")
        if driver:
            capture_screenshot(driver, item.name)
