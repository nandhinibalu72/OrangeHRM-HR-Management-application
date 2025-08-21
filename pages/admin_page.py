from playwright.sync_api import expect
from .base_page import BasePage

class AdminPage(BasePage):
    ADMIN_MENU = "//span[normalize-space()='Admin']"
    ADD_BUTTON = "//button[normalize-space()='Add']"
    SAVE_BUTTON = "(//button[normalize-space()='Save'])[1]"
    SEARCH_BUTTON = "button:has-text('Search')"

    # Add User form fields
    ROLE_DROPDOWN = "(//i)[11]"
    EMPLOYEE_NAME = "(//input[@placeholder='Type for hints...'])[1]"
    STATUS_DROPDOWN = "(//div[@class='oxd-select-text--after'])[2]"
    USERNAME = "(//input[@class='oxd-input oxd-input--active'])[2]"
    PASSWORD = "(//input[@type='password'])[1]"
    CONFIRM_PASSWORD = "(//input[@type='password'])[2]"

    # Search fields
    SEARCH_USERNAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"

    TABLE_ROWS = "div.oxd-table-body div.oxd-table-card"

    def open_admin(self):
        self.safe_click(self.ADMIN_MENU)
        expect(self.page.locator(self.ADD_BUTTON)).to_be_visible()

    def add_user(self, employee_name: str, username: str, password: str, role: str = "ESS", status: str = "Enabled"):
        self.safe_click(self.ADD_BUTTON)
        # Role
        self.safe_click(self.ROLE_DROPDOWN)
        self.safe_click(f"//div[@role='listbox']//span[text()='{role}']")
        # Employee Name (autocomplete)
        self.fill(self.EMPLOYEE_NAME, employee_name)
        self.page.locator("//div[@role='listbox']//span").first.click()
        # Status
        self.safe_click(self.STATUS_DROPDOWN)
        self.safe_click(f"//div[@role='listbox']//span[text()='{status}']")
        # Username & Password
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.fill(self.CONFIRM_PASSWORD, password)
        self.safe_click(self.SAVE_BUTTON)
        # Wait for table or toast
        expect(self.page.locator("div.oxd-toast")).to_be_visible()

    def search_user(self, username: str) -> bool:
        self.page.locator(self.SEARCH_USERNAME).clear()
        self.fill(self.SEARCH_USERNAME, username)
        self.safe_click(self.SEARCH_BUTTON)
        rows = self.page.locator(self.TABLE_ROWS)
        rows.first.wait_for(state="visible")
        texts = rows.all_inner_texts()
        return any(username in t for t in texts)
