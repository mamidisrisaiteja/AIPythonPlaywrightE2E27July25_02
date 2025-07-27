# Sauce Demo BDD Test Automation Framework

A comprehensive Cucumber BDD test automation framework in Python using Playwright for the Sauce Demo e-commerce application.

## 🎯 Overview

This framework implements Behavior-Driven Development (BDD) using pytest-bdd with Playwright browser automation. It's designed to test the Sauce Demo application (https://www.saucedemo.com/) with full integration to Playwright MCP (Model Context Protocol) server for enhanced browser automation capabilities.

## 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern and implements **BDD (Behavior-Driven Development)** methodology:

```
ECommercePortal13/
├── pages/                    # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py         # Base page with common methods
│   ├── login_page.py        # Login page objects
│   ├── products_page.py     # Products/Inventory page objects
│   └── cart_page.py         # Cart page objects
├── features/                 # Gherkin feature files
│   ├── authentication.feature
│   ├── inventory.feature
│   └── cart.feature
├── step_definitions/         # Python glue logic for BDD
│   ├── __init__.py
│   ├── common_steps.py      # Shared step definitions
│   ├── auth_steps.py        # Authentication steps
│   └── cart_steps.py        # Cart-specific steps
├── tests/                   # Test runners
│   ├── __init__.py
│   ├── test_authentication.py
│   ├── test_inventory.py
│   └── test_cart.py
├── TestData/                # Test data and configurations
│   └── test_data.py
├── reports/                 # Generated test reports
├── conftest.py             # Pytest configuration and fixtures
├── pytest.ini             # Pytest settings
└── requirements.txt        # Dependencies
```

## 🚀 Features

### Core Features
- ✅ **BDD Implementation**: Cucumber-style Gherkin scenarios with pytest-bdd
- ✅ **Page Object Model**: Modular, maintainable page objects
- ✅ **MCP Integration**: Playwright MCP server for enhanced browser automation
- ✅ **Multi-Browser Support**: Chromium, Firefox, WebKit
- ✅ **Parallel Execution**: pytest-xdist for concurrent test execution
- ✅ **Rich Reporting**: HTML, JUnit XML, and Allure reports
- ✅ **Retry Logic**: Automatic retry for flaky tests
- ✅ **Screenshot Capture**: On failure and key checkpoints
- ✅ **Comprehensive Logging**: Detailed test execution logs

### Test Coverage
- 🔐 **Authentication Module** (`@auth`): Login scenarios with valid/invalid credentials
- 📦 **Inventory Module** (`@inventory`): Product listing, sorting, cart operations
- 🛒 **Cart Module** (`@cart`): Cart management and validation
- 🔥 **Smoke Tests** (`@smoke`): Critical functionality verification

## 📋 Test Cases Implemented

### Authentication Module (@auth)
| Test ID | Description | Tags |
|---------|-------------|------|
| TC_AUTH_01 | Login with valid credentials | @auth @smoke |
| TC_AUTH_01b | Login with invalid credentials | @auth |
| TC_AUTH_02 | Login with empty username | @auth |
| TC_AUTH_03 | Login with empty password | @auth |
| TC_AUTH_04 | Login with locked out user | @auth |

### Inventory Module (@inventory)
| Test ID | Description | Tags |
|---------|-------------|------|
| TC_INV_01 | Verify product listing | @inventory @smoke |
| TC_INV_02 | Sort products by Name (A–Z) | @inventory |
| TC_INV_03 | Sort products by Name (Z–A) | @inventory |
| TC_INV_04 | Sort by Price (Low to High) | @inventory |
| TC_INV_05 | Sort by Price (High to Low) | @inventory |

### Cart Module (@cart)
| Test ID | Description | Tags |
|---------|-------------|------|
| TC_CART_01 | View cart contents | @cart @smoke |
| TC_CART_02 | View empty cart | @cart |
| TC_CART_03 | Add/verify item in cart | @cart |
| TC_CART_04 | Remove item from cart | @cart |
| TC_CART_05 | Continue shopping from cart | @cart |

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- VS Code with MCP support
- Playwright MCP server configured

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ECommercePortal13
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

5. **Verify MCP configuration**:
   Ensure `.vscode/settings.json` contains:
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "npx",
         "args": ["@playwright/mcp@latest"]
       }
     }
   }
   ```

## 🏃 Running Tests

### Run All Tests
```bash
pytest
```

### Run by Module
```bash
# Authentication tests
pytest -m auth

# Inventory tests  
pytest -m inventory

