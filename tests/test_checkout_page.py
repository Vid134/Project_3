# import ProductsPage to interact with products page
from pages.products_page import ProductsPage

# import CartPage to interact with cart page
from pages.cart_page import CartPage

# import CheckoutPage to interact with checkout information page
from pages.checkout_page import CheckoutPage

# import checkout overview page
from pages.checkout_overview_page import CheckoutOverviewPage

# import checkout complete page for browser instance
from pages.checkout_complete_page import CheckoutCompletePage

# import capture screenshot for browser instance
from utils.screenshot_helper import capture_screenshot

####------------------------------TEST CASE 25------------------------------------ADDITIONAL------------------

# test case to verify successful navigation to checkout overview page
def test_checkout_information_valid(login):

    # create products page object using driver from login fixture
    products_page = ProductsPage(login)

    # add first product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout button
    cart_page.click_checkout()

    # create checkout page object
    checkout_page = CheckoutPage(login)

    # enter first name
    checkout_page.enter_first_name("Ganan")

    # enter last name
    checkout_page.enter_last_name("Veerendra")

    # enter zip code
    checkout_page.enter_zip_code("560001")

    # click continue button
    checkout_page.click_continue()

    # verify user navigates to checkout overview page
    assert  login.current_url == "https://www.saucedemo.com/checkout-step-two.html"

####------------------------------TEST CASE 26-------------------------------------------ADDITIONAL--

