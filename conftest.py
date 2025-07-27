"""
PyTest configuration and fixtures for BDD test automation framework.
Contains browser setup, fixtures, and MCP Playwright integration.
"""
import pytest
import time
import os
from typing import Dict, Any


# Test configuration
BROWSER_TYPE = "chromium"  # chromium, firefox, webkit
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"  # Read from environment or default to headed
SLOW_MO = 100  # Milliseconds to slow down operations
TIMEOUT = 30000  # 30 seconds
VIEWPORT_SIZE = {"width": 1280, "height": 720}

# Test data
TEST_USERS = {
    "standard_user": "secret_sauce",
    "locked_out_user": "secret_sauce", 
    "problem_user": "secret_sauce",
    "performance_glitch_user": "secret_sauce"
}

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def browser_config():
    """Browser configuration fixture."""
    return {
        "browser_type": BROWSER_TYPE,
        "headless": HEADLESS,
        "slow_mo": SLOW_MO,
        "timeout": TIMEOUT,
        "viewport": VIEWPORT_SIZE
    }


@pytest.fixture(scope="function")
def browser_context(browser_config):
    """
    Browser context fixture for each test.
    This will integrate with MCP Playwright server.
    """
    context = {
        "config": browser_config,
        "base_url": BASE_URL,
        "test_users": TEST_USERS,
        "current_page": "login",
        "logged_in": False,
        "current_user": None,
        "items_in_cart": False,
        "test_start_time": time.time()
    }
    
    # Setup browser through MCP Playwright server
    # This would be implemented when using actual MCP calls
    
    yield context
    
    # Cleanup after test
    context["test_end_time"] = time.time()
    context["test_duration"] = context["test_end_time"] - context["test_start_time"]


@pytest.fixture(scope="function") 
def test_metadata():
    """Test metadata fixture for traceability."""
    return {
        "test_id": None,
        "module": None,
        "tags": [],
        "priority": "medium",
        "created_by": "automation_framework",
        "created_date": time.strftime("%Y-%m-%d %H:%M:%S")
    }


@pytest.fixture(scope="function")
def retry_config():
    """Retry configuration for flaky tests."""
    return {
        "max_retries": 3,
        "retry_delay": 1,  # seconds
        "retry_on_failure": True,
        "retry_on_timeout": True
    }


@pytest.fixture(autouse=True)
def test_setup_teardown(browser_context, test_metadata):
    """
    Auto-use fixture for test setup and teardown.
    Runs before and after each test.
    """
    # Setup
    print(f"\n=== Test Setup ===")
    print(f"Test: {test_metadata.get('test_id', 'Unknown')}")
    print(f"Module: {test_metadata.get('module', 'Unknown')}")
    print(f"Browser: {browser_context['config']['browser_type']}")
    
    # Take initial screenshot
    timestamp = int(time.time())
    browser_context["initial_screenshot"] = f"initial_{timestamp}.png"
    
    yield
    
    # Teardown
    print(f"\n=== Test Teardown ===")
    print(f"Duration: {browser_context.get('test_duration', 0):.2f} seconds")
    
    # Take final screenshot
    browser_context["final_screenshot"] = f"final_{timestamp}.png"
    
    # Generate test report data
    test_report = {
        "test_id": test_metadata.get("test_id"),
        "status": "unknown",  # Would be set based on test result
        "duration": browser_context.get("test_duration", 0),
        "screenshots": [
            browser_context.get("initial_screenshot"),
            browser_context.get("final_screenshot")
        ],
        "browser_config": browser_context["config"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    browser_context["test_report"] = test_report


@pytest.fixture
def authenticated_user(browser_context):
    """Fixture to provide an authenticated user session."""
    # This would use MCP Playwright to login
    browser_context["logged_in"] = True
    browser_context["current_user"] = "standard_user"
    browser_context["current_page"] = "products"
    return browser_context


@pytest.fixture
def empty_cart(browser_context):
    """Fixture to ensure cart is empty."""
    browser_context["items_in_cart"] = False
    return browser_context


@pytest.fixture
def cart_with_items(browser_context):
    """Fixture to provide cart with items."""
    browser_context["items_in_cart"] = True
    return browser_context


# Pytest hooks for better reporting and integration

def pytest_configure(config):
    """Configure pytest with custom markers and settings."""
    config.addinivalue_line(
        "markers", "auth: Authentication module tests"
    )
    config.addinivalue_line(
        "markers", "inventory: Inventory module tests"
    )
    config.addinivalue_line(
        "markers", "cart: Cart module tests"
    )
    config.addinivalue_line(
        "markers", "smoke: Smoke tests for critical functionality"
    )


def pytest_runtest_setup(item):
    """Setup for each test item."""
    # Extract test metadata
    markers = [marker.name for marker in item.iter_markers()]
    item.user_properties.append(("markers", markers))
    
    # Set test metadata based on markers
    if hasattr(item, "fixturenames") and "test_metadata" in item.fixturenames:
        # This would be passed to the test_metadata fixture
        pass


def pytest_runtest_makereport(item, call):
    """Generate test report."""
    if call.when == "call":
        # Test execution phase
        outcome = "PASSED" if call.excinfo is None else "FAILED"
        item.user_properties.append(("outcome", outcome))
        
        if call.excinfo:
            # Test failed - capture failure info
            item.user_properties.append(("failure_reason", str(call.excinfo.value)))


def pytest_html_report_title(report):
    """Customize HTML report title."""
    report.title = "Sauce Demo BDD Test Automation Report"


def pytest_html_results_table_header(cells):
    """Customize HTML report table headers."""
    cells.insert(2, '<th class="sortable" data-column-type="text">Module</th>')
    cells.insert(3, '<th class="sortable" data-column-type="text">Tags</th>')


def pytest_html_results_table_row(report, cells):
    """Customize HTML report table rows."""
    # Only process test reports, not collect reports
    if not hasattr(report, 'user_properties'):
        return
    
    # Extract module and tags from test markers
    markers = []
    module = "Unknown"
    
    for prop in report.user_properties:
        if prop[0] == "markers":
            markers = prop[1]
            if "auth" in markers:
                module = "Authentication"
            elif "inventory" in markers:
                module = "Inventory"
            elif "cart" in markers:
                module = "Cart"
            break
    
    cells.insert(2, f'<td>{module}</td>')
    cells.insert(3, f'<td>{", ".join(markers)}</td>')


# Retry mechanism for flaky tests
def pytest_runtest_protocol(item, nextitem):
    """Custom test execution protocol with retry logic."""
    # This would implement retry logic for failed tests
    # For now, just return None to use default protocol
    return None


# Test data fixtures
@pytest.fixture
def test_data():
    """Test data fixture."""
    return {
        "users": TEST_USERS,
        "products": [
            {
                "name": "Sauce Labs Backpack",
                "price": "$29.99",
                "description": "carry.allTheThings() with the sleek, streamlined Sly Pack"
            },
            {
                "name": "Sauce Labs Bike Light", 
                "price": "$9.99",
                "description": "A red light isn't the desired state in testing"
            }
        ],
        "sort_options": {
            "name_a_z": "az",
            "name_z_a": "za", 
            "price_low_high": "lohi",
            "price_high_low": "hilo"
        }
    }
