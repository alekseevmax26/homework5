from selector.admin_page import AdminPage
from allure import title


@title("Наличие лого")
def test_check_name(browser, url):
    name = AdminPage(browser, url)
    name.open(url)
    name.check_name()


@title("Наличие поля username")
def test_check_username(browser, url):
    username = AdminPage(browser, url)
    username.open(url)
    username.check_username()


@title("Наличие поля password")
def test_check_password(browser, url):
    password = AdminPage(browser, url)
    password.open(url)
    password.check_password()


@title("Наличие кнопки login")
def test_check_login(browser, url):
    login = AdminPage(browser, url)
    login.open(url)
    login.check_login()


@title("Проверить наличие надписи")
def test_check_panel(browser, url):
    panel = AdminPage(browser, url)
    panel.open(url)
    panel.check_panel()
