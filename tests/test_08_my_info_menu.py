from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def test_my_info_submenus(page, base_url, admin_creds):
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    DashboardPage(page).is_loaded()
    my = MyInfoPage(page)
    my.open()
    sub_items = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary",
        "Qualifications",
        "Memberships"
    ]
    my.verify_submenus(sub_items)
