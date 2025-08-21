from playwright.sync_api import expect
from .base_page import BasePage


class MyInfoPage(BasePage):
    MENU = "//span[normalize-space()='My Info']"
    # Submenu item (corrected XPath)
    SUB_ITEM = lambda self, name: f"//a[normalize-space()='{name}']"

    def open(self):
        self.safe_click(self.MENU)
        expect(self.page.locator("h6:has-text('Personal Details')")).to_be_visible()

    def verify_submenus(self, names):
        for n in names:
            loc = self.page.locator(self.SUB_ITEM(n))
            expect(loc).to_be_visible()
            loc.click()
            # Verify page header changes after click
            expect(self.page.locator(f"h6:has-text('{n}')")).to_be_visible()
