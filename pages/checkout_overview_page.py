# import By class to locate elements
from selenium.webdriver.common.by import By

# import BasePage so this page can inherit driver and wait utilities
from pages.base_page import BasePage

# import step decorator to log step execution
from utils.step_decorator import step


# create CheckoutOverviewPage class which inherits BasePage
class CheckoutOverviewPage(BasePage):


    # LOCATORS----------------------------------------------------------

    # locator for page title
    PAGE_TITLE = (By.CLASS_NAME, "title")

    # locator for product name displayed in overview
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    # locator for product price
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # locator for payment information text
    PAYMENT_INFO = (By.XPATH, "//div[text()='Payment Information:']/following-sibling::div")

    # locator for shipping information text
    SHIPPING_INFO = (By.XPATH, "//div[text()='Shipping Information:']/following-sibling::div")

    # locator for item total
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")

    # locator for tax value
    TAX = (By.CLASS_NAME, "summary_tax_label")

    # locator for total price
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    # locator for finish button
    FINISH_BUTTON = (By.ID, "finish")

    # locator for cancel button
    CANCEL_BUTTON = (By.ID, "cancel")


    # method to get checkout overview page title
    @step("Get checkout overview page title")
    def get_page_title(self):

        #wait for the visibility of page title
        element = self.wait_utils.wait_for_visibility(self.PAGE_TITLE)

        # return text of the elemeny
        return element.text


    # method to get product name displayed
    @step("Get product name from overview page")
    def get_product_name(self):

        # wait for the visibility of product name
        element = self.wait_utils.wait_for_visibility(self.PRODUCT_NAME)

        # return text of the element
        return element.text


    # method to get product price
    @step("Get product price from overview page")
    def get_product_price(self):

        # wait for the visibility of product price
        element = self.wait_utils.wait_for_visibility(self.PRODUCT_PRICE)

        # return text of the element
        return element.text


    # method to get payment information
    @step("Get payment information")
    def get_payment_info(self):

        # wait for the visibility of payment info
        element = self.wait_utils.wait_for_visibility(self.PAYMENT_INFO)

        # return text of the element
        return element.text


    # method to get shipping information
    @step("Get shipping information")
    def get_shipping_info(self):

        # wait for the visibility of shipping info
        element = self.wait_utils.wait_for_visibility(self.SHIPPING_INFO)

        # return text of the element
        return element.text


    # method to get item total
    @step("Get item total value")
    def get_item_total(self):

        # wait for the visibility of item total
        element = self.wait_utils.wait_for_visibility(self.ITEM_TOTAL)

        # return text of the element
        return element.text


    # method to get tax value
    @step("Get tax value")
    def get_tax(self):

        # wait for the visibility of tax
        element = self.wait_utils.wait_for_visibility(self.TAX)

        # return text of the element
        return element.text


    # method to get total price
    @step("Get total price")
    def get_total(self):

        # wait for the visibility of total
        element = self.wait_utils.wait_for_visibility(self.TOTAL)

        # return text of the element
        return element.text


    # method to click finish button
    @step("Click finish button")
    def click_finish(self):

         # wait for the clickability of finish button
        button = self.wait_utils.wait_for_clickable(self.FINISH_BUTTON)

       #click button
        button.click()


    # method to click cancel button
    @step("Click cancel button")
    def click_cancel(self):

        # wait for the clickability of cancel button
        button = self.wait_utils.wait_for_clickable(self.CANCEL_BUTTON)

      #click button
        button.click()