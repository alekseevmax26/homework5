from selector.catalog import Catalog
from allure import title


@title("Проверить desctops")
def test_check_desctops(browser, url):
    decktops = Catalog(browser, url)
    decktops.open_browser()
    decktops.check_desctop()
    decktops.check_mac()
    decktops.mac_check()


@title("Проверить components")
def test_check_components(browser, url):
    components = Catalog(browser, url)
    components.open_browser()
    components.check_components()
    components.check_monitors()
    components.monitors_check()


@title("Проверить tablets")
def test_check_tablets(browser, url):
    tablets = Catalog(browser, url)
    tablets.open_browser()
    tablets.tablets_check()
    tablets.check_tablets()


@title("Проверить software")
def test_check_software(browser, url):
    software = Catalog(browser,url)
    software.open_browser()
    software.software_check()
    software.software_check()


@title("Проверить phone")
def test_check_phone(browser, url):
    phone = Catalog(browser, url)
    phone.open_browser()
    phone.check_phone()
    phone.phones_check()