# Cart tests
pytest -m cart
```

### Run Smoke Tests
```bash
pytest -m smoke
```

### Run with Custom Options
```bash
# Parallel execution
pytest -n 4

# Generate HTML report
pytest --html=reports/report.html

# Run specific feature
pytest tests/test_authentication.py

# Run with retries
pytest --reruns 3 --reruns-delay 1
```

### Run in Headless Mode
```bash
pytest --headless
```

## 📊 Reports and Logging

### Generated Reports
- **HTML Report**: `reports/report.html` - Interactive test results
- **JUnit XML**: `reports/junit.xml` - CI/CD integration
- **Pytest Log**: `reports/pytest.log` - Detailed execution logs
- **Screenshots**: Captured on failures in `reports/screenshots/`

### Viewing Reports
```bash
# Open HTML report
start reports/report.html  # Windows
open reports/report.html   # Mac
xdg-open reports/report.html  # Linux
```

## 🎪 Playwright MCP Integration

The framework integrates with Playwright MCP server for:
- **Enhanced Browser Control**: Advanced browser automation capabilities
- **Real-time Debugging**: Live browser inspection during test execution
- **Dynamic Element Handling**: Intelligent wait strategies and element interactions
- **Cross-browser Testing**: Seamless switching between browser engines

### MCP Commands Used
- `mcp_playwright_browser_navigate`: Navigate to URLs
- `mcp_playwright_browser_click`: Click elements
- `mcp_playwright_browser_type`: Type text
- `mcp_playwright_browser_snapshot`: Capture page state
- `mcp_playwright_browser_wait_for`: Wait for conditions

## 🔧 Configuration

### Browser Configuration
Edit `conftest.py` to modify browser settings:
```python
BROWSER_TYPE = "chromium"  # chromium, firefox, webkit
HEADLESS = False
TIMEOUT = 30000
VIEWPORT_SIZE = {"width": 1280, "height": 720}
```

### Test Data
Modify `TestData/test_data.py` for:
- User credentials
- Product information
- Expected text values
- Sort options

### Retry Configuration
Configure retry logic in `conftest.py`:
```python
RETRY_CONFIG = {
    "max_retries": 3,
    "retry_delay": 1,
    "retry_on_failure": True
}
```

## 📝 Writing New Tests

### 1. Create Feature File
```gherkin
# features/new_feature.feature
@new_module
Feature: New Feature
  Scenario: New test scenario
    Given precondition
    When action
    Then verification
```

### 2. Implement Step Definitions
```python
# step_definitions/new_steps.py
@given('precondition')
def step_precondition(browser_context):
    # Implementation
    pass
```

### 3. Create Test Runner
```python
# tests/test_new_feature.py
from pytest_bdd import scenarios
scenarios('../features/new_feature.feature')

class TestNewFeature:
    @pytest.mark.new_module
    def test_scenario(self, browser_context, test_metadata):
        # Test implementation
        pass
```

## 🐛 Debugging and Troubleshooting

### Common Issues

1. **MCP Server Not Running**:
   - Verify MCP configuration in VS Code settings
   - Restart VS Code
   - Check MCP server logs

2. **Element Not Found**:
   - Verify selectors in page objects
   - Check wait strategies
   - Update timeout values

3. **Test Failures**:
   - Check screenshots in reports folder
   - Review pytest logs
   - Verify test data

### Debug Mode
```bash
# Run with verbose output
pytest -v -s

# Debug specific test
pytest -k "test_name" -v -s --capture=no
```

## 🚀 CI/CD Integration

### GitHub Actions
```yaml
# .github/workflows/tests.yml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install
      - name: Run tests
        run: pytest --html=reports/report.html
```

### Jenkins Pipeline
```groovy
pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'playwright install'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --junitxml=reports/junit.xml'
            }
        }
    }
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}
```

## 📈 Best Practices

1. **Page Objects**: Keep page objects focused and maintainable
2. **Step Definitions**: Write reusable, atomic step definitions
3. **Test Data**: Externalize test data for easy maintenance
4. **Assertions**: Use descriptive assertion messages
5. **Error Handling**: Implement proper exception handling
6. **Documentation**: Keep scenarios self-documenting with clear Given-When-Then

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Follow coding standards and add tests
4. Commit changes: `git commit -m 'Add new feature'`
5. Push to branch: `git push origin feature/new-feature`
6. Submit pull request

## 📞 Support

For questions or issues:
- Create GitHub issue
- Review framework documentation
- Check existing test examples
- Consult Playwright MCP documentation

---

**Happy Testing! 🎯**
