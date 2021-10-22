from selector.catalog import Catalog


def test_check_desctops(browser):
    decktops = Catalog(browser)
    decktops.go_to_site()
    decktops.check_desctop()
    decktops.check_mac()
    decktops.mac_check()


def test_check_components(browser):
    components = Catalog(browser)
    components.go_to_site()
    components.check_components()
    components.check_monitors()
    components.monitors_check()


def test_check_tablets(browser):
    tablets = Catalog(browser)
    tablets.go_to_site()
    tablets.tablets_check()
    tablets.check_tablets()


def test_check_software(browser):
    software = Catalog(browser)
    software.go_to_site()
    software.software_check()
    software.software_check()


def test_check_phone(browser):
    phone = Catalog(browser)
    phone.go_to_site()
    phone.check_phone()
    phone.phones_check()
