# import By class from selenium to locate web elements
from selenium.webdriver.common.by import By

# import BasePage so this page inherits driver and wait utilities
from pages.base_page import BasePage

# import step decorator used for logging test execution steps
from utils.step_decorator import step


# create SidebarMenuPage class which inherits BasePage
class SidebarMenuPage(BasePage):

    # LOCATORS----------------------------------------------------------

    # locator for hamburger menu button
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    # locator for sidebar close button
    CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")

    # locator for All Items option
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")

    # locator for About option
    ABOUT = (By.ID, "about_sidebar_link")

    # locator for Logout option
    LOGOUT = (By.ID, "logout_sidebar_link")

    # locator for Reset App State option
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")

    # locator for sidebar menu container
    SIDEBAR_MENU = (By.CLASS_NAME, "bm-menu")


    # step decorator to log opening sidebar menu
    @step("Open sidebar menu")
    def open_menu(self):

        # wait until menu button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.MENU_BUTTON)

        # click hamburger menu button
        button.click()


    # step decorator to log closing sidebar menu
    @step("Close sidebar menu")
    def close_menu(self):

        # wait until close button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.CLOSE_BUTTON)

        # click close button
        button.click()


    # step decorator to click All Items option
    @step("Click All Items option")
    def click_all_items(self):

        # wait until All Items option becomes clickable
        option = self.wait_utils.wait_for_clickable(self.ALL_ITEMS)

        # click All Items
        option.click()


    # step decorator to click About option
    @step("Click About option")
    def click_about(self):

        # wait until About option becomes clickable
        option = self.wait_utils.wait_for_clickable(self.ABOUT)

        # click About
        option.click()


    # step decorator to click Logout option
    @step("Click Logout option")
    def click_logout(self):

        # wait until Logout option becomes clickable
        option = self.wait_utils.wait_for_clickable(self.LOGOUT)

        # click Logout
        option.click()


    # step decorator to click Reset App State option
    @step("Click Reset App State option")
    def click_reset_app_state(self):

        # wait until Reset App State option becomes clickable
        option = self.wait_utils.wait_for_clickable(self.RESET_APP_STATE)

        # click Reset App State
        option.click()


    # step decorator to check sidebar visibility
    @step("Check sidebar visibility")
    def is_sidebar_visible(self):

        # wait until sidebar menu container becomes visible
        element = self.wait_utils.wait_for_visibility(self.SIDEBAR_MENU)

        # return True if sidebar is displayed
        return element.is_displayed()