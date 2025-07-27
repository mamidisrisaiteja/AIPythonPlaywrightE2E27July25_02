"""
Login Page Object Model for Sauce Demo application.
Handles all login-related interactions and validations.
"""
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model for authentication module."""
    
    # Page URL
    URL = "https://www.saucedemo.com/"
    
    # Element selectors
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'
    LOGO = '.login_logo'
    
    # Expected texts
    LOGIN_LOGO_TEXT = "Swag Labs"
    PRODUCTS_PAGE_TEXT = "Products"
    LOGIN_ERROR_TEXT = "Epic sadface:"
    
    def __init__(self):
        """Initialize login page."""
        super().__init__()
        
    def navigate_to_login_page(self) -> bool:
        """
        Navigate to the login page.
        
        Returns:
            bool: True if navigation successful
        """
        return self.navigate_to(self.URL)
    
    def enter_username(self, username: str) -> bool:
        """
        Enter username in the username field.
        
        Args:
            username: Username to enter
            
        Returns:
            bool: True if successful
        """
        return self.type_text(
            self.USERNAME_INPUT, 
            username, 
            "username input field"
        )
    
    def enter_password(self, password: str) -> bool:
        """
        Enter password in the password field.
        
        Args:
            password: Password to enter
            
        Returns:
            bool: True if successful
        """
        return self.type_text(
            self.PASSWORD_INPUT, 
            password, 
            "password input field"
        )
    
    def click_login_button(self) -> bool:
        """
        Click the login button.
        
        Returns:
            bool: True if click successful
        """
        return self.click_element(
            self.LOGIN_BUTTON, 
            "login button"
        )
    
    def login(self, username: str, password: str) -> bool:
        """
        Perform complete login operation.
        
        Args:
            username: Username for login
            password: Password for login
            
        Returns:
            bool: True if login process completed successfully
        """
        try:
            # Enter credentials
            if not self.enter_username(username):
                return False
                
            if not self.enter_password(password):
                return False
                
            # Click login button
            if not self.click_login_button():
                return False
                
            return True
            
        except Exception as e:
            print(f"Login failed: {e}")
            return False
    
    def is_login_page_displayed(self) -> bool:
        """
        Verify if login page is displayed.
        
        Returns:
            bool: True if login page is displayed
        """
        return (
            self.is_element_visible(self.USERNAME_INPUT) and
            self.is_element_visible(self.PASSWORD_INPUT) and
            self.is_element_visible(self.LOGIN_BUTTON)
        )
    
    def verify_login_successful(self) -> bool:
        """
        Verify if login was successful by checking for Products page.
        
        Returns:
            bool: True if redirected to products page
        """
        return self.verify_page_contains_text(self.PRODUCTS_PAGE_TEXT)
    
    def verify_login_failed(self) -> bool:
        """
        Verify if login failed by checking if still on login page.
        
        Returns:
            bool: True if still on login page (login failed)
        """
        return (
            self.is_element_visible(self.LOGIN_BUTTON) or
            self.is_element_visible(self.ERROR_MESSAGE)
        )
    
    def get_error_message(self) -> str:
        """
        Get the error message text if displayed.
        
        Returns:
            str: Error message text or empty string
        """
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE) or ""
        return ""
    
    def verify_error_message_contains(self, expected_text: str) -> bool:
        """
        Verify error message contains expected text.
        
        Args:
            expected_text: Text to verify in error message
            
        Returns:
            bool: True if error message contains expected text
        """
        error_message = self.get_error_message()
        return expected_text.lower() in error_message.lower()
    
    def clear_username(self) -> bool:
        """
        Clear the username field.
        
        Returns:
            bool: True if successful
        """
        return self.click_element(self.USERNAME_INPUT, "username field") and \
               self.type_text(self.USERNAME_INPUT, "", "username field")
    
    def clear_password(self) -> bool:
        """
        Clear the password field.
        
        Returns:
            bool: True if successful
        """
        return self.click_element(self.PASSWORD_INPUT, "password field") and \
               self.type_text(self.PASSWORD_INPUT, "", "password field")
