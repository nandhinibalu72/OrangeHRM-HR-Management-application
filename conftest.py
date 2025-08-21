import os
import json
import time
import pytest
import allure
from playwright.sync_api import sync_playwright, Page, expect

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/")
LOGIN_PATH = "web/index.php/auth/login"

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # ✅ Force English locale and Accept-Language
        context = browser.new_context(
            locale="en-US",
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"}
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture()
def page(playwright_context) -> Page:
    page = playwright_context.new_page()
    # clear storage before navigation
    page.context.clear_cookies()
    page.add_init_script("localStorage.clear(); sessionStorage.clear();")
    yield page
    if hasattr(page, "last_test_failed") and page.last_test_failed:
        png = page.screenshot(full_page=True)
        allure.attach(
            png,
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    page.close()

# Auto-mark failure flag for screenshot handling
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        page = item.funcargs.get("page")
        if page:
            page.last_test_failed = rep.failed

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL.rstrip("/") + "/" + LOGIN_PATH

@pytest.fixture(scope="session")
def admin_creds():
    # OrangeHRM demo defaults
    return {"username": "Admin", "password": "admin123"}

@pytest.fixture(scope="session")
def new_user_data():
    # load from data/new_user.json if exists
    path = os.path.join("data", "new_user.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    # fallback data
    ts = int(time.time())
    return {
        "employee_name": "Lisa Andrews",
        "username": f"qa_user_{ts}",
        "password": "Passw0rd!",
        "role": "ESS",   # or "Admin"
        "status": "Enabled"
    }