# test case to verify error when first name is missing
def test_checkout_missing_firstname(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout button
    cart_page.click_checkout()

    # create checkout page object
    checkout_page = CheckoutPage(login)

    # leave first name empty and enter last name
    checkout_page.enter_last_name("Veerendra")

    # enter zip code
    checkout_page.enter_zip_code("560001")

    # click continue
    checkout_page.click_continue()

    # verify error message for missing first name
    assert "First Name is required" in checkout_page.get_error_message()

####------------------------------TEST CASE 27------------------------------------------ADDITIONAL

# test case to verify error when last name is missing
def test_checkout_missing_lastname(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout button
    cart_page.click_checkout()

    # create checkout page object
    checkout_page = CheckoutPage(login)

    # enter first name
    checkout_page.enter_first_name("Ganan")

    # leave last name empty and enter zip code
    checkout_page.enter_zip_code("560001")

    # click continue button
    checkout_page.click_continue()

    # verify last name error message
    assert "Last Name is required" in checkout_page.get_error_message()

####------------------------------TEST CASE 28--------------------------------------ADDITIONAL

# test case to verify error when zip code is missing
def test_checkout_missing_zipcode(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout
    cart_page.click_checkout()

    # create checkout page object
    checkout_page = CheckoutPage(login)

    # enter first name
    checkout_page.enter_first_name("Ganan")

    # enter last name
    checkout_page.enter_last_name("Veerendra")

    # leave zip code empty and click continue
    checkout_page.click_continue()

    # verify zip code error message
    assert "Postal Code is required" in checkout_page.get_error_message()


####------------------------------TEST CASE 29------------------------------------ADDITIONAL

# test case to verify cancel button navigation
def test_checkout_cancel_navigation(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout button
    cart_page.click_checkout()

    # create checkout page object
    checkout_page = CheckoutPage(login)

    # click cancel button
    checkout_page.click_cancel()

    # verify user navigates back to cart page
    assert "cart" in login.current_url


####------------------------------TEST CASE 30-----------------------------------------TEST SUITE

# test checkout overview validations
def test_checkout_overview_validations(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout
    cart_page.click_checkout()

    # create checkout information page object
    checkout_page = CheckoutPage(login)

    # enter first name
    checkout_page.enter_first_name("Ganan")

    # enter last name
    checkout_page.enter_last_name("Veerendra")

    # enter zip code
    checkout_page.enter_zip_code("560001")

    # click continue button
    checkout_page.click_continue()

    # create overview page object
    checkout_overview_page = CheckoutOverviewPage(login)

    # verify page title
    assert checkout_overview_page.get_page_title() == "Checkout: Overview"

    # verify product name exists
    assert checkout_overview_page.get_product_name() != ""

    # verify product price exists
    assert checkout_overview_page.get_product_price() != ""

    # verify payment information
    assert checkout_overview_page.get_payment_info() != ""

    # verify shipping information
    assert checkout_overview_page.get_shipping_info() != ""

    # verify item total exists
    assert checkout_overview_page.get_item_total() != ""

    # verify tax value exists
    assert checkout_overview_page.get_tax() != ""

    # verify total price exists
    assert checkout_overview_page.get_total() != ""


####------------------------------TEST CASE 31----------------------------------------TEST SUITE

# test finish order and complete page
def test_checkout_complete_page(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open cart page
    products_page.open_cart()

    # create cart page object
    cart_page = CartPage(login)

    # click checkout
    cart_page.click_checkout()

    # create checkout information page object
    checkout_page = CheckoutPage(login)

    # enter first name
    checkout_page.enter_first_name("Ganan")

    # enter last name
    checkout_page.enter_last_name("Veerendra")

    # enter zip code
    checkout_page.enter_zip_code("560001")

    # click continue button
    checkout_page.click_continue()

    # to capture screenshot of order summary
    capture_screenshot(login, "order_summary")

    # create checkout information page object
    checkout_overview_page = CheckoutOverviewPage(login)

    # click finish button
    checkout_overview_page.click_finish()

    # create complete page object
    complete_page = CheckoutCompletePage(login)

    # verify success message
    assert complete_page.get_success_message() == "Thank you for your order!"

    # verify confirmation text exists
    assert complete_page.get_confirmation_text() != ""

    # click back home
    complete_page.click_back_home()

    # verify user returns to inventory page
    assert "inventory" in login.current_url


    ####------------------------------TEST CASE 32-----------------------------------ADDITIONAL

    # test case to verify payment information is displayed in checkout overview page
def test_checkout_payment_information(login):
        # create products page object using driver from login fixture
        products_page = ProductsPage(login)

        # add the first available product to the cart
        products_page.add_first_product_to_cart()

        # click the cart icon to navigate to the cart page
        products_page.open_cart()

        # create cart page object
        cart_page = CartPage(login)

        # click checkout button to go to checkout information page
        cart_page.click_checkout()

        # create checkout page object
        checkout_page = CheckoutPage(login)

        # enter first name into the checkout form
        checkout_page.enter_first_name("Ganan")

        # enter last name into the checkout form
        checkout_page.enter_last_name("Veerendra")

        # enter zip/postal code into the checkout form
        checkout_page.enter_zip_code("560001")

        # click continue button to navigate to checkout overview page
        checkout_page.click_continue()

        # create checkout overview page object
        checkout_overview_page = CheckoutOverviewPage(login)

        # verify that payment information text is displayed
        assert checkout_overview_page.get_payment_info() != ""

####------------------------------TEST CASE 33----------------------------------------ADDITIONAL

    # test case to verify shipping information is displayed
def test_checkout_shipping_information(login):
        # create products page object
        products_page = ProductsPage(login)

        # add first product to cart
        products_page.add_first_product_to_cart()

        # open cart page
        products_page.open_cart()

        # create cart page object
        cart_page = CartPage(login)

        # click checkout button
        cart_page.click_checkout()

        # create checkout information page object
        checkout_page = CheckoutPage(login)

        # enter first name
        checkout_page.enter_first_name("Ganan")

        # enter last name
        checkout_page.enter_last_name("Veerendra")

        # enter zip code
        checkout_page.enter_zip_code("560001")

        # click continue button
        checkout_page.click_continue()

        # create checkout overview page object
        checkout_overview_page = CheckoutOverviewPage(login)

        # verify shipping information text exists
        assert checkout_overview_page.get_shipping_info() != ""

####------------------------------TEST CASE 34-------------------------------------ADDITIONAL

    # test case to verify item total amount is displayed
def test_checkout_item_total(login):
        # create products page object
        products_page = ProductsPage(login)

        # add first product to cart
        products_page.add_first_product_to_cart()

        # open cart page
        products_page.open_cart()

        # create cart page object
        cart_page = CartPage(login)

        # click checkout button
        cart_page.click_checkout()

        # create checkout information page object
        checkout_page = CheckoutPage(login)

        # enter first name
        checkout_page.enter_first_name("Ganan")

        # enter last name
        checkout_page.enter_last_name("Veerendra")

        # enter zip code
        checkout_page.enter_zip_code("560001")

        # click continue button
        checkout_page.click_continue()

        # create checkout overview page object
        checkout_overview_page = CheckoutOverviewPage(login)

        # verify item total value is displayed
        assert checkout_overview_page.get_item_total() != ""


####------------------------------TEST CASE 35----------------------------------------ADDITIONAL

    # test case to verify total calculation exists
def test_checkout_total_calculation(login):
        # create products page object
        products_page = ProductsPage(login)

        # add first product to cart
        products_page.add_first_product_to_cart()

        # open cart page
        products_page.open_cart()

        # create cart page object
        cart_page = CartPage(login)

        # click checkout button
        cart_page.click_checkout()

        # create checkout information page object
        checkout_page = CheckoutPage(login)

        # enter first name
        checkout_page.enter_first_name("Ganan")

        # enter last name
        checkout_page.enter_last_name("Veerendra")

        # enter zip code
        checkout_page.enter_zip_code("560001")

        # click continue button
        checkout_page.click_continue()

        # create checkout overview page object
        checkout_overview_page = CheckoutOverviewPage(login)

        # verify total amount including tax is displayed
        assert checkout_overview_page.get_total() != ""

####------------------------------TEST CASE 36----------------------------------------TEST SUITE

    # test case to verify order confirmation text after successful order
def test_order_confirmation_text(login):
        # create products page object
        products_page = ProductsPage(login)

        # add first product to cart
        products_page.add_first_product_to_cart()

        # open cart page
        products_page.open_cart()

        # create cart page object
        cart_page = CartPage(login)

        # click checkout button
        cart_page.click_checkout()

        # create checkout information page object
        checkout_page = CheckoutPage(login)

        # enter first name
        checkout_page.enter_first_name("Ganan")

        # enter last name
        checkout_page.enter_last_name("Veerendra")

        # enter zip code
        checkout_page.enter_zip_code("560001")

        # click continue button
        checkout_page.click_continue()

        # create checkout overview page object
        checkout_overview_page = CheckoutOverviewPage(login)

        # click finish button to complete order
        checkout_overview_page.click_finish()

        # create checkout complete page object
        complete_page = CheckoutCompletePage(login)

        # verify order confirmation message text
        assert "Thank you for your order" in complete_page.get_success_message()