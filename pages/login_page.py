# import By locator strategy
from selenium.webdriver.common.by import By

# import BasePage
from pages.base_page import BasePage

# import step decorator
from utils.step_decorator import step


class LoginPage(BasePage):

    """
    Page Object class for login functionality
    """

    # LOCATORS----------------------------------------------------------

    # locator for username field
    USERNAME_INPUT = (By.ID, "user-name")

    # locator for password field
    PASSWORD_INPUT = (By.ID, "password")

    # locator for login button
    LOGIN_BUTTON = (By.ID, "login-button")

    # locator for login error message
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    @step("Enter Username")
    def enter_username(self, username):

        # wait until username field is visible
        element = self.wait_utils.wait_for_visibility(self.USERNAME_INPUT)

        # clear existing text
        element.clear()

        # type username
        element.send_keys(username)

    @step("Enter Password")
    def enter_password(self, password):

        # wait until password field is visible
        element = self.wait_utils.wait_for_visibility(self.PASSWORD_INPUT)

        # clear existing text
        element.clear()

        # type password
        element.send_keys(password)

    @step("Click Login Button")
    def click_login(self):

        # wait until login button becomes clickable
        element = self.wait_utils.wait_for_clickable(self.LOGIN_BUTTON)

        # click login button
        element.click()

    @step("Perform Login")
    def login(self, username, password):

        # enter username
        self.enter_username(username)

        # enter password
        self.enter_password(password)

        # click login button
        self.click_login()

    @step("Get error message")
    def get_error_message(self):

        # wait until error message becomes visible
        element = self.wait_utils.wait_for_visibility(self.ERROR_MESSAGE)

        # return text of error message
        return element.text