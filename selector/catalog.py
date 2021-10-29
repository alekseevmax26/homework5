from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selector.BasePage import BasePage


class CatalogSelector:
    desctops = (By.XPATH, "p:nth-child(1) > b")
    mac = (By.XPATH, "//a[contains(text(),'Mac (1)')]")
    check_mac = (By.CSS_SELECTOR, "h2")
    components = (By.XPATH, "//a[contains(text(),'Components')]")
    monitors = (By.XPATH, "//a[contains(text(),'Monitors (2)')]")
    check_monitors = (By.CSS_SELECTOR, "h2")
    tablets = (By.XPATH, "//a[contains(text(),'Tablets')]")
    check_tablets = (By.CSS_SELECTOR, "h2")
    software = (By.XPATH, "//a[contains(text(),'Software')]")
    check_software = (By.CSS_SELECTOR, "h2")
    phones = (By.XPATH, "//a[contains(text(),'Phones & PDAs')]")
    check_phones = (By.CSS_SELECTOR, "h2")


class Catalog(BasePage):
    @step("Открыть дектоп")
    def check_desctop(self):
        desctop = self.find_element_with_wait(CatalogSelector.desctops)
        return desctop

    @step("Открыть mac")
    def check_mac(self):
        mac = self.find_element_with_wait(CatalogSelector.mac)
        return mac

    @step("Открыть компоненты")
    def check_components(self):
        components = self.find_element_with_wait(CatalogSelector.components)
        return components

    @step("Открыть мониторы")
    def check_monitors(self):
        monitors = self.find_element_with_wait(CatalogSelector.monitors)
        return monitors

    @step("Открыть планшеты")
    def check_tablets(self):
        tablets = self.find_element_with_wait(CatalogSelector.tablets)
        return tablets

    @step("Открыть ПО")
    def check_software(self):
        software = self.find_element_with_wait(CatalogSelector.software)
        return software

    @step("Открыть телефоны")
    def check_phone(self):
        phone = self.find_element_with_wait(CatalogSelector.phones)
        return phone

    @step("Наличие mac")
    def mac_check(self):
        mac_check = self.find_element_with_wait(CatalogSelector.check_mac)
        return mac_check

    @step("Наличие монитора")
    def monitors_check(self):
        monitors_check = self.find_element_with_wait(CatalogSelector.check_monitors)
        return monitors_check

    @step("Наличие планшетов")
    def tablets_check(self):
        tablets_check = self.find_element_with_wait(CatalogSelector.check_tablets)
        return tablets_check

    @step("Наличие software")
    def software_check(self):
        software_check = self.find_element_with_wait(CatalogSelector.check_software)
        return software_check

    @step("Наличие phones")
    def phones_check(self):
        phones_check = self.find_element_with_wait(CatalogSelector.check_phones)
        return phones_check
    