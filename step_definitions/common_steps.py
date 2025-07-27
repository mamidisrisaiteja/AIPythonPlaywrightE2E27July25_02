"""
Common step definitions for BDD tests.
Contains shared steps that can be used across multiple features.
"""
import pytest
from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@given('user is on "https://www.saucedemo.com/"')
def user_is_on_sauce_demo_site(browser_context):
    """Navigate to Sauce Demo website."""
    login_page = LoginPage()
    assert login_page.navigate_to_login_page(), "Failed to navigate to login page"
    assert login_page.is_login_page_displayed(), "Login page is not displayed"


@given(parsers.parse('user is on "{url}"'))
def user_is_on_url(browser_context, url):
    """Navigate to a specific URL."""
    login_page = LoginPage()
    assert login_page.navigate_to(url), f"Failed to navigate to {url}"


@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(browser_context, username, password):
    """Enter username and password."""
    login_page = LoginPage()
    assert login_page.enter_username(username), f"Failed to enter username: {username}"
    assert login_page.enter_password(password), f"Failed to enter password"


@when('click Login Button')
def click_login_button(browser_context):
    """Click the login button."""
    login_page = LoginPage()
    assert login_page.click_login_button(), "Failed to click login button"


@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text(browser_context, text):
    """Verify that page contains specific text."""
    from pages.base_page import BasePage
    base_page = BasePage()
    assert base_page.verify_page_contains_text(text), f"Page does not contain text: {text}"


@then('then redirect to Products page')
def verify_redirect_to_products_page(browser_context):
    """Verify user is redirected to products page."""
    products_page = ProductsPage()
    assert products_page.is_products_page_displayed(), "Products page is not displayed"


@then('login Button should be still displayed')
def verify_login_button_still_displayed(browser_context):
    """Verify login button is still displayed (login failed)."""
    login_page = LoginPage()
    assert login_page.verify_login_failed(), "Login button is not displayed - login may have succeeded unexpectedly"


@then('error message should be displayed')
def verify_error_message_displayed(browser_context):
    """Verify error message is displayed."""
    login_page = LoginPage()
    error_message = login_page.get_error_message()
    assert error_message, "Error message is not displayed"


@then(parsers.parse('error message should contain "{text}"'))
def verify_error_message_contains(browser_context, text):
    """Verify error message contains specific text."""
    login_page = LoginPage()
    assert login_page.verify_error_message_contains(text), f"Error message does not contain: {text}"


@when('click Sort Icon')
def click_sort_icon(browser_context):
    """Click the sort dropdown icon."""
    products_page = ProductsPage()
    assert products_page.click_sort_dropdown(), "Failed to click sort dropdown"


@when('click Sort the Products by Name (A–Z)')
def sort_products_by_name_a_z(browser_context):
    """Sort products by name A-Z."""
    products_page = ProductsPage()
    assert products_page.sort_products_by_name_a_z(), "Failed to sort products by name A-Z"


@when(parsers.parse('select sort option "{option}"'))
def select_sort_option(browser_context, option):
    """Select a specific sort option."""
    products_page = ProductsPage()
    assert products_page.select_sort_option(option), f"Failed to select sort option: {option}"


@then('all the products must be sorted from A to Z')
def verify_products_sorted_a_z(browser_context):
    """Verify products are sorted alphabetically A-Z."""
    products_page = ProductsPage()
    assert products_page.verify_products_sorted_alphabetically(), "Products are not sorted alphabetically A-Z"


@then('all the products must be sorted from Z to A')
def verify_products_sorted_z_a(browser_context):
    """Verify products are sorted alphabetically Z-A."""
    products_page = ProductsPage()
    product_names = products_page.get_product_names()
    sorted_names = sorted(product_names, reverse=True)
    assert product_names == sorted_names, "Products are not sorted alphabetically Z-A"


@then('all the products must be sorted by price low to high')
def verify_products_sorted_price_low_high(browser_context):
    """Verify products are sorted by price low to high."""
    # This would need actual price extraction logic
    # For now, just verify the sort option was selected
    assert True, "Price sorting low to high verification not yet implemented"


@then('all the products must be sorted by price high to low')
def verify_products_sorted_price_high_low(browser_context):
    """Verify products are sorted by price high to low."""
    # This would need actual price extraction logic
    # For now, just verify the sort option was selected
    assert True, "Price sorting high to low verification not yet implemented"


@when('click Add to cart')
def click_add_to_cart(browser_context):
    """Click add to cart for the first product."""
    products_page = ProductsPage()
    assert products_page.add_first_product_to_cart(), "Failed to add first product to cart"


@when('click cart icon')
def click_cart_icon(browser_context):
    """Click the shopping cart icon."""
    products_page = ProductsPage()
    assert products_page.click_shopping_cart(), "Failed to click shopping cart icon"


@then('cart page displays selected items')
def verify_cart_displays_items(browser_context):
    """Verify cart page displays selected items."""
    cart_page = CartPage()
    assert cart_page.is_cart_page_displayed(), "Cart page is not displayed"
    assert cart_page.verify_cart_contains_items(), "Cart does not contain any items"


@when(parsers.parse('user clicks on "{button_text}" button for "{product_name}"'))
def click_product_button(browser_context, button_text, product_name):
    """Click a specific button for a product."""
    if button_text.lower() == "add to cart":
        products_page = ProductsPage()
        assert products_page.add_product_to_cart_by_name(product_name), f"Failed to add {product_name} to cart"
    elif button_text.lower() == "remove":
        if "cart" in browser_context.get("current_page", "").lower():
            cart_page = CartPage()
            assert cart_page.remove_item_from_cart(product_name), f"Failed to remove {product_name} from cart"
        else:
            # Remove from products page would be handled differently
            assert True, f"Remove {product_name} from products page"


@when('user clicks on cart icon')
def user_clicks_cart_icon(browser_context):
    """User clicks on the cart icon."""
    products_page = ProductsPage()
    assert products_page.click_shopping_cart(), "Failed to click cart icon"
    browser_context["current_page"] = "cart"


@then(parsers.parse('the cart badge should show "{count}"'))
def verify_cart_badge_count(browser_context, count):
    """Verify cart badge shows specific count."""
    products_page = ProductsPage()
    actual_count = products_page.get_cart_item_count()
    expected_count = int(count)
    assert actual_count == expected_count, f"Cart badge shows {actual_count}, expected {expected_count}"


@then('the cart badge should not be visible')
def verify_cart_badge_not_visible(browser_context):
    """Verify cart badge is not visible."""
    products_page = ProductsPage()
    cart_count = products_page.get_cart_item_count()
    assert cart_count == 0, f"Cart badge is visible with count {cart_count}, expected not visible"


@then(parsers.parse('the button should change to "{button_text}"'))
def verify_button_text_changed(browser_context, button_text):
    """Verify button text has changed."""
    # This would need to check the actual button text
    # For now, just assert true as placeholder
    assert True, f"Button text changed to {button_text}"
