from playwright.sync_api import expect
from .base_page import BasePage

class DashboardPage(BasePage):
    # Sidebar menu items by role
    MENU_ITEM = lambda self, name: f"nav >> role=link[name='{name}']"
    
    # Avatar dropdown (top right)
    AVATAR_DROPDOWN = "(//span[@class='oxd-userdropdown-tab'])[1]"  # safer than CSS if possible
    
    # Logout link
    LOGOUT = "role=menuitem[name='Logout']"
    
    # Dashboard header (entire sidebar menu area)
    DASHBOARD_HEADER = "nav[aria-label='Sidepanel']"

    def is_loaded(self):
        expect(self.page.locator(self.DASHBOARD_HEADER)).to_be_visible()

    def menu_visible_and_clickable(self, names):
        for n in names:
            loc = self.page.locator(self.MENU_ITEM(n))
            expect(loc).to_be_visible()
            expect(loc).to_be_enabled()

    def open_menu(self, name):
        self.safe_click(self.MENU_ITEM(name))

    def logout(self):
        self.safe_click(self.AVATAR_DROPDOWN)
        self.safe_click(self.LOGOUT)
