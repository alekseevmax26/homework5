from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class LoginAdminSelector:
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

    def __init__(self, browser):
        super().__init__(browser)
        self.url = ("http://localhost/admin/")

    def open(self):
        self.browser.get(self.url)

    def login(self):
        login = self.find_element(LoginAdminSelector.login)
        login.send_keys("user")
        return login

    def password(self):
        password = self.find_element(LoginAdminSelector.password)
        password.send_keys("bitnami")
        return password

    def login_button(self):
        login_button = self.find_element(LoginAdminSelector.login_button)
        login_button.click()
        return login_button

    def catalog(self):
        catalog = self.find_element(LoginAdminSelector.catalog)
        catalog.click()
        return catalog

    def products(self):
        products = self.element_to_be_clickable(LoginAdminSelector.products)
        products.click()
        return products


class AddProduct(BasePage):

    def name_product(self):
        name_product = self.find_element(AddProductSelector.name_product)
        name_product.send_keys("123456789")
        return name_product

    def meta_teg(self):
        meta_teg = self.find_element(AddProductSelector.meta_teg)
        meta_teg.send_keys("123456789")
        return meta_teg

    def link_data(self):
        link_data = self.element_to_be_clickable(AddProductSelector.link_data)
        link_data.click()
        return link_data

    def model(self):
        model = self.find_element(AddProductSelector.model)
        model.send_keys("123456")
        return model

    def save(self):
        save = self.find_element(AddProductSelector.save)
        save.click()
        return save

    def add_new(self):
        add = self.find_element(AddProductSelector.add_new)
        add.click()
        return add


class DeleteProduct(BasePage):

    def delete(self):
        delete = self.find_element(DeleteProductSelector.delete)
        delete.click()
        return delete

    def assert_confirmation(self):
        alert = self.browser.switch_to_alert()\
            .accept()
        return alert
        
    def accept_product(self):
        accept_product = self.find_element(DeleteProductSelector.accept_product)
        accept_product.click()
        return accept_product

    def switch_to_alert(self):
        pass
