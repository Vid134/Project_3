# import By class to locate elements using different locator strategies
from selenium.webdriver.common.by import By

# import BasePage so CartPage can inherit common driver functionality
from pages.base_page import BasePage

# import step decorator used for logging steps in the framework
from utils.step_decorator import step


# create CartPage class which inherits from BasePage
class CartPage(BasePage):


    # LOCATORS----------------------------------------------------------


    # locator for all product names displayed in the cart
    CART_PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    # locator for product price displayed in cart
    CART_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # locator for product quantity displayed in cart
    CART_PRODUCT_QUANTITY = (By.CLASS_NAME, "cart_quantity")

    # locator for remove button inside cart
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")

    # locator for Continue Shopping button
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    # locator for Checkout button
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # locator to check if cart is empty (cart items container)
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    CHECKOUT_TITLE = (By.CLASS_NAME, "title")



    # METHOD: Get product names from cart
    @step("Get cart product names")
    def get_cart_product_names(self):

        # wait until all product name elements appear in cart
        elements = self.wait_utils.wait_for_all_elements(self.CART_PRODUCT_NAMES)

        # create an empty list to store product names
        product_names = []

        # loop through each element in the list
        for element in elements:

            # append the text of each element into product_names list
            product_names.append(element.text)

        # return the list containing all product names
        return product_names



    # METHOD: Get product name
    @step("Get product names")
    def get_product_name(self):

        # wait until the product name is visible
        element = self.wait_utils.wait_for_visibility(self.CART_PRODUCT_NAMES)

        # return the text of the product name
        return element.text



    # METHOD: Get product price
    @step("Get product price")
    def get_product_price(self):

        # wait until the product price element is visible
        element = self.wait_utils.wait_for_visibility(self.CART_PRODUCT_PRICE)

        # return the product price text
        return element.text


    # METHOD: Get product quantity
    @step("Get product quantity")
    def get_product_quantity(self):

        # wait until quantity element becomes visible
        element = self.wait_utils.wait_for_visibility(self.CART_PRODUCT_QUANTITY)

        # return the quantity value displayed
        return element.text



    # METHOD: Remove product from cart
    @step("Remove product")
    def remove_product(self):

        # wait until remove button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.REMOVE_BUTTON)

        # click remove button to delete product from cart
        button.click()



    # METHOD: Click Continue Shopping
    @step("Continue Shopping")
    def click_continue_shopping(self):

        # wait until continue shopping button is clickable
        button = self.wait_utils.wait_for_clickable(self.CONTINUE_SHOPPING_BUTTON)

        # click continue shopping button
        button.click()



    # METHOD: Click Checkout
    @step("Click checkout")
    def click_checkout(self):

        # wait until checkout button becomes clickable
        button = self.wait_utils.wait_for_clickable(self.CHECKOUT_BUTTON)

        # click checkout button
        button.click()


    # METHOD: Verify cart is empty
    @step("Cart is empty")
    def is_cart_empty(self):

        # find all cart item elements
        items = self.driver.find_elements(*self.CART_ITEMS)

        # return True if cart has zero products
        return len(items) == 0


    # METHOD: To get cart items
    @step("Get cart items")
    def get_cart_items(self):

            # fetch all products listed in cart
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")

            # return cart items
            return cart_items


    # METHOD: To get cart item names
    @step("Get cart item names")
    def get_cart_item_names(self):

        # fetch all products listed in cart
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # return cart items names
        return [item.text for item in items]

    # METHOD: To get cart item prices
    @step("Get cart item prices")
    def get_cart_item_prices(self):
        # locate all price elements for the products listed in the cart
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        # extract price text, remove '$' symbol and convert it to float
        prices = [float(price.text.replace("$", "")) for price in price_elements]

        # return the list of cart product prices
        return prices