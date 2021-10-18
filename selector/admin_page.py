from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class AdminPageSelector:
    name = (By.CSS_SELECTOR, "img")
    username = (By.ID, "input-username")
    password = (By.ID, "input-password")
    login = (By.CSS_SELECTOR, ".btn")
    panel = (By.CSS_SELECTOR, ".panel-title")


class AdminPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = ("http://localhost/admin/")

    def check_name(self):
        name = self.find_element(AdminPageSelector.name)
        return name

    def check_username(self):
        username = self.find_element(AdminPageSelector.username)
        return username

    def check_password(self):
        password = self.find_element(AdminPageSelector.password)
        return password

    def check_login(self):
        login = self.find_element(AdminPageSelector.login)
        return login

    def check_panel(self):
        panel = self.find_element(AdminPageSelector.panel)
        return panel

    def open(self):
        self.browser.get(self.url)
