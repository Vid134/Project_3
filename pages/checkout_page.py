# import By class to locate elements
from selenium.webdriver.common.by import By

# import BasePage so this page can inherit driver and wait utilities
from pages.base_page import BasePage

# import step decorator used for logging steps in the framework
from utils.step_decorator import step

class CheckoutPage(BasePage):


    # LOCATORS----------------------------------------------------------

    # locator for the page title
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")

    # locator for first name input field
    FIRST_NAME_INPUT = (By.ID, "first-name")

    # locator for last name input field
    LAST_NAME_INPUT = (By.ID, "last-name")

    # locator for zip/postal code input field
    ZIP_CODE_INPUT = (By.ID, "postal-code")

    # locator for continue button
    CONTINUE_BUTTON = (By.ID, "continue")

    # locator for cancel button
    CANCEL_BUTTON = (By.ID, "cancel")

    # locator for error message shown when validation fails
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # method to get checkout page title
    @step("Get checkout title")
    def get_checkout_title(self):

        # wait until the title becomes visible
        title = self.wait_utils.wait_for_visibility(self.CHECKOUT_TITLE)

        # return title text
        return title.text

    @step("Enter first name in checkout form")
    def enter_first_name(self, first_name):

        # wait until the first name field becomes visible
        element = self.wait_utils.wait_for_visibility(self.FIRST_NAME_INPUT)

        # clear any existing text from the field
        element.clear()

        # type the first name provided in the method argument
        element.send_keys(first_name)

    # step decorator to log entering last name
    @step("Enter last name in checkout form")
    def enter_last_name(self, last_name):
        # wait until last name field becomes visible
        element = self.wait_utils.wait_for_visibility(self.LAST_NAME_INPUT)

        # clear existing text
        element.clear()

        # enter last name
        element.send_keys(last_name)

    # step decorator to log entering zip code
    @step("Enter zip code in checkout form")
    def enter_zip_code(self, zip_code):
        # wait until zip code field becomes visible
        element = self.wait_utils.wait_for_visibility(self.ZIP_CODE_INPUT)

        # clear any existing text
        element.clear()

        # enter the zip/postal code
        element.send_keys(zip_code)

    # step decorator to log clicking continue button
    @step("Click Continue button on checkout page")
    def click_continue(self):

        # wait until continue button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.CONTINUE_BUTTON)

        # click continue button
        button.click()

    # step decorator to log clicking cancel button
    @step("Click Cancel button on checkout page")
    def click_cancel(self):

        # wait until cancel button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.CANCEL_BUTTON)

        # click cancel button
        button.click()

    # step decorator to log retrieval of error message
    @step("Get checkout form error message")
    def get_error_message(self):

        # wait until error message becomes visible
        error = self.wait_utils.wait_for_visibility(self.ERROR_MESSAGE)

        # return the text of the error message
        return error.text