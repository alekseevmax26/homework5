from selector.admin_page import AdminPage


def test_check_name(browser):
    name = AdminPage(browser)
    name.open()
    name.check_name()


def test_check_username(browser):
    username = AdminPage(browser)
    username.open()
    username.check_username()


def test_check_password(browser):
    password = AdminPage(browser)
    password.open()
    password.check_password()


def test_check_login(browser):
    login = AdminPage(browser)
    login.open()
    login.check_login()


def test_check_panel(browser):
    panel = AdminPage(browser)
    panel.open()
    panel.check_panel()
