"""Example 4: CI/CD Integration

Demonstrates how to configure Playwright tests for CI/CD pipelines,
Docker setup, parallel execution, and artifact collection.

Run with:
    pytest 04_ci_cd_integration.py -v -s
"""
import pytest
import os
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# GITHUB ACTIONS WORKFLOW
# ============================================
#
# .github/workflows/tests.yml:
#
# name: Playwright Tests
# on:
#   push:
#     branches: [main]
#   pull_request:
#     branches: [main]
#
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#
#       - name: Set up Python
#         uses: actions/setup-python@v5
#         with:
#           python-version: "3.12"
#
#       - name: Install dependencies
#         run: |
#           pip install -r requirements.txt
#           playwright install --with-deps chromium
#
#       - name: Run tests
#         run: |
#           pytest --tracing retain-on-failure \
#                  --screenshot only-on-failure \
#                  --output test-results/ \
#                  -v
#
#       - name: Upload artifacts
#         if: failure()
#         uses: actions/upload-artifact@v4
#         with:
#           name: test-results
#           path: test-results/


# ============================================
# DOCKER SETUP
# ============================================
#
# Dockerfile:
#
# FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
#
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
#
# COPY . .
#
# CMD ["pytest", "--tracing", "retain-on-failure", "-v"]
#
#
# docker-compose.yml:
#
# services:
#   tests:
#     build: .
#     volumes:
#       - ./test-results:/app/test-results
#     environment:
#       - BASE_URL=https://the-internet.herokuapp.com


# ============================================
# ENVIRONMENT-AWARE CONFIGURATION
# ============================================

@pytest.fixture(scope="session")
def env_base_url():
    """Get base URL from environment (CI vs local)."""
    return os.environ.get("BASE_URL", BASE_URL)


def test_env_aware(page: Page, env_base_url):
    """Test that uses environment-configured URL."""
    page.goto(f"{env_base_url}/login")
    assert page.locator("h2").text_content() == "Login Page"


# ============================================
# PARALLEL EXECUTION
# ============================================
#
# Install: pip install pytest-xdist
#
# Run in parallel:
#   pytest -n auto              # Auto-detect CPU count
#   pytest -n 4                 # Use 4 workers
#   pytest -n auto --dist loadgroup  # Group tests
#
# Mark tests that CANNOT run in parallel:
# @pytest.mark.xdist_group("serial")
# def test_that_needs_isolation(page):
#     ...


@pytest.mark.smoke
def test_homepage_loads(page: Page):
    """Quick smoke test - ideal for parallel execution."""
    page.goto(BASE_URL)
    assert page.title() == "The Internet"


@pytest.mark.smoke
def test_login_page_accessible(page: Page):
    """Another independent test - can run in parallel."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("#username").is_visible()


@pytest.mark.smoke
def test_checkboxes_page_accessible(page: Page):
    """Independent test - can run in parallel."""
    page.goto(f"{BASE_URL}/checkboxes")
    assert page.locator("input[type='checkbox']").count() == 2


# ============================================
# ARTIFACTS COLLECTION
# ============================================

@pytest.fixture
def artifact_page(page: Page, request, tmp_path):
    """Fixture that saves artifacts on test failure."""
    yield page

    # Save screenshot and HTML on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        name = request.node.name
        screenshot_path = tmp_path / f"{name}.png"
        page.screenshot(path=str(screenshot_path))
        print(f"\n  Screenshot saved: {screenshot_path}")

        html_path = tmp_path / f"{name}.html"
        html_path.write_text(page.content())
        print(f"  HTML saved: {html_path}")


def test_with_artifacts(artifact_page: Page):
    """Test that auto-saves artifacts if it fails."""
    artifact_page.goto(f"{BASE_URL}/login")
    assert artifact_page.locator("h2").text_content() == "Login Page"


# ============================================
# CI-FRIENDLY CONFTEST.PY
# ============================================
#
# # conftest.py
# import pytest
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Store test result for fixture access."""
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, f"rep_{rep.when}", rep)
#
#
# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     """Configure browser for CI."""
#     return {
#         **browser_type_launch_args,
#         "args": ["--disable-gpu", "--no-sandbox"],
#     }
#
#
# def pytest_collection_modifyitems(config, items):
#     """Auto-add markers based on file path."""
#     for item in items:
#         if "login" in item.nodeid:
#             item.add_marker(pytest.mark.login)
#         if "checkout" in item.nodeid:
#             item.add_marker(pytest.mark.checkout)


# ============================================
# RETRY ON FAILURE
# ============================================
#
# Install: pip install pytest-rerunfailures
#
# Run with retries:
#   pytest --reruns 2                    # Retry failed tests 2 times
#   pytest --reruns 2 --reruns-delay 5   # Retry with 5s delay
#
# Or mark specific flaky tests:
# @pytest.mark.flaky(reruns=3, reruns_delay=2)
# def test_flaky_network(page):
#     ...


def test_stable_test(page: Page):
    """A stable test that should pass on first run."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


# ============================================
# KEY POINTS:
#
# 1. Use GitHub Actions / GitLab CI for automated testing
# 2. Docker for consistent environment
# 3. pytest-xdist for parallel execution
# 4. Save artifacts (screenshots, traces) on failure
# 5. Use environment variables for configuration
# 6. Add --tracing retain-on-failure for CI
# 7. pytest-rerunfailures for flaky test handling
#
# Run: pytest 04_ci_cd_integration.py -v -s -m smoke
# ============================================
