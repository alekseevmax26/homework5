from selector.new_user import NewUser


def test_new_user(browser):
    newuser = NewUser(browser)
    newuser.go_to_site()
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
