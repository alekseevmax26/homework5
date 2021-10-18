from selenium.webdriver.common.by import By

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
    def my_account(self):
        my_account = self.find_element(NewUserSelector.my_account)
        my_account.click()
        return my_account

    def link_register(self):
        link_register = self.find_element(NewUserSelector.link_register)
        link_register.click()
        return link_register

    def first_name(self):
        first_name = self.element_to_be_clickable(NewUserSelector.firstname)
        first_name.send_keys("Maxim")
        return first_name

    def last_name(self):
        last_name = self.find_element(NewUserSelector.lastname)
        last_name.send_keys("Abvgd")
        return last_name

    def email(self):
        email = self.find_element(NewUserSelector.email)
        email.send_keys("test@mail.ru")
        return email

    def telephone(self):
        telephone = self.find_element(NewUserSelector.telephone)
        telephone.send_keys("+79281234567")
        return telephone

    def password(self):
        password = self.find_element(NewUserSelector.password)
        password.send_keys("123456789")
        return password

    def confirm(self):
        confirm = self.find_element(NewUserSelector.confirm)
        confirm.send_keys("123456789")
        return confirm

    def privacy(self):
        privacy = self.find_element(NewUserSelector.privacy)
        privacy.click()
        return privacy

    def confirm_btn(self):
        confirm_btn = self.find_element(NewUserSelector.continue_btn)
        confirm_btn.click()
        return confirm_btn
