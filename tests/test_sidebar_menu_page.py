# import ProductsPage to interact with products page
from pages.products_page import ProductsPage

# import SidebarMenuPage to interact with sidebar menu
from pages.sidebar_menu_page import SidebarMenuPage

####------------------------------TEST CASE 19---------------------------------------------ADDITIONAL

# test case to verify sidebar menu opens
def test_sidebar_menu_open(login):

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # verify sidebar menu is visible
    assert sidebar_menu_page.is_sidebar_visible() == True

####------------------------------TEST CASE 20-----------------------------------------ADDITIONAL

# test case to verify sidebar menu closes
def test_sidebar_menu_close(login):

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # close sidebar menu
    sidebar_menu_page.close_menu()

    # verify sidebar menu is not visible
    assert "inventory" in login.current_url

####------------------------------TEST CASE 21----------------------------------------ADDITIONAL

# test case to verify All Items navigation
def test_sidebar_all_items_navigation(login):

    # create products page object
    products_page = ProductsPage(login)

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # click All Items option
    sidebar_menu_page.click_all_items()

    # verify navigation to inventory page
    assert "inventory" in login.current_url

####------------------------------TEST CASE 22-------------------------------------------ADDITIONAL

# test case to verify About navigation
def test_sidebar_about_navigation(login):

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # click About option
    sidebar_menu_page.click_about()

    # verify navigation to SauceLabs website
    assert "saucelabs" in login.current_url

####------------------------------TEST CASE 23--------------------------------------------------TEST SUITE

# test case to verify Logout functionality
def test_sidebar_logout(login):

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # click Logout option
    sidebar_menu_page.click_logout()

    # verify user redirected to login page
    assert "saucedemo" in login.current_url


####------------------------------TEST CASE 24-------------------------------------------------TEST SUITE

# test case to verify Reset App State functionality
def test_sidebar_reset_app_state(login):

    # create products page object
    products_page = ProductsPage(login)

    # create sidebar page object
    sidebar_menu_page = SidebarMenuPage(login)

    # add product to cart
    products_page.add_first_product_to_cart()

    # open sidebar menu
    sidebar_menu_page.open_menu()

    # click Reset App State
    sidebar_menu_page.click_reset_app_state()

    # verify cart badge disappears by checking cart count
    assert products_page.get_cart_badge_count1() == 0