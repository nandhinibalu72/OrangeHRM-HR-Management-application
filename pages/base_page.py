from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def safe_click(self, selector: str):
        el = self.page.locator(selector)
        expect(el).to_be_visible()
        expect(el).to_be_enabled()
        el.click()

    def fill(self, selector: str, text: str):
        el = self.page.locator(selector)
        expect(el).to_be_visible()
        el.fill(text)

    def goto(self, url: str):
        self.page.goto(url)
