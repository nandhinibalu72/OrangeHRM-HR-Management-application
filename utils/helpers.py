from playwright.sync_api import Page, expect

class Wait:
    @staticmethod
    def visible(page: Page, locator: str):
        expect(page.locator(locator)).to_be_visible()

    @staticmethod
    def clickable(page: Page, locator: str):
        # Playwright has no explicit clickable check; visibility + enabled is enough
        el = page.locator(locator)
        expect(el).to_be_visible()
        expect(el).to_be_enabled()
