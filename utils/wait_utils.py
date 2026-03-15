# import WebDriverWait class for applying explicit waits
from selenium.webdriver.support.ui import WebDriverWait

# import expected_conditions for checking element states
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    """
    WaitUtils provides reusable explicit wait methods
    to handle dynamic web elements.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize wait utility with driver and timeout
        """

        # store driver instance
        self.driver = driver

        # create WebDriverWait object with given timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        """
        Wait until element becomes visible on the page
        """

        # wait until the element located by locator is visible
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        """
        Wait until element becomes clickable
        """

        # wait until the element located by locator is clickable
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator):
        """
        Wait until element exists in DOM
        """

        # wait until element is present in the DOM
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_all_elements(self, locator):
        """
        Wait until multiple elements are present
        """

        # wait until all elements appear in DOM
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )