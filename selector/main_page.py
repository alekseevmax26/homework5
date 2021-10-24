from selenium.webdriver.common.by import By
from selector.BasePage import BasePage
from allure import step


class MainPageSelectors:
    name = (By.CSS_SELECTOR, "#logo .img-responsive")
    cart = (By.ID, "cart-total")
    macbook = (By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")
    search = (By.CSS_SELECTOR, ".form-control")
    product = (By.CSS_SELECTOR, ".product-layout:nth-child(4) button:nth-child(2)")


class MainPage(BasePage):
    @step("Проверка лого")
    def check_name(self):
        check_name = self.find_element_with_wait(MainPageSelectors.name)
        return check_name

    @step("Кнопка корзины")
    def check_cart(self):
        check_cart = self.find_element_with_wait(MainPageSelectors.cart)
        return check_cart

    @step("Наименование товара")
    def check_macbook(self):
        check_macbook = self.find_element_with_wait(MainPageSelectors.macbook)
        return check_macbook

    @step("Поиск")
    def check_search(self):
        check_search = self.find_element_with_wait(MainPageSelectors.search)
        return check_search

    @step("Наличие кнопки продукт")
    def check_product(self):
        check_product = self.find_element_with_wait(MainPageSelectors.product)
        return check_product

    def should_be_search_name(self):
        assert self.find_element_with_wait_clickable(MainPageSelectors.name), "Your Store"
        

