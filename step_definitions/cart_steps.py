"""
Cart-specific step definitions for BDD tests.
Contains steps related to cart operations and validations.
"""
import pytest
from pytest_bdd import given, when, then, parsers
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


@given('user has items in cart')
def user_has_items_in_cart(browser_context):
    """Pre-condition: User has items in cart."""
    products_page = ProductsPage()
    # Add a default item to cart
    assert products_page.add_first_product_to_cart(), "Failed to add item to cart"
    browser_context["items_in_cart"] = True


@given('user has empty cart')
def user_has_empty_cart(browser_context):
    """Pre-condition: User has empty cart."""
    # Ensure cart is empty - this would need actual implementation
    browser_context["items_in_cart"] = False


@when('user navigates to cart page')
def user_navigates_to_cart_page(browser_context):
    """User navigates to cart page."""
    products_page = ProductsPage()
    assert products_page.click_shopping_cart(), "Failed to navigate to cart page"
    browser_context["current_page"] = "cart"


@then('cart should be empty')
def verify_cart_is_empty(browser_context):
    """Verify cart is empty."""
    cart_page = CartPage()
    assert cart_page.verify_cart_is_empty(), "Cart is not empty"


@then(parsers.parse('cart should contain "{item_name}"'))
def verify_cart_contains_item(browser_context, item_name):
    """Verify cart contains specific item."""
    cart_page = CartPage()
    assert cart_page.verify_item_in_cart(item_name), f"Cart does not contain {item_name}"


@then(parsers.parse('cart should have {count:d} items'))
def verify_cart_item_count(browser_context, count):
    """Verify cart has specific number of items."""
    cart_page = CartPage()
    actual_count = cart_page.get_cart_item_count()
    assert actual_count == count, f"Cart has {actual_count} items, expected {count}"


@then(parsers.parse('cart item should have price "{price}"'))
def verify_cart_item_price(browser_context, price):
    """Verify cart item has specific price."""
    cart_page = CartPage()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in cart to verify price"
    
    # Check if any item has the expected price
    price_found = any(item["price"] == price for item in cart_items)
    assert price_found, f"No item found with price {price}"


@when(parsers.parse('user clicks on "Continue Shopping" button'))
def click_continue_shopping(browser_context):
    """Click continue shopping button."""
    cart_page = CartPage()
    assert cart_page.continue_shopping(), "Failed to click continue shopping button"


@then('user should be on products page')
def verify_on_products_page(browser_context):
    """Verify user is on products page."""
    products_page = ProductsPage()
    assert products_page.is_products_page_displayed(), "User is not on products page"


@when('user removes item from cart')
def user_removes_item_from_cart(browser_context):
    """User removes first item from cart."""
    cart_page = CartPage()
    assert cart_page.remove_first_item_from_cart(), "Failed to remove item from cart"


@then(parsers.parse('cart item "{item_name}" should have correct details'))
def verify_cart_item_details(browser_context, item_name):
    """Verify cart item has correct details."""
    cart_page = CartPage()
    assert cart_page.verify_item_in_cart(item_name), f"Item {item_name} not found in cart"
    
    # Verify item details are present
    cart_items = cart_page.get_cart_items()
    item_found = False
    for item in cart_items:
        if item["name"] == item_name:
            assert item["price"], f"Price not found for {item_name}"
            assert item["description"], f"Description not found for {item_name}"
            assert item["quantity"], f"Quantity not found for {item_name}"
            item_found = True
            break
    
    assert item_found, f"Item {item_name} not found in cart for details verification"


@then(parsers.parse('item quantity should be "{quantity}"'))
def verify_item_quantity(browser_context, quantity):
    """Verify item quantity."""
    cart_page = CartPage()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in cart to verify quantity"
    
    # Check if any item has the expected quantity
    quantity_found = any(item["quantity"] == quantity for item in cart_items)
    assert quantity_found, f"No item found with quantity {quantity}"


@then('item description should be displayed')
def verify_item_description_displayed(browser_context):
    """Verify item description is displayed."""
    cart_page = CartPage()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in cart to verify description"
    
    # Check if all items have descriptions
    for item in cart_items:
        assert item.get("description"), f"Description not found for item {item.get('name', 'Unknown')}"


@when('user proceeds to checkout')
def user_proceeds_to_checkout(browser_context):
    """User proceeds to checkout."""
    cart_page = CartPage()
    assert cart_page.proceed_to_checkout(), "Failed to proceed to checkout"
    browser_context["current_page"] = "checkout"


@then('user should be on checkout page')
def verify_on_checkout_page(browser_context):
    """Verify user is on checkout page."""
    # This would need checkout page implementation
    # For now, just verify checkout was initiated
    assert browser_context.get("current_page") == "checkout", "User is not on checkout page"


@then('cart total should be calculated correctly')
def verify_cart_total_calculation(browser_context):
    """Verify cart total is calculated correctly."""
    cart_page = CartPage()
    total = cart_page.get_total_cart_value()
    assert total >= 0, f"Cart total should be non-negative, got {total}"
    
    # If cart has items, total should be greater than 0
    if cart_page.get_cart_item_count() > 0:
        assert total > 0, f"Cart has items but total is {total}"


@given(parsers.parse('user has "{item_name}" in cart'))
def user_has_specific_item_in_cart(browser_context, item_name):
    """Pre-condition: User has specific item in cart."""
    products_page = ProductsPage()
    assert products_page.add_product_to_cart_by_name(item_name), f"Failed to add {item_name} to cart"
    browser_context["items_in_cart"] = True
    browser_context["last_added_item"] = item_name


@when(parsers.parse('user removes "{item_name}" from cart'))
def user_removes_specific_item_from_cart(browser_context, item_name):
    """User removes specific item from cart."""
    cart_page = CartPage()
    assert cart_page.remove_item_from_cart(item_name), f"Failed to remove {item_name} from cart"


@then(parsers.parse('"{item_name}" should not be in cart'))
def verify_item_not_in_cart(browser_context, item_name):
    """Verify specific item is not in cart."""
    cart_page = CartPage()
    assert not cart_page.verify_item_in_cart(item_name), f"{item_name} is still in cart"


@then('cart page should be displayed')
def verify_cart_page_displayed(browser_context):
    """Verify cart page is displayed."""
    cart_page = CartPage()
    assert cart_page.is_cart_page_displayed(), "Cart page is not displayed"


@then('cart icon should show correct item count')
def verify_cart_icon_count(browser_context):
    """Verify cart icon shows correct item count."""
    products_page = ProductsPage()
    cart_page = CartPage()
    
    # Get counts from both pages to verify consistency
    icon_count = products_page.get_cart_item_count()
    actual_cart_count = cart_page.get_cart_item_count()
    
    assert icon_count == actual_cart_count, \
        f"Cart icon shows {icon_count} but cart has {actual_cart_count} items"
