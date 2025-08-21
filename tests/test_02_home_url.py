from pages.login_page import LoginPage

def test_home_url_accessible(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
