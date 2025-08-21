from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

def test_verify_new_user_in_admin_list(page, base_url, admin_creds, new_user_data):
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    DashboardPage(page).is_loaded()
    admin = AdminPage(page)
    admin.open_admin()
    assert admin.search_user(new_user_data["username"]) is True
