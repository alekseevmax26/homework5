from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class CardProductSelectors:
    name = (By.CSS_SELECTOR, "p:nth-child(1) > b")
    price = (By.CSS_SELECTOR, "h2:nth-child(1)")
    cart = (By.ID, "button-cart")
    reviews = (By.CSS_SELECTOR, "a:nth-child(6)")
    reviews_write = (By.CSS_SELECTOR, "h2:nth-child(2)")
    link = (By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")


class CardProduct(BasePage):

    def check_name(self):
        name = self.find_element(CardProductSelectors.name)
        return name

    def check_price(self):
        price = self.find_element(CardProductSelectors.price)
        return price

    def check_cart(self):
        cart = self.find_element(CardProductSelectors.cart)
        return cart

    def check_reviews(self):
        reviews = self.find_element(CardProductSelectors.reviews)
        return reviews

    def check_write_reviews(self):
        reviews_write = self.find_element(CardProductSelectors.reviews_write)
        return reviews_write

    def should_be_price(self):
        assert self.find_element(CardProductSelectors.price), '$602.00'

    def should_be_name(self):
        assert self.find_element(CardProductSelectors.name), 'Intel Core 2 Duo processor'

    def should_be_cart(self):
        assert self.find_element(CardProductSelectors.cart), 'Add to Cart'

    def should_be_reviews(self):
        assert self.find_element(CardProductSelectors.reviews), '0 reviews'

    def should_be_reviews_write(self):
        assert self.find_element(CardProductSelectors.reviews_write), 'Write a review'

    def open_link(self):
        link = self.find_element(CardProductSelectors.link)
        link.click()
