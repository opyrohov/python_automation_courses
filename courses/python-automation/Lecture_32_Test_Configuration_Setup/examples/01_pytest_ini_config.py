"""Example 1: pytest.ini and pyproject.toml Configuration

Demonstrates how to configure pytest settings for your project.
This file shows the configuration options and how they affect test execution.

Configuration files (choose ONE):
- pytest.ini       (classic, simple)
- pyproject.toml   (modern, combines with other tools)
- setup.cfg        (legacy, also works)
"""
from playwright.sync_api import Page


# ============================================
# pytest.ini EXAMPLE
# ============================================
#
# Create a file called pytest.ini in your project root:
#
# [pytest]
# # Default command line options
# addopts = -v --tb=short
#
# # Where to find tests
# testpaths = tests
#
# # Test file patterns
# python_files = test_*.py
# python_functions = test_*
# python_classes = Test*
#
# # Register custom markers
# markers =
#     smoke: Quick smoke tests
#     regression: Full regression suite
#     slow: Tests that take a long time
#
# # Base URL for Playwright
# base_url = https://the-internet.herokuapp.com


# ============================================
# pyproject.toml EXAMPLE
# ============================================
#
# Add to pyproject.toml in your project root:
#
# [tool.pytest.ini_options]
# addopts = "-v --tb=short"
# testpaths = ["tests"]
# python_files = ["test_*.py"]
# python_functions = ["test_*"]
# python_classes = ["Test*"]
# markers = [
#     "smoke: Quick smoke tests",
#     "regression: Full regression suite",
#     "slow: Tests that take a long time",
# ]
# base_url = "https://the-internet.herokuapp.com"


# ============================================
# HOW addopts WORKS
# ============================================
#
# addopts = -v --tb=short
#
# This means running just "pytest" is equivalent to:
#   pytest -v --tb=short
#
# Common addopts combinations:
#   addopts = -v                          # Always verbose
#   addopts = -v --tb=short               # Verbose + short tracebacks
#   addopts = -v -x                       # Stop on first failure
#   addopts = -v --strict-markers         # Error on unknown markers
#   addopts = -v --headed                 # Always show browser


# ============================================
# DEMO: Tests that work with base_url
# ============================================

def test_homepage(page: Page, base_url):
    """When base_url is set, you can use relative paths."""
    # With base_url = "https://the-internet.herokuapp.com"
    # page.goto("/") goes to "https://the-internet.herokuapp.com/"
    page.goto(base_url)
    assert page.title() == "The Internet"


def test_login_page(page: Page, base_url):
    """Using base_url to navigate to subpages."""
    page.goto(f"{base_url}/login")
    assert page.locator("h2").text_content() == "Login Page"


def test_checkboxes_page(page: Page, base_url):
    """Another page using base_url."""
    page.goto(f"{base_url}/checkboxes")
    assert page.locator("h3").text_content() == "Checkboxes"


# ============================================
# DEMO: Tests with markers (registered in pytest.ini)
# ============================================

import pytest


@pytest.mark.smoke
def test_site_is_up(page: Page, base_url):
    """Smoke test - site responds."""
    page.goto(base_url)
    assert page.title()


@pytest.mark.regression
def test_all_links_present(page: Page, base_url):
    """Regression - check all links on homepage."""
    page.goto(base_url)
    links = page.locator("#content ul li a")
    assert links.count() > 20


# ============================================
# KEY POINTS:
#
# 1. pytest.ini - classic config file
# 2. pyproject.toml - modern alternative
# 3. addopts - default CLI arguments
# 4. testpaths - where to find tests
# 5. markers - register custom markers
# 6. base_url - set base URL for all tests
# 7. --strict-markers - catch typos in markers
#
# Run: pytest 01_pytest_ini_config.py -v
# ============================================
