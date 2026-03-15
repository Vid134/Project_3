# import pytest
import pytest

# import LoginPage
from pages.login_page import LoginPage

# import Excel reader
from utils.data_reader import get_login_data

# read login data from Excel sheet
test_data = get_login_data("test_data_excel\\Book1 (1).xlsx", "Sheet1")


####------------------------------TEST CASE 1-----------------------------------------------TEST SUITE
# pytest decorator used to run the same test multiple times with different data
# Username, Password, Result are column names from Excel
@pytest.mark.parametrize("Username,Password,Result", test_data)
def test_login_with_predefined_users(driver, Username, Password, Result):
    # Test function for login using multiple users from Excel

    # create login page object
    login_page = LoginPage(driver)

    # perform login operation
    login_page.login(Username,Password)

    # Check expected result from Excel
    # If the Excel result column says PASS
    if Result == "PASS":
        assert "inventory" in driver.current_url    # verify user navigated to inventory page
    else:

       assert "inventory" not in driver.current_url  # verify user shouldnt navigate to inventory page as the login fails

####------------------------------TEST CASE 2----------------------------------------------TEST SUITE

def test_login_with_invalid_credentials(driver):
    # Test function for login with invalid credentials

    # create login page object
    login_page = LoginPage(driver)

    # perform login operation
    login_page.login("vid34","113445")

    error_message = login_page.get_error_message()   # Capture the error message displayed on the page

    assert "Epic sadface" in error_message
    # Verify that the error message contains "Epic sadface"
    # SauceDemo shows this message for invalid login