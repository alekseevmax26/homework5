from selector.admin_selector import AddProduct
from selector.admin_selector import Login
from selector.admin_selector import DeleteProduct


def test_add_product(browser):
    auth = Login(browser)
    auth.open()
    auth.login()
    auth.password()
    auth.login_button()
    auth.catalog()
    auth.products()
    add = AddProduct(browser)
    add.add_new()
    add.name_product()
    add.meta_teg()
    add.link_data()
    add.model()
    add.save()


def test_delete_product(browser):
    auth = Login(browser)
    auth.open()
    auth.login()
    auth.password()
    auth.login_button()
    auth.catalog()
    auth.products()
    delete = DeleteProduct(browser)
    delete.accept_product()
    delete.delete()
    delete.assert_confirmation()
