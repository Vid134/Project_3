# Import CartPage class from cart_page module inside pages folder
from pages.cart_page import CartPage

# Import ProductsPage class from products_page module inside pages folder
from pages.products_page import ProductsPage

# Import time module to use sleep function
import time

####------------------------------TEST CASE 3---------------------------------------ADDITIONAL

# Test case to verify the products page is displayed after login
def test_product_page_displayed(login):

    # create products page object
    products_page = ProductsPage(login)

    # verify product list exists
    assert products_page.is_product_list_displayed()

####------------------------------TEST CASE 4-------------------------------------------ADDITIONAL

# Test case to verify number of products displayed
def test_product_count(login):

    # create products page object
    products_page = ProductsPage(login)

    # Get list of product names displayed on the page
    product_names = products_page.get_product_names()

    # Verify the number of products is 6
    assert len(product_names) == 6

####------------------------------TEST CASE 5-----------------------------------ADDITIONAL

# Test case to verify product details such as name, price, image and add to cart button
def test_product_details_displayed(login):

    # create products page object
    products_page = ProductsPage(login)

    # Get list of product names
    product_names = products_page.get_product_names()

    # Get list of product prices
    product_price = products_page.get_product_prices()

    # Get list of product images
    product_images = products_page.get_product_images()

    # Get list of add-to-cart buttons for products
    product_add_to_cart_options = products_page.get_product_add_to_cart_options()

    print("Products displayed:", product_names )   # Print product names in console
    print("Products price:", product_price)  # Print product prices in console
    print("Products images:", product_images)   # Print product images in console
    print("Products cart options:", product_add_to_cart_options) # Print add to cart buttons list

    # verify product details are visible
    assert products_page.verify_product_details()

####------------------------------TEST CASE 6---------------------------------------------TEST SUITE

# Test case to verify cart icon is visible on products page
def test_cart_icon_visibility(login):

    # create products page object
    products_page = ProductsPage(login)

    # Verify cart icon is displayed
    assert products_page.is_cart_icon_visible()

####------------------------------TEST CASE 7----------------------------------------------TEST SUITE

# Test case to verify cart badge increases after adding product
def test_cart_badge_increment(login):

    # create products page object
    products_page = ProductsPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # verify badge value
    assert products_page.get_cart_badge_count() == 1

####------------------------------TEST CASE 8--------------------------------------------TEST SUITE - 5,6,7

# Test case to verify adding random products to cart
def test_random_product_selection(login, cart_names=None, item=None):

    # create products page object
    products_page = ProductsPage(login)

    # select 4 random products
    selected_products = products_page.add_random_products(4)

    # print("Selected product prices:", selected-products)
    print("Selected products:",selected_products)

    # verify that exactly 4 random products were selected
    assert len(selected_products) == 4

    #  Navigate to the cart pag
    products_page.open_cart()

    # Create Cart Page object
    cart_page = CartPage(login)

    # Fetch all products currently present in the cart
    cart_items = cart_page.get_cart_items()

    # Validate that the number of items in the cart is equal to the selected products
    assert len(cart_items) == 4

 # Extract product names from the randomly selected products list
    selected_names = [item[0] for item in selected_products]

    # Fetch the product names that are displayed in the cart page
    cart_names = cart_page.get_cart_item_names()

    print("Selected names:", selected_names)  # Print selected product names for logging
    print("Cart names:", cart_names)  # Print cart product names for verification

    # Validate that the selected products and cart products are the same
    assert set(selected_names) == set(cart_names)

    # extract the prices of the randomly selected products
    selected_prices = [float(item[1].replace("$", " "))for item in selected_products]

    # fetch the prices of the products displayed in the cart
    cart_prices = cart_page.get_cart_item_prices()

    print("Selected price", selected_prices)  # Print selected product names for logging
    print("Cart price:", cart_prices)  # print cart price for loggi ng

    # validate that the prices of the selected products match the prices in the cart
    assert set(selected_prices) == set(cart_prices)


####------------------------------TEST CASE 9-----------------------------------------ADDITIONAL-----

# Test case to verify sorting by product name (A to Z)
def test_sort_name_a_to_z(login):

    # create products page object
    products_page = ProductsPage(login)

    # Wait for page elements to load (temporary wait)
    time.sleep(10)

    # apply sorting
    products_page.sort_products("Name (A to Z)")

    # Get product names after sorting
    product_names = products_page.get_product_names()

    print("Actual order:", product_names)  # Print actual order of products from UI
    print("Expected order:", sorted(product_names))  # Print expected sorted order

    # test passes if action executes
    assert product_names == sorted(product_names)

####------------------------------TEST CASE 10-------------------------------------------TEST SUITE

# Test case to verify sorting by product name (Z to A)
def test_sort_name_z_to_a(login):

    # create products page object
    products_page = ProductsPage(login)

    # apply sorting
    products_page.sort_products("Name (Z to A)")

    time.sleep(10) # Wait for page elements to load (temporary wait)

    product_names = products_page.get_product_names()
    # Get product names after sorting

    print("Actual order:", product_names)  # Print actual order of products from UI
    print("Expected order:", sorted(product_names,reverse=True))   # Print expected sorted order

    # test passes if action executes
    assert product_names == sorted(product_names,reverse=True)

####------------------------------TEST CASE 11-----------------------------------------TEST SUITE

# Test case to verify sorting by price (low to high)
def test_sort_price_low_to_high(login):

    # create products page object
    products_page = ProductsPage(login)

    # apply sorting
    products_page.sort_products("Price (low to high)")

    # apply sorting
    prices = products_page.get_product_prices()

    print("Actual order:",prices)   # Print actual order of prices from UI
    print("Expected order:", sorted(prices))
    # Print expected sorted prices

    assert prices == sorted(prices)
# Verify prices are sorted from low to high

####------------------------------TEST CASE 12----------------------------------------ADDITIONAL

# Test case to verify sorting by price (high to low)
def test_sort_price_high_to_low(login):


    # Create products page object
    products_page = ProductsPage(login)

    # Apply sorting option "Price (high to low)"
    products_page.sort_products("Price (high to low)")

    # Get list of product prices
    prices = products_page.get_product_prices()

    print("Actual order:",prices)  # Print actual order from UI
    print("Expected order:", sorted(prices,reverse= True))
    # Print expected descending price order

    assert prices == sorted(prices,reverse= True)
    # Verify prices are sorted from high to low

