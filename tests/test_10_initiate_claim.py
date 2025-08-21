from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.claim_page import ClaimPage


def test_initiate_claim(page, base_url, admin_creds):
    LoginPage(page).open(base_url)
    LoginPage(page).login(admin_creds["username"], admin_creds["password"])
    DashboardPage(page).is_loaded()
    claim = ClaimPage(page)
    claim.open_my_claims()
    claim.create_claim(event_name="Accommodation", currency="Euro")
