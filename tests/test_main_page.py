from selector.main_page import MainPage


def test_check_name(browser):
    main = MainPage(browser)
    main.go_to_site()
    main.check_name()
    main.should_be_search_name()


def test_check_cart(browser):
    main = MainPage(browser)
    main.go_to_site()
    main.check_cart()


def test_check_macbook(browser):
    main = MainPage(browser)
    main.go_to_site()
    main.check_macbook()


def test_check_search(browser):
    main = MainPage(browser)
    main.go_to_site()
    main.check_search()


def test_check_product(browser):
    main = MainPage(browser)
    main.go_to_site()
    main.check_product()
