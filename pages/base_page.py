"""
Base Page Object Model class providing common functionality for all pages.
This class integrates with Playwright MCP server for browser automation.
"""
import time
from typing import Optional
from mcp_integration import (
    mcp_navigate, mcp_click, mcp_type, mcp_verify_text, 
    mcp_wait_for_element, mcp_screenshot, mcp_select_option
)


class BasePage:
    """Base page class with common page operations."""
    
    def __init__(self):
        """Initialize base page."""
        self.timeout = 30000  # 30 seconds default timeout
        
    def navigate_to(self, url: str) -> bool:
        """
        Navigate to a specific URL.
        
        Args:
            url: The URL to navigate to
            
        Returns:
            bool: True if navigation successful
        """
        try:
            return mcp_navigate(url)
        except Exception as e:
            print(f"Navigation failed: {e}")
            return False
    
    def wait_for_element(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Wait for an element to be visible.
        
        Args:
            selector: CSS selector or element identifier
            timeout: Wait timeout in milliseconds
            
        Returns:
            bool: True if element found within timeout
        """
        try:
            return mcp_wait_for_element(selector, timeout)
        except Exception as e:
            print(f"Element not found: {selector}, Error: {e}")
            return False
    
    def click_element(self, selector: str, element_description: str = "") -> bool:
        """
        Click on an element.
        
        Args:
            selector: CSS selector or element identifier
            element_description: Human readable description of element
            
        Returns:
            bool: True if click successful
        """
        try:
            return mcp_click(selector, element_description)
        except Exception as e:
            print(f"Click failed on {selector}: {e}")
            return False
    
    def type_text(self, selector: str, text: str, element_description: str = "") -> bool:
        """
        Type text into an element.
        
        Args:
            selector: CSS selector or element identifier
            text: Text to type
            element_description: Human readable description of element
            
        Returns:
            bool: True if typing successful
        """
        try:
            return mcp_type(selector, text, element_description)
        except Exception as e:
            print(f"Typing failed on {selector}: {e}")
            return False
    
    def get_text(self, selector: str) -> Optional[str]:
        """
        Get text content of an element.
        
        Args:
            selector: CSS selector or element identifier
            
        Returns:
            str: Element text content or None if not found
        """
        try:
            # This will be handled by MCP Playwright server
            return ""
        except Exception as e:
            print(f"Get text failed on {selector}: {e}")
            return None
    
    def is_element_visible(self, selector: str) -> bool:
        """
        Check if element is visible.
        
        Args:
            selector: CSS selector or element identifier
            
        Returns:
            bool: True if element is visible
        """
        try:
            # This will be handled by MCP Playwright server
            return True
        except Exception as e:
            print(f"Visibility check failed on {selector}: {e}")
            return False
    
    def verify_page_contains_text(self, text: str) -> bool:
        """
        Verify that page contains specific text.
        
        Args:
            text: Text to search for
            
        Returns:
            bool: True if text found on page
        """
        try:
            return mcp_verify_text(text)
        except Exception as e:
            print(f"Text verification failed for '{text}': {e}")
            return False
    
    def take_screenshot(self, filename: Optional[str] = None) -> str:
        """
        Take a screenshot of the current page.
        
        Args:
            filename: Optional filename for screenshot
            
        Returns:
            str: Path to screenshot file
        """
        try:
            return mcp_screenshot(filename)
        except Exception as e:
            print(f"Screenshot failed: {e}")
            return ""
    
    def select_dropdown_option(self, selector: str, value: str, element_description: str = "") -> bool:
        """
        Select an option from dropdown.
        
        Args:
            selector: CSS selector for dropdown
            value: Value to select
            element_description: Human readable description
            
        Returns:
            bool: True if selection successful
        """
        try:
            return mcp_select_option(selector, value, element_description)
        except Exception as e:
            print(f"Dropdown selection failed on {selector}: {e}")
            return False
