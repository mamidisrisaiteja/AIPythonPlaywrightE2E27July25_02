"""
Authentication-specific step definitions for BDD tests.
Contains steps related to login, logout, and authentication scenarios.
"""
import pytest
from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@given('user is logged in with valid credentials')
def user_logged_in_with_valid_credentials(browser_context):
    """Pre-condition: User is already logged in with valid credentials."""
    login_page = LoginPage()
    
    # Navigate to login page
    assert login_page.navigate_to_login_page(), "Failed to navigate to login page"
    
    # Login with standard user
    assert login_page.login("standard_user", "secret_sauce"), "Failed to login"
    
    # Verify login success
    assert login_page.verify_login_successful(), "Login was not successful"
    
    browser_context["logged_in"] = True
    browser_context["current_user"] = "standard_user"


@given('user is on login page')
def user_is_on_login_page(browser_context):
    """Ensure user is on the login page."""
    login_page = LoginPage()
    assert login_page.navigate_to_login_page(), "Failed to navigate to login page"
    assert login_page.is_login_page_displayed(), "Login page is not displayed"


@when('user enters invalid username')
def user_enters_invalid_username(browser_context):
    """Enter an invalid username."""
    login_page = LoginPage()
    assert login_page.enter_username("invalid_user"), "Failed to enter invalid username"


@when('user enters invalid password')
def user_enters_invalid_password(browser_context):
    """Enter an invalid password."""
    login_page = LoginPage()
    assert login_page.enter_password("invalid_password"), "Failed to enter invalid password"


@when('user enters empty username')
def user_enters_empty_username(browser_context):
    """Enter empty username."""
    login_page = LoginPage()
    assert login_page.enter_username(""), "Failed to enter empty username"


@when('user enters empty password')
def user_enters_empty_password(browser_context):
    """Enter empty password."""
    login_page = LoginPage()
    assert login_page.enter_password(""), "Failed to enter empty password"


@when('user clears username field')
def user_clears_username_field(browser_context):
    """Clear the username field."""
    login_page = LoginPage()
    assert login_page.clear_username(), "Failed to clear username field"


@when('user clears password field')
def user_clears_password_field(browser_context):
    """Clear the password field."""
    login_page = LoginPage()
    assert login_page.clear_password(), "Failed to clear password field"


@then('user should be redirected to products page')
def verify_redirected_to_products_page(browser_context):
    """Verify user is redirected to products page."""
    login_page = LoginPage()
    assert login_page.verify_login_successful(), "User was not redirected to products page"
    
    products_page = ProductsPage()
    assert products_page.is_products_page_displayed(), "Products page is not displayed"


@then('user should remain on login page')
def verify_remains_on_login_page(browser_context):
    """Verify user remains on login page."""
    login_page = LoginPage()
    assert login_page.verify_login_failed(), "User was not kept on login page"
    assert login_page.is_login_page_displayed(), "Login page is not displayed"


@then('login form should be displayed')
def verify_login_form_displayed(browser_context):
    """Verify login form is displayed."""
    login_page = LoginPage()
    assert login_page.is_login_page_displayed(), "Login form is not displayed"


@then('error message should indicate locked user')
def verify_locked_user_error(browser_context):
    """Verify error message indicates user is locked."""
    login_page = LoginPage()
    error_message = login_page.get_error_message()
    assert "locked" in error_message.lower(), f"Error message does not indicate locked user: {error_message}"


@then('error message should indicate invalid credentials')
def verify_invalid_credentials_error(browser_context):
    """Verify error message indicates invalid credentials."""
    login_page = LoginPage()
    error_message = login_page.get_error_message()
    assert "username" in error_message.lower() or "password" in error_message.lower(), \
        f"Error message does not indicate invalid credentials: {error_message}"


@then('error message should indicate required field')
def verify_required_field_error(browser_context):
    """Verify error message indicates required field."""
    login_page = LoginPage()
    error_message = login_page.get_error_message()
    assert "required" in error_message.lower(), f"Error message does not indicate required field: {error_message}"


@when('user logs out')
def user_logs_out(browser_context):
    """User logs out from the application."""
    products_page = ProductsPage()
    assert products_page.logout(), "Failed to logout"
    browser_context["logged_in"] = False
    browser_context["current_user"] = None


@then('user should be redirected to login page after logout')
def verify_redirected_to_login_after_logout(browser_context):
    """Verify user is redirected to login page after logout."""
    login_page = LoginPage()
    assert login_page.is_login_page_displayed(), "User was not redirected to login page after logout"


@given(parsers.parse('user is logged in as "{username}"'))
def user_logged_in_as_specific_user(browser_context, username):
    """Pre-condition: User is logged in as a specific user."""
    login_page = LoginPage()
    
    # Navigate to login page
    assert login_page.navigate_to_login_page(), "Failed to navigate to login page"
    
    # Login with specified user
    password = "secret_sauce"  # Assuming same password for all test users
    assert login_page.login(username, password), f"Failed to login as {username}"
    
    # Verify login success
    if username != "locked_out_user":  # locked_out_user should not be able to login
        assert login_page.verify_login_successful(), f"Login was not successful for {username}"
        browser_context["logged_in"] = True
    else:
        assert login_page.verify_login_failed(), f"Locked out user {username} should not be able to login"
        browser_context["logged_in"] = False
    
    browser_context["current_user"] = username


@then('login should be successful')
def verify_login_successful(browser_context):
    """Verify that login was successful."""
    login_page = LoginPage()
    assert login_page.verify_login_successful(), "Login was not successful"
    browser_context["logged_in"] = True


@then('login should fail')
def verify_login_failed(browser_context):
    """Verify that login failed."""
    login_page = LoginPage()
    assert login_page.verify_login_failed(), "Login did not fail as expected"
    browser_context["logged_in"] = False


@when('user attempts to access products page directly')
def user_attempts_direct_access_to_products(browser_context):
    """User attempts to access products page without logging in."""
    products_page = ProductsPage()
    # This would need actual navigation to products URL
    # For now, just verify we're not logged in
    assert not browser_context.get("logged_in", False), "User should not be logged in"
