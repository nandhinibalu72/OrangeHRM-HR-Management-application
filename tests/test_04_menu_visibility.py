from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_menu_items_visible_clickable(page, base_url, admin_creds):
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    dash = DashboardPage(page)
    dash.is_loaded()
    expected_menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]
    dash.menu_visible_and_clickable(expected_menus)
