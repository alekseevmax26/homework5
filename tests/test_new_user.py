from selector.new_user import NewUser
from allure import title


@title("Создание нового пользователя")
def test_new_user(browser, url):
    newuser = NewUser(browser, url)
    newuser.open_browser()
    newuser.my_account()
    newuser.link_register()
    newuser.first_name()
    newuser.last_name()
    newuser.email()
    newuser.telephone()
    newuser.password()
    newuser.confirm()
    newuser.privacy()
    newuser.confirm_btn()
