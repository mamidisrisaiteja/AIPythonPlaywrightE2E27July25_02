#!/usr/bin/env python3
"""
Test execution script for Sauce Demo BDD Framework.
Provides various options to run tests using the Playwright MCP integration.
"""
import os
import sys
import argparse
import subprocess
from pathlib import Path


def setup_environment():
    """Setup the test environment."""
    print("🔧 Setting up test environment...")
    
    # Ensure we're in the right directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Create reports directory if it doesn't exist
    reports_dir = project_root / "reports"
    reports_dir.mkdir(exist_ok=True)
    
    print(f"✅ Working directory: {project_root}")
    print(f"✅ Reports directory: {reports_dir}")


def run_smoke_tests():
    """Run smoke tests."""
    print("🔥 Running smoke tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-m", "smoke",
        "-v",
        "--tb=short",
        "--html=reports/smoke_test_report.html",
        "--self-contained-html",
        "--junitxml=reports/smoke_junit.xml"
    ]
    return subprocess.run(cmd)


def run_auth_tests():
    """Run authentication module tests."""
    print("🔐 Running authentication tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-m", "auth",
        "-v",
        "--tb=short", 
        "--html=reports/auth_test_report.html",
        "--self-contained-html",
        "--junitxml=reports/auth_junit.xml"
    ]
    return subprocess.run(cmd)


def run_inventory_tests():
    """Run inventory module tests."""
    print("📦 Running inventory tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-m", "inventory",
        "-v",
        "--tb=short",
        "--html=reports/inventory_test_report.html", 
        "--self-contained-html",
        "--junitxml=reports/inventory_junit.xml"
    ]
    return subprocess.run(cmd)


def run_cart_tests():
    """Run cart module tests."""
    print("🛒 Running cart tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-m", "cart",
        "-v",
        "--tb=short",
        "--html=reports/cart_test_report.html",
        "--self-contained-html", 
        "--junitxml=reports/cart_junit.xml"
    ]
    return subprocess.run(cmd)


def run_all_tests():
    """Run all tests."""
    print("🚀 Running all tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-v",
        "--tb=short",
        "--html=reports/full_test_report.html",
        "--self-contained-html",
        "--junitxml=reports/full_junit.xml",
        "--maxfail=10"
    ]
    return subprocess.run(cmd)


def run_parallel_tests():
    """Run tests in parallel."""
    print("⚡ Running tests in parallel...")
    cmd = [
        sys.executable, "-m", "pytest",
        "-n", "4",  # 4 parallel workers
        "-v",
        "--tb=short",
        "--html=reports/parallel_test_report.html",
        "--self-contained-html",
        "--junitxml=reports/parallel_junit.xml"
    ]
    return subprocess.run(cmd)


