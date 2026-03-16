# SauceDemo Automation Testing Framework

Automation testing framework developed using **Python, Selenium, PyTest, and Page Object Model (POM)** to test the functionality of the SauceDemo e-commerce web application.

---

# Project Description

This project automates end-to-end testing of the SauceDemo web application including login, product validation, cart functionality, checkout process, sorting features, and reset functionality.

The framework follows **Page Object Model architecture** for better maintainability, readability, and scalability.

---

# Website Under Test

https://www.saucedemo.com/

---

# Test Objective

The objective of this automation framework is to validate:

- Login functionality
- Product listing and details
- Add products to cart
- Cart validation
- Checkout process
- Order confirmation
- Product sorting
- Reset application state

---

# Preconditions

Before executing the test suite:

- Python should be installed
- Chrome browser installed
- Internet connection available
- Required dependencies installed

---

# Test Environment

| Parameter | Value |
|----------|------|
| OS | Windows |
| Language | Python |
| Automation Tool | Selenium |
| Framework | PyTest |
| Browser | Chrome |
| IDE | PyCharm |

---

# Technologies Used

| Tool | Purpose |
|-----|--------|
| Python | Programming language |
| Selenium | Browser automation |
| PyTest | Test execution framework |
| POM | Framework design pattern |
| WebDriver Manager | Driver management |
| GitHub | Version control |
| Jenkins | CI/CD automation |

---

# Table of Contents

1. [Project Structure](#project-structure)
2. [Detailed Project Architecture](#detailed-project-architecture)
3. [Project Features](#project-features)
4. [Project Usage](#project-usage)
5. [UI Under Test](#ui-under-test)
6. [Test Design Techniques](#test-design-techniques)
7. [Test Cases Covered In Project](#test-cases-covered-in-project)
8. [Advantages Of This Framework](#advantages-of-this-framework)
9. [CI/CD Integration](#cicd-integration)
10. [Future Enhancements](#future-enhancements)

---

# Project Structure
Project_3
│
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests
│   ├── test_login_page.py
│   ├── test_products_page.py
│   ├── test_cart_page.py
│   ├── test_checkout_page.py
│   └── test_sidebar_menu_page.py
│
├── utils
│   ├── driver_factory.py
│   ├── wait_utils.py
│   ├── step_decorator.py
│   ├── screenshot_helper.py
│   ├── config_reader.py
│   └── data_reader.py
│
├── test_data_excel
│   └── login_test_data.xlsx
│
├── config.ini
├── conftest.py
└── README.md

---

# Detailed Project Architecture

The framework follows the **Page Object Model (POM)** design pattern.

### Pages Layer
Contains page classes representing each webpage.

### Tests Layer
Contains PyTest test scripts that execute test scenarios.

### Utils Layer
Reusable helper utilities such as:

- Driver initialization
- Explicit waits
- Screenshot capture
- Test data reader

### Test Data Layer
Stores external test data in Excel.

---

# Project Features

- Page Object Model framework
- Data-driven testing
- Modular reusable functions
- Screenshot capture on important steps
- Sorting validation
- Cart validation
- Checkout validation
- Scalable automation structure

---

# Project Usage

Install dependencies:
pip install -r requirements.txt


Run all tests:


pytest -v


Generate HTML report:


pytest --html=report.html


Generate Allure report:


pytest --alluredir=allure-results
allure serve allure-results


---

# UI Under Test

The application under test is **SauceDemo E-commerce Website**.

Major modules tested:

- Login page
- Products page
- Cart page
- Checkout page
- Checkout overview page
- Order confirmation page

---

# Test Design Techniques

The following testing techniques were used:

- Functional Testing
- UI Validation
- Data Driven Testing
- End-to-End Testing
- Positive and Negative Testing

---

# Test Cases Covered In Project

## Test Cases Covered In Project

1. Verify successful login with valid credentials
2. Verify login with invalid credentials
3. Verify locked-out user cannot login

4. Verify product list is displayed on the products page
5. Verify product names are displayed correctly
6. Verify product prices are displayed correctly
7. Verify product images are displayed
8. Verify "Add to Cart" button is present for products
9. Verify adding a single product to the cart
10. Verify cart badge increments after adding a product
11. Verify adding multiple products to the cart
12. Verify removing a product from the products page

13. Verify cart icon navigation to cart page
14. Verify products added are displayed in the cart
15. Verify cart item names match selected products
16. Verify cart item prices match selected products
17. Verify cart badge count matches number of products
18. Verify removing a product from the cart page
19. Verify continue shopping button navigation
20. Verify cart retains products after navigation

21. Verify checkout button navigates to checkout information page
22. Verify continue button functionality on checkout information page
23. Verify cancel button navigates back to previous page
24. Verify checkout validation when first name is empty
25. Verify checkout validation when last name is empty
26. Verify checkout validation when postal code is empty
27. Verify checkout validation when all fields are empty
28. Verify successful navigation to checkout overview page

29. Verify order summary displays correct product names
30. Verify order summary displays correct product prices
31. Verify tax and total price calculation
32. Verify finishing checkout successfully
33. Verify order confirmation message after checkout
34. Verify screenshot capture of order summary

35. Verify product sorting functionality (Name A to Z, Z to A, Price Low to High, High to Low)

36. Verify "Reset App State" clears cart items and resets application state

---

# Advantages Of This Framework

- Highly maintainable
- Scalable architecture
- Reusable components
- Easy debugging
- Supports CI/CD integration

---

# CI/CD Integration

This project is integrated with **Jenkins** for continuous testing.

Pipeline flow:
GitHub → Jenkins → Test Execution → Report Generation


Benefits:

- Automated test execution
- Continuous integration
- Faster feedback

---

# Future Enhancements

Possible improvements for this framework:

- Parallel test execution
- Docker integration
- Cross-browser testing
- Cloud execution (BrowserStack / SauceLabs)
- Slack test notifications

---

# Author

Automation Framework Developed by **Vidhyashree.V**