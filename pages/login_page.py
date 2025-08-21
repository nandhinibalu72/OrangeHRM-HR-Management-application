from playwright.sync_api import expect
from .base_page import BasePage

class LoginPage(BasePage):
    # New OrangeHRM v4 selectors
    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BTN = "button[type='submit']"
    ERROR = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]"

    def open(self, url: str):
        self.goto(url)
        expect(self.page.locator(self.USERNAME)).to_be_visible()

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.safe_click(self.LOGIN_BTN)

    def error_text(self):
        return self.page.locator(self.ERROR).inner_text(timeout=3000)
