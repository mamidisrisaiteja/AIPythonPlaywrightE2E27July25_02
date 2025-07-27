"""
Test runner for Authentication module BDD tests.
Maps Gherkin scenarios to pytest-bdd test functions.
"""
import pytest
from pytest_bdd import scenarios


# Import step definitions
from step_definitions import common_steps, auth_steps

# Load all scenarios from the authentication feature file
scenarios('../features/authentication.feature')


class TestAuthentication:
    """Test class for authentication module scenarios."""
    
    @pytest.mark.auth
    @pytest.mark.smoke
    def test_login_with_valid_credentials(self, browser_context, test_metadata):
        """Test TC_AUTH_01: Login with valid credentials."""
        test_metadata.update({
            "test_id": "TC_AUTH_01",
            "module": "Authentication",
            "tags": ["auth", "smoke"],
            "description": "Login with valid credentials and verify redirect to products page"
        })
        
        # Test is implemented through BDD steps
        pass
    
    @pytest.mark.auth  
    def test_login_with_invalid_credentials(self, browser_context, test_metadata):
        """Test TC_AUTH_01b: Login with invalid credentials."""
        test_metadata.update({
            "test_id": "TC_AUTH_01b", 
            "module": "Authentication",
            "tags": ["auth"],
            "description": "Login with invalid credentials and verify login fails"
        })
        
        # Test is implemented through BDD steps
        pass
    
    @pytest.mark.auth
    def test_login_with_empty_username(self, browser_context, test_metadata):
        """Test authentication with empty username."""
        test_metadata.update({
            "test_id": "TC_AUTH_02",
            "module": "Authentication", 
            "tags": ["auth"],
            "description": "Verify login fails with empty username"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.auth
    def test_login_with_empty_password(self, browser_context, test_metadata):
        """Test authentication with empty password."""
        test_metadata.update({
            "test_id": "TC_AUTH_03",
            "module": "Authentication",
            "tags": ["auth"], 
            "description": "Verify login fails with empty password"
        })
        
        # Test is implemented through BDD steps
        pass
        
    @pytest.mark.auth
    def test_login_with_locked_user(self, browser_context, test_metadata):
        """Test authentication with locked out user."""
        test_metadata.update({
            "test_id": "TC_AUTH_04",
            "module": "Authentication",
            "tags": ["auth"],
            "description": "Verify login fails for locked out user"
        })
        
        # Test is implemented through BDD steps
        pass
