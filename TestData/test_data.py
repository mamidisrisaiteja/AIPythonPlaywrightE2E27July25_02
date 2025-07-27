"""
Test data constants and configurations for the Sauce Demo application.
Contains test data organized by modules for easy maintenance.
"""

# Application URLs
BASE_URL = "https://www.saucedemo.com/"
LOGIN_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"

# Test Users
TEST_USERS = {
    "standard_user": {
        "username": "standard_user",
        "password": "secret_sauce",
        "expected_result": "success"
    },
    "locked_out_user": {
        "username": "locked_out_user", 
        "password": "secret_sauce",
        "expected_result": "locked"
    },
    "problem_user": {
        "username": "problem_user",
        "password": "secret_sauce", 
        "expected_result": "success"
    },
    "performance_glitch_user": {
        "username": "performance_glitch_user",
        "password": "secret_sauce",
        "expected_result": "success"
    },
    "invalid_user": {
        "username": "standard_use",  # Intentionally wrong
        "password": "secret_sauce",
        "expected_result": "failed"
    },
    "empty_username": {
        "username": "",
        "password": "secret_sauce", 
        "expected_result": "failed"
    },
    "empty_password": {
        "username": "standard_user",
        "password": "",
        "expected_result": "failed"
    }
}

# Product Information
PRODUCTS = {
    "sauce_labs_backpack": {
        "name": "Sauce Labs Backpack",
        "price": "$29.99",
        "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        "add_to_cart_id": "add-to-cart-sauce-labs-backpack",
        "remove_id": "remove-sauce-labs-backpack"
    },
    "sauce_labs_bike_light": {
        "name": "Sauce Labs Bike Light",
        "price": "$9.99", 
        "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night.",
        "add_to_cart_id": "add-to-cart-sauce-labs-bike-light",
        "remove_id": "remove-sauce-labs-bike-light"
    },
    "sauce_labs_bolt_tshirt": {
        "name": "Sauce Labs Bolt T-Shirt",
        "price": "$15.99",
        "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt.",
        "add_to_cart_id": "add-to-cart-sauce-labs-bolt-t-shirt", 
        "remove_id": "remove-sauce-labs-bolt-t-shirt"
    },
    "sauce_labs_fleece_jacket": {
        "name": "Sauce Labs Fleece Jacket",
        "price": "$49.99",
        "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        "add_to_cart_id": "add-to-cart-sauce-labs-fleece-jacket",
        "remove_id": "remove-sauce-labs-fleece-jacket"
    },
    "sauce_labs_onesie": {
        "name": "Sauce Labs Onesie", 
        "price": "$7.99",
        "description": "Rib snap infant onesie for the junior automation engineer in development.",
        "add_to_cart_id": "add-to-cart-sauce-labs-onesie",
        "remove_id": "remove-sauce-labs-onesie"
    },
    "test_all_things_tshirt": {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "price": "$15.99",
        "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests.",
        "add_to_cart_id": "add-to-cart-test.allthethings()-t-shirt-(red)",
        "remove_id": "remove-test.allthethings()-t-shirt-(red)"
    }
}

# Sort Options
SORT_OPTIONS = {
    "name_a_z": {
        "value": "az",
        "display": "Name (A to Z)"
    },
    "name_z_a": {
        "value": "za", 
        "display": "Name (Z to A)"
    },
    "price_low_high": {
        "value": "lohi",
        "display": "Price (low to high)"
    },
    "price_high_low": {
        "value": "hilo",
        "display": "Price (high to low)"
    }
}

# Expected Text Messages
EXPECTED_TEXTS = {
    "login_logo": "Swag Labs",
    "products_title": "Products", 
    "add_to_cart": "Add to cart",
    "remove": "Remove",
    "your_cart": "Your Cart",
    "continue_shopping": "Continue Shopping",
    "checkout": "Checkout",
    "error_locked_user": "Epic sadface: Sorry, this user has been locked out.",
    "error_invalid_credentials": "Epic sadface: Username and password do not match any user in this service",
    "error_username_required": "Epic sadface: Username is required",
    "error_password_required": "Epic sadface: Password is required"
}

# Test Case Mappings
TEST_CASES = {
    "TC_AUTH_01": {
        "test_id": "TC_AUTH_01",
        "module": "Authentication Module",
        "description": "Login with Valid credentials",
        "user": "standard_user",
        "expected_result": "Then Redirect to Products page"
    },
    "TC_AUTH_01b": {
        "test_id": "TC_AUTH_01b",
        "module": "Authentication Module", 
        "description": "Login with invalid credentials",
        "user": "invalid_user",
        "expected_result": "Login Button should be still displayed"
    },
    "TC_INV_01": {
        "test_id": "TC_INV_01",
        "module": "Inventory Module",
        "description": "Verify product listing",
        "user": "standard_user",
        "expected_result": 'verify Products page has text "Products" and "Add to cart"'
    },
    "TC_INV_02": {
        "test_id": "TC_INV_02", 
        "module": "Inventory Module",
        "description": "Sort products by Name (A–Z)",
        "user": "standard_user",
        "expected_result": "All the products must be sorted from A to Z"
    },
    "TC_CART_01": {
        "test_id": "TC_CART_01",
        "module": "Cart Module",
        "description": "View cart contents", 
        "user": "standard_user",
        "expected_result": "Cart page displays selected items"
    }
}

# Browser Configuration
BROWSER_CONFIG = {
    "default_timeout": 30000,  # 30 seconds
    "page_load_timeout": 60000,  # 60 seconds
    "element_timeout": 10000,   # 10 seconds
    "viewport": {
        "width": 1280,
        "height": 720
    },
    "slow_mo": 100,  # milliseconds
    "headless": False
}

# Retry Configuration  
RETRY_CONFIG = {
    "max_retries": 3,
    "retry_delay": 1,  # seconds
    "retry_on_timeout": True,
    "retry_on_network_error": True
}

# Report Configuration
REPORT_CONFIG = {
    "screenshots_on_failure": True,
    "video_on_failure": True, 
    "trace_on_failure": True,
    "html_report": True,
    "junit_xml": True,
    "allure_report": True
}
