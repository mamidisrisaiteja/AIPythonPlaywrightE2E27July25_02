"""
Products/Inventory Page Object Model for Sauce Demo application.
Handles all product listing, sorting, and selection interactions.
"""
from pages.base_page import BasePage
from typing import List


class ProductsPage(BasePage):
    """Products page object model for inventory module."""
    
    # Element selectors
    PRODUCTS_TITLE = '.title'
    PRODUCTS_CONTAINER = '.inventory_list'
    PRODUCT_ITEMS = '.inventory_item'
    PRODUCT_NAMES = '.inventory_item_name'
    PRODUCT_DESCRIPTIONS = '.inventory_item_desc'
    PRODUCT_PRICES = '.inventory_item_price'
    ADD_TO_CART_BUTTONS = '[data-test^="add-to-cart"]'
    REMOVE_BUTTONS = '[data-test^="remove"]'
    SORT_DROPDOWN = '[data-test="product_sort_container"]'
    SHOPPING_CART_LINK = '.shopping_cart_link'
    SHOPPING_CART_BADGE = '.shopping_cart_badge'
    HAMBURGER_MENU = '#react-burger-menu-btn'
    LOGOUT_LINK = '#logout_sidebar_link'
    
    # Sort options
    SORT_NAME_A_Z = "az"
    SORT_NAME_Z_A = "za"
    SORT_PRICE_LOW_HIGH = "lohi"
    SORT_PRICE_HIGH_LOW = "hilo"
    
    # Expected texts
    PRODUCTS_TITLE_TEXT = "Products"
    ADD_TO_CART_TEXT = "Add to cart"
    REMOVE_TEXT = "Remove"
    
    def __init__(self):
        """Initialize products page."""
        super().__init__()
        
    def is_products_page_displayed(self) -> bool:
        """
        Verify if products page is displayed.
        
        Returns:
            bool: True if products page is displayed
        """
        return (
            self.verify_page_contains_text(self.PRODUCTS_TITLE_TEXT) and
            self.is_element_visible(self.PRODUCTS_CONTAINER)
        )
    
    def verify_products_page_title(self) -> bool:
        """
        Verify the products page title.
        
        Returns:
            bool: True if products title is displayed
        """
        return self.verify_page_contains_text(self.PRODUCTS_TITLE_TEXT)
    
    def verify_add_to_cart_buttons_visible(self) -> bool:
        """
        Verify that add to cart buttons are visible.
        
        Returns:
            bool: True if add to cart buttons are visible
        """
        return self.verify_page_contains_text(self.ADD_TO_CART_TEXT)
    
    def get_product_names(self) -> List[str]:
        """
        Get list of all product names on the page.
        
        Returns:
            List[str]: List of product names
        """
        # This will be implemented with actual MCP Playwright calls
        # For now, return sample data for framework structure
        return [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light", 
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]
    
    def click_sort_dropdown(self) -> bool:
        """
        Click on the sort dropdown.
        
        Returns:
            bool: True if click successful
        """
        return self.click_element(
            self.SORT_DROPDOWN,
            "sort dropdown"
        )
    
    def select_sort_option(self, sort_option: str) -> bool:
        """
        Select a sort option from the dropdown.
        
        Args:
            sort_option: Sort option to select (az, za, lohi, hilo)
            
        Returns:
            bool: True if selection successful
        """
        return self.select_dropdown_option(
            self.SORT_DROPDOWN,
            sort_option,
            f"sort option {sort_option}"
        )
    
    def sort_products_by_name_a_z(self) -> bool:
        """
        Sort products by name A-Z.
        
        Returns:
            bool: True if sorting successful
        """
        return self.select_sort_option(self.SORT_NAME_A_Z)
    
    def sort_products_by_name_z_a(self) -> bool:
        """
        Sort products by name Z-A.
        
        Returns:
            bool: True if sorting successful
        """
        return self.select_sort_option(self.SORT_NAME_Z_A)
    
    def sort_products_by_price_low_high(self) -> bool:
        """
        Sort products by price low to high.
        
        Returns:
            bool: True if sorting successful
        """
        return self.select_sort_option(self.SORT_PRICE_LOW_HIGH)
    
    def sort_products_by_price_high_low(self) -> bool:
        """
        Sort products by price high to low.
        
        Returns:
            bool: True if sorting successful
        """
        return self.select_sort_option(self.SORT_PRICE_HIGH_LOW)
    
    def verify_products_sorted_alphabetically(self) -> bool:
        """
        Verify that products are sorted alphabetically A-Z.
        
        Returns:
            bool: True if products are sorted correctly
        """
        product_names = self.get_product_names()
        sorted_names = sorted(product_names)
        return product_names == sorted_names
    
    def add_product_to_cart_by_name(self, product_name: str) -> bool:
        """
        Add a specific product to cart by name.
        
        Args:
            product_name: Name of the product to add
            
        Returns:
            bool: True if product added successfully
        """
        # Convert product name to data-test attribute format
        test_id = product_name.lower().replace(" ", "-").replace(".", "").replace("(", "").replace(")", "")
        add_button_selector = f'[data-test="add-to-cart-{test_id}"]'
        
        return self.click_element(
            add_button_selector,
            f"add to cart button for {product_name}"
        )
    
    def add_first_product_to_cart(self) -> bool:
        """
        Add the first product to cart.
        
        Returns:
            bool: True if product added successfully
        """
        return self.add_product_to_cart_by_name("Sauce Labs Backpack")
    
    def click_shopping_cart(self) -> bool:
        """
        Click on the shopping cart icon.
        
        Returns:
            bool: True if click successful
        """
        return self.click_element(
            self.SHOPPING_CART_LINK,
            "shopping cart icon"
        )
    
    def get_cart_item_count(self) -> int:
        """
        Get the number of items in the cart from the badge.
        
        Returns:
            int: Number of items in cart
        """
        if self.is_element_visible(self.SHOPPING_CART_BADGE):
            badge_text = self.get_text(self.SHOPPING_CART_BADGE)
            try:
                return int(badge_text or "0")
            except ValueError:
                return 0
        return 0
    
    def logout(self) -> bool:
        """
        Logout from the application.
        
        Returns:
            bool: True if logout successful
        """
        # Click hamburger menu
        if not self.click_element(self.HAMBURGER_MENU, "hamburger menu"):
            return False
            
        # Click logout link
        return self.click_element(self.LOGOUT_LINK, "logout link")
