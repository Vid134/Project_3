# import By locator strategy
from selenium.webdriver.common.by import By

# import BasePage class
from pages.base_page import BasePage

# import step decorator
from utils.step_decorator import step

# import Select class to handle dropdown
from selenium.webdriver.support.ui import Select

# import random module to select random products
import random
import time


class ProductsPage(BasePage):
    """
    Page Object Model for Products Page
    """
    # LOCATORS----------------------------------------------------------


    # locator for all product containers
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")

    # locator for product names
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    # locator for product prices
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    # locator for add to cart buttons
    ##ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    ADD_TO_CART_BUTTONS = ( By.CSS_SELECTOR,"button.btn_inventory")
    # locator for cart icon
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # locator for cart badge number
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # locator for sorting dropdown
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # locator for product images
    PRODUCT_IMAGES = (By.CLASS_NAME, "inventory_item_img")



    @step("Get all products from page")
    def get_all_products(self):

        # wait until all products appear in DOM
        products = self.wait_utils.wait_for_all_elements(self.PRODUCT_LIST)

        # return list of products
        return products

    @step("Get all product names from page")
    def get_product_names(self):

         # to find elements of product names using locator
         elements = self.driver.find_elements(*self.PRODUCT_NAMES)

         # extract text from each product name
         products_name = [element.text for element in elements]

         # return the list of product names
         return products_name

    @step("Get all product prices from page")
    def get_product_prices(self):

        # locator all product price elements using locator
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)

        #extract price text,remove $ symbol and convert it to float
        prices = [float(price.text.replace("$","")) for price in price_elements]

        # return the list of product prices
        return prices

    @step("Get all product images from page")
    def get_product_images(self):

        # locate all images from locator
        images = self.driver.find_elements(*self.PRODUCT_IMAGES)

        # return the list of  image elements
        return images

    @step("Get all product add to cart option from page")
    def get_product_add_to_cart_options(self):

        # to find cart elements using locator
        cart_elements = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

        # return cart elements
        return cart_elements

    @step("Verify product list is displayed")
    def is_product_list_displayed(self):

        # get all products
        products = self.get_all_products()

        # return True if products exist
        return len(products) > 0

    @step("Verify product details are displayed")
    def verify_product_details(self):

        # get product names
        names = self.wait_utils.wait_for_all_elements(self.PRODUCT_NAMES)

        # get product prices
        prices = self.wait_utils.wait_for_all_elements(self.PRODUCT_PRICES)

        # wait and get all product images
        images = self.wait_utils.wait_for_all_elements(self.PRODUCT_IMAGES)

        # wait and get all add to cart buttons
        buttons = self.wait_utils.wait_for_all_elements(self.ADD_TO_CART_BUTTONS)

        # verify that all elements exist
        return (
                len(names) > 0 and
                len(prices) > 0 and
                len(images) > 0 and
                len(buttons) > 0
        )

    @step("Verify Cart icon visibility")
    def is_cart_icon_visible(self):

         # return cart icon visibility
         return self.driver.find_element(*self.CART_ICON).is_displayed()

    @step("Add first product to cart")
    def add_first_product_to_cart(self):

        # get add to cart buttons
        buttons = self.wait_utils.wait_for_all_elements(self.ADD_TO_CART_BUTTONS)

        # click first product add to cart
        buttons[0].click()

    @step("Verify cart badge increments")
    def get_cart_badge_count(self):

        # wait until cart badge appears
        badge = self.wait_utils.wait_for_visibility(self.CART_BADGE)

        # return badge count as integer
        return int(badge.text)

    @step("Verify cart badge increments")
    def get_cart_badge_count1(self):
        # wait until cart badge appears
        badges = self.driver.find_elements(*self.CART_BADGE)

        if len(badges) == 0:
            return 0
        return int(badges[0].text)


    @step("Add random products to cart")
    def add_random_products(self, count):
            ## fetch all products locator
            all_products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")

            ## select the random  products
            selected_products = random.sample(all_products, count)

            # create a list to store selected product name and price
            selected_products_details = []

            ## to select the product selected
            for products in selected_products:

                 name = products.find_element(By.CLASS_NAME,"inventory_item_name").text
                 # fetch the product name

                 price = products.find_element(By.CLASS_NAME,"inventory_item_price").text
                 # fetch the product price

                 products.find_element(By.CLASS_NAME,"btn_inventory").click()
                 # click the add to cart button for the selected product

                 selected_products_details.append((name, price))
            # store the product name and price in the list

            return selected_products_details
    ## return the selected products details


    @step("Sort products")
    def sort_products(self, option_text):
        """
        Select sorting option from dropdown
        """

        # wait until sorting dropdown becomes visible
        dropdown = self.wait_utils.wait_for_visibility(self.SORT_DROPDOWN)

        # create Select object
        select = Select(dropdown)

        # choose sorting option using visible text
        select.select_by_visible_text(option_text)

    @step("Click the cart icon which navigates to cart page")
    def open_cart(self):
        # to open the cart

        cart = self.wait_utils.wait_for_clickable(self.CART_ICON)
        # wait for clickabilty of cart icon

        cart.click()
        #  click cart


