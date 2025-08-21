from playwright.sync_api import expect
from .base_page import BasePage

class LeavePage(BasePage):
    MENU = "//span[normalize-space()='Leave']"
    ASSIGN_LEAVE = "a:has-text('Assign Leave')"
    EMPLOYEE = "input[placeholder='Type for hints...']"
    LEAVE_TYPE = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    FROM_DATE = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    TO_DATE = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    COMMENT = "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    ASSIGN_BTN = "//button[normalize-space()='Assign']"

    def open_assign(self):
        self.safe_click(self.MENU)
        self.safe_click(self.ASSIGN_LEAVE)
        expect(self.page.locator(self.EMPLOYEE)).to_be_visible()

    def assign_leave(self, employee: str, leave_type: str, from_date: str, to_date: str, comment: str = ""):
        self.fill(self.EMPLOYEE, employee)
        self.page.locator("//div[@role='listbox']//span").first.click()
        self.safe_click(self.LEAVE_TYPE)
        self.safe_click(f"//div[@role='listbox']//span[text()='{leave_type}']")
        self.fill(self.FROM_DATE, from_date)
        if comment:
            self.fill(self.COMMENT, comment)
        self.safe_click(self.ASSIGN_BTN)
        modal = self.page.locator("//div[@role='document']")
        expect(modal).to_be_visible()
        self.safe_click("//button[normalize-space()='Ok']")
        expect(self.page.locator("div.oxd-toast")).to_be_visible()
