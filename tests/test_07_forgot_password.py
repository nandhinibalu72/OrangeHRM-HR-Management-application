from playwright.sync_api import expect

LOGIN_LINK = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
RESET_USERNAME = "input[name='username']"
RESET_BUTTON = "button[type='submit']"

# The OrangeHRM demo redirects to a reset page and shows a toast or content text

def test_forgot_password_flow(page, base_url):
    page.goto(base_url)
    page.locator(LOGIN_LINK).click()
    expect(page.locator(RESET_USERNAME)).to_be_visible()
    page.fill(RESET_USERNAME, "Admin")
    page.locator(RESET_BUTTON).click()
    # success indicator (toast or message)
    expect(page.locator("div.oxd-text--toast-message, .orangehrm-card-container")).to_be_visible()
