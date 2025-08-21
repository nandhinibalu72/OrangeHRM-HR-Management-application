from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

def test_assign_leave(page, base_url, admin_creds):
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    DashboardPage(page).is_loaded()
    leave = LeavePage(page)
    leave.open_assign()
    leave.assign_leave(
        employee="adam kumar sahoo",
        leave_type="CAN - Bereavement",
        from_date="2025-08-21",
        to_date="2025-08-21",
        comment="Automation assignment"
    )
