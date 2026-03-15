# import ProductsPage class to perform actions on the products page
from pages.products_page import ProductsPage

# import CartPage class to perform actions and validations on the cart page
from pages.cart_page import CartPage

# import checkout page class to perform actions and validations on the checkout page
from pages.checkout_page import CheckoutPage


####------------------------------TEST CASE 13---------------------------------------TEST SUITE

def test_cart_icon_navigation(login):
    # create an object of ProductsPage using the driver from the login fixture
    products_page = ProductsPage(login)

    # click the cart icon present on the products page
    products_page.open_cart()

    # verify that the current URL contains the word "cart"
    # this confirms the user navigated to the cart page
    assert "cart" in login.current_url


####------------------------------TEST CASE 14---------------------------------------TEST SUITE-

def test_product_added_to_cart(login):
    # create products page object
    products_page = ProductsPage(login)

    # add the first available product to the cart
    products_page.add_first_product_to_cart()

    # open the cart page
    products_page.open_cart()

    # create cart page object to interact with cart elements
    cart_page = CartPage(login)

    # get the list of product names displayed in the cart
    cart_products = cart_page.get_cart_product_names()

    # verify that at least one product is present in the cart
    assert len(cart_products) > 0


####------------------------------TEST CASE 15-----------------------------------TEST SUITE

def test_product_details_in_cart(login):
    # create products page object
    products_page = ProductsPage(login)

    # add a product to the cart
    products_page.add_first_product_to_cart()

    # open the cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # retrieve product name displayed in cart
    product_name = cart_page.get_product_name()

    # retrieve product price displayed in cart
    product_price = cart_page.get_product_price()

    # retrieve product quantity displayed in cart
    product_quantity = cart_page.get_product_quantity()

    # verify product name is displayed
    assert product_name != ""

    # verify product price is displayed
    assert product_price != ""

    # verify product quantity is displayed
    assert product_quantity != ""


####------------------------------TEST CASE 16-----------------------------------------ADDITIONAL


def test_remove_product_from_cart(login):
    # create products page object
    products_page = ProductsPage(login)

    # add a product to the cart
    products_page.add_first_product_to_cart()

    # open the cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # remove the product from the cart
    cart_page.remove_product()

    # verify that the cart is empty after removing the product
    assert cart_page.is_cart_empty()


####------------------------------TEST CASE 17-------------------------------------------ADDITIONAL


def test_continue_shopping_navigation(login):
    # create products page object
    products_page = ProductsPage(login)

    # open the cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click the Continue Shopping button
    cart_page.click_continue_shopping()

    # verify user is redirected back to products page
    assert "inventory" in login.current_url


####------------------------------TEST CASE 18-----------------------------------------------ADDITIONAL

def test_checkout_navigation(login):
    # create products page object
    products_page = ProductsPage(login)

    # add a product to the cart
    products_page.add_first_product_to_cart()

    # open the cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click the Checkout button
    cart_page.click_checkout()

    checkout_page = CheckoutPage(login)

    # verify that the user is redirected to the checkout step one page
    assert checkout_page.get_checkout_title() == "Checkout: Your Information"