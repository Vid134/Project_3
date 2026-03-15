# import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import Service class to start ChromeDriver service
from selenium.webdriver.chrome.service import Service

# import ChromeDriverManager to automatically download chromedriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """
    DriverFactory is responsible for creating and configuring
    the browser driver instance used in tests.
    """



    @staticmethod
    def get_driver():
        """
        Create and return a Chrome WebDriver instance
        """

        # create a Service object that manages the ChromeDriver executable
        service = Service(ChromeDriverManager().install())

        # create Chrome browser options
        options = Options()

        options.add_argument("--guest")

        options.add_argument("--disable-notifications")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs",prefs)
        options.add_argument("--disable-notifications")


        # start the Chrome browser with service and options
        driver = webdriver.Chrome(service=service, options=options)

        # maximize browser window for better visibility during tests
        driver.maximize_window()

        # return the driver object so tests can use it
        return driver