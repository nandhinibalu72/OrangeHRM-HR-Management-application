from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_fields_visible(page, base_url):
    lp = LoginPage(page)
    lp.open(base_url)
    expect(page.locator(lp.USERNAME)).to_be_visible()
    expect(page.locator(lp.PASSWORD)).to_be_visible()
    expect(page.locator(lp.LOGIN_BTN)).to_be_visible()
