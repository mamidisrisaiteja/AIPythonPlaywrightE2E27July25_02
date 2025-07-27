"""
Test runner for Inventory module BDD tests.
Maps Gherkin scenarios to pytest-bdd test functions.
"""
import pytest
from pytest_bdd import scenarios


# Import step definitions
from step_definitions import common_steps

# Load all scenarios from the inventory feature file
scenarios('../features/inventory.feature')


class TestInventory:
    """Test class for inventory module scenarios."""
    
    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_verify_product_listing(self, browser_context, test_metadata, authenticated_user):
        """Test TC_INV_01: Verify product listing."""
        test_metadata.update({
            "test_id": "TC_INV_01",
            "module": "Inventory",
            "tags": ["inventory", "smoke"],
            "description": "Verify products page displays products and add to cart buttons"
        })
        
        # Test is implemented through BDD steps
        pass
    
    @pytest.mark.inventory
    def test_sort_products_by_name_a_z(self, browser_context, test_metadata, authenticated_user):
        """Test TC_INV_02: Sort products by Name (A–Z)."""
        test_metadata.update({
            "test_id": "TC_INV_02",
            "module": "Inventory", 
            "tags": ["inventory"],
            "description": "Sort products by name A-Z and verify sorting is correct"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory
    def test_sort_products_by_name_z_a(self, browser_context, test_metadata, authenticated_user):
        """Test sorting products by Name (Z–A)."""
        test_metadata.update({
            "test_id": "TC_INV_03",
            "module": "Inventory",
            "tags": ["inventory"],
            "description": "Sort products by name Z-A and verify sorting is correct"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory
    def test_sort_products_by_price_low_high(self, browser_context, test_metadata, authenticated_user):
        """Test sorting products by Price (Low to High)."""
        test_metadata.update({
            "test_id": "TC_INV_04",
            "module": "Inventory",
            "tags": ["inventory"],
            "description": "Sort products by price low to high and verify sorting is correct"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory 
    def test_sort_products_by_price_high_low(self, browser_context, test_metadata, authenticated_user):
        """Test sorting products by Price (High to Low).""" 
        test_metadata.update({
            "test_id": "TC_INV_05",
            "module": "Inventory",
            "tags": ["inventory"],
            "description": "Sort products by price high to low and verify sorting is correct"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory
    def test_add_single_product_to_cart(self, browser_context, test_metadata, authenticated_user):
        """Test adding single product to cart."""
        test_metadata.update({
            "test_id": "TC_INV_06",
            "module": "Inventory",
            "tags": ["inventory"],
            "description": "Add single product to cart and verify cart count"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory
    def test_add_multiple_products_to_cart(self, browser_context, test_metadata, authenticated_user):
        """Test adding multiple products to cart."""
        test_metadata.update({
            "test_id": "TC_INV_07", 
            "module": "Inventory",
            "tags": ["inventory"],
            "description": "Add multiple products to cart and verify cart count"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.inventory
    def test_remove_product_from_cart_on_products_page(self, browser_context, test_metadata, authenticated_user):
        """Test removing product from cart on products page."""
        test_metadata.update({
            "test_id": "TC_INV_08",
            "module": "Inventory", 
            "tags": ["inventory"],
            "description": "Remove product from cart on products page and verify cart count"
        })
        
        # Test is implemented through BDD steps
        pass
