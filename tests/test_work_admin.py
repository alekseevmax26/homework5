from selector.admin_selector import AddProduct
from selector.admin_selector import Login
from selector.admin_selector import DeleteProduct
from allure import title


@title("Добавить новый товар")
def test_add_product(browser, url):
    auth = Login(browser, url)
    auth.open(url)
    auth.login()
    auth.password()
    auth.login_button()
    auth.catalog()
    auth.products()
    add = AddProduct(browser, url)
    add.add_new()
    add.name_product()
    add.meta_teg()
    add.link_data()
    add.model()
    add.save()


@title("Удалить продукт")
def test_delete_product(browser, url, web_browser):
    auth = Login(browser, url)
    auth.open(url)
    auth.login()
    auth.password()
    auth.login_button()
    auth.catalog()
    auth.products()
    delete = DeleteProduct(browser, url)
    delete.accept_product()
    delete.delete()
    delete.assert_confirmation()
