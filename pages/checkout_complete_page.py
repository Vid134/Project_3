# import By class for locating elements
from selenium.webdriver.common.by import By

# import BasePage to inherit driver functionality
from pages.base_page import BasePage

# import step decorator
from utils.step_decorator import step


# create CheckoutCompletePage class
class CheckoutCompletePage(BasePage):


    # LOCATORS----------------------------------------------------------


    # locator for success message
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    # locator for order confirmation text
    CONFIRM_TEXT = (By.CLASS_NAME, "complete-text")

    # locator for back home button
    BACK_HOME = (By.ID, "back-to-products")


    # method to get success message
    @step("Get order success message")
    def get_success_message(self):

         # wait until element of success message becomes visible
        element = self.wait_utils.wait_for_visibility(self.SUCCESS_MESSAGE)

        #return text of the element
        return element.text


    # method to get confirmation text
    @step("Get order confirmation text")
    def get_confirmation_text(self):

        # wait until element of confirm text becomes visible
        element = self.wait_utils.wait_for_visibility(self.CONFIRM_TEXT)

        ##return text of the element
        return element.text


    # method to click back home button
    @step("Click back home button")
    def click_back_home(self):

        # wait until element of confirm text becomes clickable
        button = self.wait_utils.wait_for_clickable(self.BACK_HOME)

        #click button
        button.click()