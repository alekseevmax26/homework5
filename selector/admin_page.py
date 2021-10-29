from allure import step
from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class AdminPageSelector:
    POSTFIX_URL = "/admin"
    name = (By.CSS_SELECTOR, "img")
    username = (By.ID, "input-username")
    password = (By.ID, "input-password")
    login = (By.CSS_SELECTOR, ".btn")
    panel = (By.CSS_SELECTOR, ".panel-title")


class AdminPage(BasePage):

    def open(self, url):
        self.browser.get(url + AdminPageSelector.POSTFIX_URL)

    @step("Проверка заголовка")
    def check_name(self):
        name = self.find_element_with_wait(AdminPageSelector.name)
        return name

    @step("Проверка поля username")
    def check_username(self):
        username = self.find_element_with_wait(AdminPageSelector.username)
        return username

    @step("Проверка поля password")
    def check_password(self):
        password = self.find_element_with_wait(AdminPageSelector.password)
        return password

    @step("Проверка кнопки login")
    def check_login(self):
        login = self.find_element_with_wait(AdminPageSelector.login)
        return login

    @step("Проверка наличии надписи")
    def check_panel(self):
        panel = self.find_element_with_wait(AdminPageSelector.panel)
        return panel
