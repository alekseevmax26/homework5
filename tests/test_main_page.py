from selector.main_page import MainPage
from allure import title


@title("Наличие логотипа")
def test_check_name(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_name()
    main.should_be_search_name()


@title("Наличие корзины")
def test_check_cart(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_cart()


@title("Наличие кнопки корзина")
def test_check_macbook(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_macbook()


@title("Наличие поиска")
def test_check_search(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_search()


@title("Наличие продукта")
def test_check_product(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_product()
