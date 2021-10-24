from selenium.webdriver.common.by import By
from selector.BasePage import BasePage
from allure import step


class LoginAdminSelector:
    POSTFIX_URL = "/admin"
    login = (By.ID, 'input-username')
    password = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, ".btn")
    catalog = (By.CSS_SELECTOR, "#menu-catalog > .parent")
    products = (By.XPATH, "//a[contains(text(),'Products')]")


class AddProductSelector:
    add_new = (By.XPATH, "//a[@data-original-title]")
    name_product = (By.ID, "input-name1")
    meta_teg = (By.ID, "input-meta-title1")
    link_data = (By.CSS_SELECTOR, ".nav-tabs>li:nth-child(2)>a")
    model = (By.ID, "input-model")
    save = (By.CSS_SELECTOR, ".fa-save")


class DeleteProductSelector:
    delete = (By.CSS_SELECTOR, ".btn-danger")
    accept_product = (By.CSS_SELECTOR, "tbody > tr:nth-child(1) input")


class Login(BasePage):

    def open(self, url):
        self.browser.get(url + LoginAdminSelector.POSTFIX_URL)

    @step("Ввод логина")
    def login(self):
        login = self.find_element_with_wait(LoginAdminSelector.login)
        login.send_keys("admin ")
        return login

    @step("Ввод пароля")
    def password(self):
        password = self.find_element_with_wait(LoginAdminSelector.password)
        password.send_keys("admin")
        return password

    @step("Нажатие кнопки Login")
    def login_button(self):
        login_button = self.find_element_with_wait(LoginAdminSelector.login_button)
        login_button.click()
        return login_button

    @step("Открыть каталоп")
    def catalog(self):
        catalog = self.find_element_with_wait(LoginAdminSelector.catalog)
        catalog.click()
        return catalog

    @step("Открыть продукты")
    def products(self):
        products = self.find_element_with_wait(LoginAdminSelector.products)
        products.click()
        return products


class AddProduct(BasePage):
    @step("Ввести имя продукта")
    def name_product(self):
        name_product = self.find_element_with_wait(AddProductSelector.name_product)
        name_product.send_keys("123456789")
        return name_product

    @step("Ввести метатег")
    def meta_teg(self):
        meta_teg = self.find_element_with_wait(AddProductSelector.meta_teg)
        meta_teg.send_keys("123456789")
        return meta_teg

    @step("Перейти на вкладку Data")
    def link_data(self):
        link_data = self.click_element(AddProductSelector.link_data)
        link_data.click()
        return link_data

    @step("Ввести модель")
    def model(self):
        model = self.find_element_with_wait(AddProductSelector.model)
        model.send_keys("123456")
        return model

    @step("Нажать сохранить")
    def save(self):
        save = self.find_element_with_wait(AddProductSelector.save)
        save.click()
        return save

    @step("Нажать на добавить")
    def add_new(self):
        add = self.find_element_with_wait(AddProductSelector.add_new)
        add.click()
        return add


class DeleteProduct(BasePage):
    @step("Нажать удалить")
    def delete(self):
        delete = self.find_element_with_wait(DeleteProductSelector.delete)
        delete.click()
        return delete

    @step("Переметиться в assert")
    def assert_confirmation(self):
        alert = self.browser.switch_to_alert()\
            .accept()
        return alert

    @step("Нажать принять")
    def accept_product(self):
        accept_product = self.find_element_with_wait(DeleteProductSelector.accept_product)
        accept_product.click()
        return accept_product

    def switch_to_alert(self):
        pass
