
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "http://localhost"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def element_to_be_clickable(self, locator, time=30):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.browser.get(self.base_url)


