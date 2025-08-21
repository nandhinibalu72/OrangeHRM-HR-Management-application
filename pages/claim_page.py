from playwright.sync_api import expect
from .base_page import BasePage

class ClaimPage(BasePage):
    MENU = "//span[normalize-space()='Claim']"
    ASSIGN = "a:has-text('My Claims')"
    ADD_BTN = "//a[normalize-space()='Submit Claim']"
    EVENT_DROPDOWN = "(//div[@class='oxd-select-wrapper'])[1]"
    CURRENCY_DROPDOWN = "(//div[@class='oxd-select-wrapper'])[2]"
    SAVE_BTN = "//button[normalize-space()='Create']"

    def open_my_claims(self):
        """Navigate to My Claims page"""
        self.safe_click(self.MENU)
        self.safe_click(self.ASSIGN)
        expect(self.page.locator(self.ADD_BTN)).to_be_visible()

    def create_claim(self, event_name: str = "Accommodation", currency: str = "Euro"):
        """Create a new claim with given event and currency"""
        self.safe_click(self.ADD_BTN)

        # --- Event dropdown ---
        self.safe_click(self.EVENT_DROPDOWN)
        # exact match on event
        self.safe_click(f"//div[@role='listbox']//span[normalize-space()='{event_name}']")

        # --- Currency dropdown ---
        self.safe_click(self.CURRENCY_DROPDOWN)
        # flexible match: allows 'Euro', 'USD', or 'United States Dollar'
        self.safe_click(f"//div[@role='listbox']//span[contains(normalize-space(), '{currency}')]")

        # --- Save Claim ---
        self.safe_click(self.SAVE_BTN)
        expect(self.page.locator('div.oxd-toast')).to_be_visible()