def run_specific_test(test_name):
    """Run a specific test."""
    print(f"🎯 Running specific test: {test_name}")
    cmd = [
        sys.executable, "-m", "pytest",
        "-k", test_name,
        "-v",
        "-s",
        "--tb=long",
        "--html=reports/specific_test_report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)


def run_mcp_demo():
    """Run MCP integration demo."""
    print("🎭 Running MCP integration demo...")
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_mcp_demo.py",
        "-v",
        "-s",
        "--tb=short",
        "--html=reports/mcp_demo_report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)


def show_test_structure():
    """Show the test structure."""
    print("📁 Test Framework Structure:")
    print("=" * 50)
    
    structure = """
    ECommercePortal13/
    ├── 📁 pages/                    # Page Object Model
    │   ├── base_page.py            # Base page functionality
    │   ├── login_page.py           # Login page objects
    │   ├── products_page.py        # Products page objects
    │   └── cart_page.py            # Cart page objects
    ├── 📁 features/                 # Gherkin feature files
    │   ├── authentication.feature  # Login scenarios
    │   ├── inventory.feature       # Product scenarios
    │   └── cart.feature            # Cart scenarios
    ├── 📁 step_definitions/         # BDD step implementations
    │   ├── common_steps.py         # Shared steps
    │   ├── auth_steps.py           # Auth-specific steps
    │   └── cart_steps.py           # Cart-specific steps
    ├── 📁 tests/                   # Test runners
    │   ├── test_authentication.py  # Auth test runner
    │   ├── test_inventory.py       # Inventory test runner
    │   ├── test_cart.py            # Cart test runner
    │   └── test_mcp_demo.py        # MCP demo tests
    ├── 📁 TestData/                # Test data
    │   └── test_data.py            # Constants and config
    ├── 📁 reports/                 # Generated reports
    ├── mcp_integration.py          # MCP Playwright client
    ├── conftest.py                 # Pytest configuration
    └── pytest.ini                 # Pytest settings
    """
    
    print(structure)
    
    print("\n🏷️ Available Test Tags:")
    print("  @auth      - Authentication module tests")
    print("  @inventory - Inventory module tests") 
    print("  @cart      - Cart module tests")
    print("  @smoke     - Critical functionality tests")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Sauce Demo BDD Test Automation Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py --smoke                    # Run smoke tests
  python run_tests.py --auth                     # Run auth tests
  python run_tests.py --all                      # Run all tests
  python run_tests.py --parallel                 # Run tests in parallel
  python run_tests.py --test login_with_valid    # Run specific test
  python run_tests.py --mcp-demo                 # Run MCP demo
  python run_tests.py --structure                # Show framework structure
        """
    )
    
    parser.add_argument("--smoke", action="store_true", help="Run smoke tests")
    parser.add_argument("--auth", action="store_true", help="Run authentication tests")
    parser.add_argument("--inventory", action="store_true", help="Run inventory tests")
    parser.add_argument("--cart", action="store_true", help="Run cart tests")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    parser.add_argument("--parallel", action="store_true", help="Run tests in parallel")
    parser.add_argument("--test", type=str, help="Run specific test by name")
    parser.add_argument("--mcp-demo", action="store_true", help="Run MCP integration demo")
    parser.add_argument("--structure", action="store_true", help="Show test framework structure")
    parser.add_argument("--headed", action="store_true", help="Run tests in headed mode (browser visible)")
    parser.add_argument("--headless", action="store_true", help="Run tests in headless mode (browser hidden)")
    
    args = parser.parse_args()
    
    # Handle browser mode configuration
    if args.headed and args.headless:
        print("❌ Error: Cannot specify both --headed and --headless options")
        return
    
    if args.headed:
        print("🖥️  Running in HEADED mode (browser visible)")
        os.environ["HEADLESS"] = "false"
    elif args.headless:
        print("👻 Running in HEADLESS mode (browser hidden)")
        os.environ["HEADLESS"] = "true"
    else:
        print("🖥️  Running in HEADED mode (default - browser visible)")
        os.environ["HEADLESS"] = "false"
    
    # Print header
    print("🎯 Sauce Demo BDD Test Automation Framework")
    print("=" * 60)
    print("🌐 Target: https://www.saucedemo.com/")
    print("🤖 Engine: Playwright MCP Server")
    print("🥒 Framework: pytest-bdd (Cucumber style)")
    print("=" * 60)
    
    if args.structure:
        show_test_structure()
        return
    
    # Setup environment
    setup_environment()
    
    # Execute based on arguments
    result = None
    
    if args.smoke:
        result = run_smoke_tests()
    elif args.auth:
        result = run_auth_tests()
    elif args.inventory:
        result = run_inventory_tests()
    elif args.cart:
        result = run_cart_tests()
    elif args.all:
        result = run_all_tests()
    elif args.parallel:
        result = run_parallel_tests()
    elif args.test:
        result = run_specific_test(args.test)
    elif args.mcp_demo:
        result = run_mcp_demo()
    else:
        print("ℹ️  No specific test option provided. Use --help for options.")
        print("🚀 Running smoke tests by default...")
        result = run_smoke_tests()
    
    # Print results
    if result:
        print("\n" + "=" * 60)
        if result.returncode == 0:
            print("✅ Tests completed successfully!")
        else:
            print("❌ Some tests failed!")
        print(f"📊 Exit code: {result.returncode}")
        print("📁 Check reports/ directory for detailed results")


if __name__ == "__main__":
    main()
