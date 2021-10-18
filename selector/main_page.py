from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class MainPageSelectors:
    name = (By.CSS_SELECTOR, "h1 > a")
    cart = (By.ID, "cart-total")
    macbook = (By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")
    search = (By.CSS_SELECTOR, ".form-control")
    product = (By.CSS_SELECTOR, ".product-layout:nth-child(4) button:nth-child(2)")


class MainPage(BasePage):

    def check_name(self):
        check_name = self.find_element(MainPageSelectors.name)
        return check_name

    def check_cart(self):
        check_cart = self.find_element(MainPageSelectors.cart)
        return check_cart

    def check_macbook(self):
        check_macbook = self.find_element(MainPageSelectors.macbook)
        return check_macbook

    def check_search(self):
        check_search = self.find_element(MainPageSelectors.search)
        return check_search

    def check_product(self):
        check_product = self.find_element(MainPageSelectors.product)
        return check_product

    def should_be_search_name(self):
        assert self.element_to_be_clickable(MainPageSelectors.name), "Your Store"
        

