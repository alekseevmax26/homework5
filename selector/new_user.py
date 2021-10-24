from selenium.webdriver.common.by import By
from allure import step, attach
from selector.BasePage import BasePage


class NewUserSelector:
    my_account = (By.CSS_SELECTOR, ".caret")
    link_register = (By.CSS_SELECTOR, ".dropdown-menu>li:nth-child(1)>a")
    firstname = (By.ID, "input-firstname")
    lastname = (By.ID, "input-lastname")
    email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    password = (By.ID, "input-password")
    confirm = (By.ID, "input-confirm")
    privacy = (By.CSS_SELECTOR, ".pull-right>input:nth-child(2)")
    continue_btn = (By.CSS_SELECTOR, ".btn-primary")


class NewUser(BasePage):
    @step("Нажать кнопку добавления аккаунта")
    def my_account(self):
        my_account = self.find_element_with_wait(NewUserSelector.my_account)
        my_account.click()
        return my_account

    @step("Нажать регистрацию")
    def link_register(self):
        link_register = self.find_element_with_wait(NewUserSelector.link_register)
        link_register.click()
        return link_register

    @step("Ввести имя")
    def first_name(self):
        first_name = self.find_element_with_wait_clickable(NewUserSelector.firstname)
        first_name.send_keys("Maxim")
        return first_name

    @step("Ввести фамилию")
    def last_name(self):
        last_name = self.find_element_with_wait(NewUserSelector.lastname)
        last_name.send_keys("Abvgd")
        return last_name

    @step("Ввести почту")
    def email(self):
        email = self.find_element_with_wait(NewUserSelector.email)
        email.send_keys("test@mail.ru")
        return email

    @step("Ввести телефон")
    def telephone(self):
        telephone = self.find_element_with_wait(NewUserSelector.telephone)
        telephone.send_keys("+79281234567")
        return telephone

    @step("Ввести пароль")
    def password(self):
        password = self.find_element_with_wait(NewUserSelector.password)
        password.send_keys("123456789")
        return password

    @step("Подтвердить пароль")
    def confirm(self):
        confirm = self.find_element_with_wait(NewUserSelector.confirm)
        confirm.send_keys("123456789")
        return confirm

    @step("Нажать на принять условия")
    def privacy(self):
        privacy = self.find_element_with_wait(NewUserSelector.privacy)
        privacy.click()
        return privacy

    @step("Нажать кнопку принять")
    def confirm_btn(self):
        confirm_btn = self.find_element_with_wait(NewUserSelector.continue_btn)
        confirm_btn.click()
        return confirm_btn
