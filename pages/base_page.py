# import expected_conditions for element conditions
from selenium.webdriver.support import expected_conditions as EC

# import wait utils from utils
from utils.wait_utils import WaitUtils


class BasePage:
    """
    BasePage is the parent class for all page classes.
    It contains common reusable methods like click, enter text, get text etc.
    """

    # Constructor method -- runs automatically when a page object is created
    def __init__(self, driver):
        # store driver instance so every page can use the same browser
        self.driver = driver

        # create a WebDriverWait object with 10 seconds timeout
        self.wait_utils = WaitUtils(driver)

    ##Generic click method to click any element safely
    def click(self, locator):
        """
        Click an element after waiting for it to be clickable
        """

        # wait until the element becomes clickable
        element = self.wait_utils.wait_for_clickable(locator)

        # perform click action
        element.click()

    # Generic click method to enter text into input fields
    def enter_text(self, locator, text):
        """
        Enter text into an input field
        """

        # wait until the element becomes visible
        element = self.wait_utils.wait_for_visibility(locator)

        # clear existing text
        element.clear()

        # type the given text
        element.send_keys(text)

    ##Generic method to fetch visible text from any element
    def get_text(self, locator):
        """
        Retrieve text from an element
        """

        # wait until element is visible
        element = self.wait_utils.wait.until(EC.visibility_of_element_located(locator))

        # return the text of that element
        return element.text

    ## Generic method to fetch visible element from a page
    def get_elements(self, locator):
        """
        Get multiple elements from a page
        """

        # wait until elements appear in DOM
        self.wait_utils.wait.until(EC.presence_of_all_elements_located(locator))

        # return list of elements
        return self.driver.find_elements(*locator)