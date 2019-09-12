from pages.login_page import LoginPage


class TestLogin:

    def test_login(self, endevice):
        page = LoginPage(endevice)
        page.search("alibaba")