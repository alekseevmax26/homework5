from selector.change_currency import Currencu
from allure import title


@title("Смена валюты")
def test_currencu(browser, url):
    currencu = Currencu(browser, url)
    currencu.open_browser()
    currencu.change_btn()
    currencu.gbr()
