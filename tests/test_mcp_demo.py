"""
Sample test execution demonstrating Playwright MCP integration.
This script shows how to run a real test case using the MCP server.
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestMCPIntegrationDemo:
    """
    Demo test class showing MCP Playwright integration.
    This will be executed using the actual MCP server configured in VS Code.
    """
    
    @pytest.mark.smoke
    @pytest.mark.auth
    def test_login_with_mcp_integration(self, browser_context, test_metadata):
        """
        Demo test: TC_AUTH_01 - Login with valid credentials using MCP.
        This test demonstrates the complete flow using Playwright MCP server.
        """
        test_metadata.update({
            "test_id": "TC_AUTH_01_MCP_DEMO",
            "module": "Authentication",
            "tags": ["auth", "smoke", "mcp_demo"],
            "description": "Login with valid credentials using MCP Playwright server"
        })
        
        # Initialize page objects
        login_page = LoginPage()
        products_page = ProductsPage()
        
        # Test execution - this will use MCP Playwright server
        print("🚀 Starting MCP Playwright test execution...")
        
        # Step 1: Navigate to Sauce Demo
        print("📍 Step 1: Navigating to https://www.saucedemo.com/")
        assert login_page.navigate_to_login_page(), "Failed to navigate to login page"
        
        # Step 2: Verify login page is displayed
        print("✅ Step 2: Verifying login page is displayed")
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        
        # Step 3: Enter valid credentials
        print("🔑 Step 3: Entering valid credentials")
        assert login_page.enter_username("standard_user"), "Failed to enter username"
        assert login_page.enter_password("secret_sauce"), "Failed to enter password"
        
        # Step 4: Click login button
        print("🖱️ Step 4: Clicking login button")
        assert login_page.click_login_button(), "Failed to click login button"
        
        # Step 5: Verify successful login
        print("🎯 Step 5: Verifying successful login")
        assert login_page.verify_login_successful(), "Login was not successful"
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        
        print("✨ Test completed successfully with MCP integration!")
    
    @pytest.mark.inventory
    @pytest.mark.smoke  
    def test_add_to_cart_with_mcp(self, browser_context, test_metadata):
        """
        Demo test: Add product to cart using MCP integration.
        """
        test_metadata.update({
            "test_id": "TC_CART_MCP_DEMO",
            "module": "Cart",
            "tags": ["cart", "smoke", "mcp_demo"],
            "description": "Add product to cart and verify using MCP"
        })
        
        # Pre-requisite: Login first
        login_page = LoginPage()
        products_page = ProductsPage()
        cart_page = CartPage()
        
        print("🔐 Pre-requisite: Logging in...")
        assert login_page.navigate_to_login_page(), "Failed to navigate"
        assert login_page.login("standard_user", "secret_sauce"), "Failed to login"
        
        # Step 1: Verify products page
        print("📦 Step 1: Verifying products page")
        assert products_page.verify_products_page_title(), "Products title not found"
        assert products_page.verify_add_to_cart_buttons_visible(), "Add to cart buttons not visible"
        
        # Step 2: Add product to cart
        print("🛒 Step 2: Adding Sauce Labs Backpack to cart")
        assert products_page.add_product_to_cart_by_name("Sauce Labs Backpack"), "Failed to add product"
        
        # Step 3: Verify cart count
        print("🔢 Step 3: Verifying cart count")
        cart_count = products_page.get_cart_item_count()
        assert cart_count == 1, f"Expected cart count 1, got {cart_count}"
        
        # Step 4: Navigate to cart
        print("🏪 Step 4: Navigating to cart page")
        assert products_page.click_shopping_cart(), "Failed to click cart"
        
        # Step 5: Verify cart contents
        print("✅ Step 5: Verifying cart contents")
        assert cart_page.verify_your_cart_text(), "Cart page title not found"
        assert cart_page.verify_item_in_cart("Sauce Labs Backpack"), "Product not found in cart"
        
        print("🎉 Cart test completed successfully with MCP!")


def run_mcp_demo():
    """
    Function to run the MCP demo tests.
    This can be called directly to execute the demo.
    """
    print("🎭 Sauce Demo BDD Framework - MCP Integration Demo")
    print("=" * 60)
    
    # Run the demo tests
    pytest.main([
        "tests/test_mcp_demo.py",
        "-v",
        "-s", 
        "--tb=short",
        "--html=reports/mcp_demo_report.html",
        "--self-contained-html"
    ])


if __name__ == "__main__":
    run_mcp_demo()
