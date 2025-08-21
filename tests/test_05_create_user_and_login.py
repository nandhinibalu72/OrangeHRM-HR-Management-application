from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

def test_create_user_and_login(page, base_url, admin_creds, new_user_data):
    # Admin login
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    dash = DashboardPage(page)
    dash.is_loaded()

    # Add user
    admin = AdminPage(page)
    admin.open_admin()
    admin.add_user(
        employee_name=new_user_data["employee_name"],
        username=new_user_data["username"],
        password=new_user_data["password"],
        role=new_user_data["role"],
        status=new_user_data["status"],
    )

    # Logout and login as new user
    dash.logout()
    LoginPage(page).open(base_url)
    LoginPage(page).login(new_user_data["username"], new_user_data["password"])
    DashboardPage(page).is_loaded()
