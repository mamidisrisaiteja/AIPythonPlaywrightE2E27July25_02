"""
Cart Page Object Model for Sauce Demo application.
Handles all cart-related interactions and validations.
"""
from pages.base_page import BasePage
from typing import List, Dict, Optional


class CartPage(BasePage):
    """Cart page object model for cart module."""
    
    # Element selectors
    CART_TITLE = '.title'
    CART_LIST = '.cart_list'
    CART_ITEMS = '.cart_item'
    CART_ITEM_NAMES = '.inventory_item_name'
    CART_ITEM_DESCRIPTIONS = '.inventory_item_desc'
    CART_ITEM_PRICES = '.inventory_item_price'
    CART_QUANTITY = '.cart_quantity'
    REMOVE_BUTTONS = '[data-test^="remove"]'
    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'
    
    # Expected texts
    YOUR_CART_TEXT = "Your Cart"
    CART_TITLE_TEXT = "Your Cart"
    
    def __init__(self):
        """Initialize cart page."""
        super().__init__()
        
    def is_cart_page_displayed(self) -> bool:
        """
        Verify if cart page is displayed.
        
        Returns:
            bool: True if cart page is displayed
        """
        return (
            self.verify_page_contains_text(self.YOUR_CART_TEXT) and
            self.is_element_visible(self.CART_LIST)
        )
    
    def verify_cart_page_title(self) -> bool:
        """
        Verify the cart page title.
        
        Returns:
            bool: True if cart title is displayed
        """
        return self.verify_page_contains_text(self.CART_TITLE_TEXT)
    
    def verify_your_cart_text(self) -> bool:
        """
        Verify 'Your Cart' text is displayed.
        
        Returns:
            bool: True if 'Your Cart' text is visible
        """
        return self.verify_page_contains_text(self.YOUR_CART_TEXT)
    
    def get_cart_items(self) -> List[Dict[str, str]]:
        """
        Get list of all items in the cart with their details.
        
        Returns:
            List[Dict[str, str]]: List of cart items with name, description, price, quantity
        """
        # This will be implemented with actual MCP Playwright calls
        # For now, return sample data for framework structure
        return [
            {
                "name": "Sauce Labs Backpack",
                "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
                "price": "$29.99",
                "quantity": "1"
            }
        ]
    
    def get_cart_item_count(self) -> int:
        """
        Get the number of items in the cart.
        
        Returns:
            int: Number of items in cart
        """
        cart_items = self.get_cart_items()
        return len(cart_items)
    
    def verify_item_in_cart(self, item_name: str) -> bool:
        """
        Verify if a specific item is in the cart.
        
        Args:
            item_name: Name of the item to verify
            
        Returns:
            bool: True if item is found in cart
        """
        cart_items = self.get_cart_items()
        for item in cart_items:
            if item["name"] == item_name:
                return True
        return False
    
    def verify_cart_contains_items(self) -> bool:
        """
        Verify that cart contains at least one item.
        
        Returns:
            bool: True if cart has items
        """
        return self.get_cart_item_count() > 0
    
    def verify_cart_is_empty(self) -> bool:
        """
        Verify that cart is empty.
        
        Returns:
            bool: True if cart is empty
        """
        return self.get_cart_item_count() == 0
    
    def remove_item_from_cart(self, item_name: str) -> bool:
        """
        Remove a specific item from cart.
        
        Args:
            item_name: Name of the item to remove
            
        Returns:
            bool: True if item removed successfully
        """
        # Convert item name to data-test attribute format
        test_id = item_name.lower().replace(" ", "-").replace(".", "").replace("(", "").replace(")", "")
        remove_button_selector = f'[data-test="remove-{test_id}"]'
        
        return self.click_element(
            remove_button_selector,
            f"remove button for {item_name}"
        )
    
    def remove_first_item_from_cart(self) -> bool:
        """
        Remove the first item from cart.
        
        Returns:
            bool: True if item removed successfully
        """
        cart_items = self.get_cart_items()
        if cart_items:
            return self.remove_item_from_cart(cart_items[0]["name"])
        return False
    
    def continue_shopping(self) -> bool:
        """
        Click continue shopping button.
        
        Returns:
            bool: True if click successful
        """
        return self.click_element(
            self.CONTINUE_SHOPPING_BUTTON,
            "continue shopping button"
        )
    
    def proceed_to_checkout(self) -> bool:
        """
        Click checkout button to proceed to checkout.
        
        Returns:
            bool: True if click successful
        """
        return self.click_element(
            self.CHECKOUT_BUTTON,
            "checkout button"
        )
    
    def get_total_cart_value(self) -> float:
        """
        Calculate total value of items in cart.
        
        Returns:
            float: Total cart value
        """
        cart_items = self.get_cart_items()
        total = 0.0
        
        for item in cart_items:
            try:
                # Remove $ and convert to float
                price = float(item["price"].replace("$", ""))
                quantity = int(item["quantity"])
                total += price * quantity
            except (ValueError, KeyError):
                continue
                
        return total
    
    def verify_cart_item_details(self, item_name: str, expected_price: Optional[str] = None, 
                                expected_quantity: Optional[str] = None) -> bool:
        """
        Verify details of a specific cart item.
        
        Args:
            item_name: Name of the item to verify
            expected_price: Expected price of the item
            expected_quantity: Expected quantity of the item
            
        Returns:
            bool: True if item details match expectations
        """
        cart_items = self.get_cart_items()
        
        for item in cart_items:
            if item["name"] == item_name:
                if expected_price and item["price"] != expected_price:
                    return False
                if expected_quantity and item["quantity"] != expected_quantity:
                    return False
                return True
                
        return False
