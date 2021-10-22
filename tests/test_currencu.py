from selector.change_currency import Currencu


def test_currencu(browser):
    currencu = Currencu(browser)
    currencu.go_to_site()
    currencu.change_btn()
    currencu.gbr()
