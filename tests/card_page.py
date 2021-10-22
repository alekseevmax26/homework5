from selector.card_priduct import CardProduct

link = "http://localhost/index.php?route=product/product&product_id=43"


def test_check_name(browser, ):
    name = CardProduct(browser)
    name.go_to_site()
    name.open_link()
    name.check_name()
    name.should_be_name()


def test_check_price(browser):
    price = CardProduct(browser)
    price.go_to_site()
    price.open_link()
    price.check_price()
    price.should_be_price()


def test_check_cart(browser):
    cart = CardProduct(browser)
    cart.go_to_site()
    cart.open_link()
    cart.check_cart()
    cart.should_be_cart()


def test_check_reviews(browser):
    reviews = CardProduct(browser)
    reviews.go_to_site()
    reviews.open_link()
    reviews.check_reviews()
    reviews.should_be_reviews()


def test_check_reviews_write(browser):
    reviews_write = CardProduct(browser)
    reviews_write.open_link()
    reviews_write.check_write_reviews()
    reviews_write.should_be_reviews_write()
