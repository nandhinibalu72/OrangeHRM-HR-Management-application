import pytest
from utils.data_loader import csv_records
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.ddt
@pytest.mark.parametrize("row", csv_records("data/login_data.csv"))
def test_login_data_driven(page, base_url, row):
    login = LoginPage(page)
    login.open(base_url)
    login.login(row["username"], row["password"])
    if row["expected"] == "success":
        dash = DashboardPage(page)
        dash.is_loaded()
        dash.logout()
    else:
        assert "Invalid" in login.error_text()
