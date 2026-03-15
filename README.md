SauceDemo Web Application Automation Framework
Project Title

Automation Testing Framework for SauceDemo E-Commerce Web Application

Project Description

This project implements an automated testing framework for the SauceDemo web application using Python, Selenium WebDriver, PyTest, and the Page Object Model (POM) design pattern.

The framework validates core functionalities of the application including login authentication, product listing, cart operations, checkout workflow, sorting functionality, and reset application state.

The framework is structured using Page Object Model architecture, which improves code maintainability, readability, and scalability.

Website Link

Application under test:

https://www.saucedemo.com/

Test Objective

The objective of this automation framework is to:

Validate core functionalities of the SauceDemo application

Ensure login authentication works correctly

Verify product listing and product details

Validate cart operations

Validate checkout workflow

Verify sorting functionality

Validate reset application state

Create a maintainable and scalable automation framework

Preconditions

Before executing the automation test suite, ensure the following:

Python is installed on the system

Selenium WebDriver is installed

PyTest testing framework is installed

Chrome browser is installed

ChromeDriver is configured

Required Python packages are installed

Test Environment
Parameter	Value
Operating System	Windows
Programming Language	Python
Automation Tool	Selenium WebDriver
Testing Framework	PyTest
Browser	Google Chrome
IDE	PyCharm
Technologies Used

Python

Selenium WebDriver

PyTest

Page Object Model (POM)

Excel Data-Driven Testing

Explicit Waits (WebDriverWait)

Table of Contents

Project Structure

Detailed Project Architecture

Project Features

Project Usage

UI Under Test

Test Design Techniques

Test Cases Covered in Project

Advantages of this Framework

CI/CD Integration

Future Enhancements

Project Structure
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
Detailed Project Architecture

The automation framework follows the Page Object Model (POM) design pattern.

Page Layer

Contains page classes that store:

Web element locators

Page interaction methods

UI actions

Examples:

LoginPage

ProductsPage

CartPage

CheckoutPage

Test Layer

Contains PyTest test scripts that validate application functionality.

Examples:

Login validation

Product listing validation

Cart validation

Checkout validation

Sorting validation

Utility Layer

Reusable helper modules used across the framework.

Examples:

Driver Factory

Wait Utilities

Screenshot Helper

Config Reader

Excel Data Reader

Project Features

Page Object Model architecture

Modular test design

Reusable utility modules

Explicit waits implementation

Screenshot capture capability

Data-driven testing using Excel

PyTest based test execution

Clean and maintainable project structure

Project Usage

To execute the test suite run:

pytest -v

To execute a specific test file:

pytest tests/test_login_page.py
UI Under Test

The application under test is SauceDemo, a demo e-commerce web application that provides the following features:

User login authentication

Product browsing

Cart management

Checkout process

Sorting functionality

Reset application state

Test Design Techniques

The following testing techniques were applied:

Functional Testing

Positive Testing

Negative Testing

Data Driven Testing

UI Validation Testing

Test Cases Covered in Project

The automation framework covers the following scenarios:

Login with predefined users

Login with invalid credentials

Validate logout functionality

Verify cart icon visibility

Random product selection and data extraction

Add selected products to cart and validate

Validate product details inside cart

Complete checkout and validate order confirmation

Validate product sorting functionality

Validate Reset App State functionality

Advantages of this Framework

Modular and maintainable architecture

High reusability of page objects

Easy scalability for new test cases

Clean code structure

Supports data-driven testing

Faster execution of repetitive tests

CI/CD Integration

This automation framework can be integrated with CI/CD tools such as:

Jenkins

GitHub Actions

GitLab CI

Automation pipelines can execute the test suite automatically during build and deployment stages.

Future Enhancements

Possible improvements for the framework include:

Parallel test execution

Integration with reporting tools (Allure / HTML reports)

CI/CD pipeline integration

Docker-based execution

Cross-browser testing

Cloud testing integration (BrowserStack / Sauce Lab
