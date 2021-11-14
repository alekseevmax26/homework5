import pytest
import logging
import os

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


logging.basicConfig(level=logging.INFO, filename="../selenium.log")
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption('--url', action='store', default='https://demo.opencart.com')
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--executor", action="store", default="192.168.0.103")
    parser.addoption("--bversion", action="store", default="94.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))

  
@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    fp = webdriver.FirefoxProfile()
    drivers = request.config.getoption("--drivers")
    logger.info(f"Run browser {browser_name}")
    if executor == "localhost":
        capabilities = {'goog:chromeOptions': {}}

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(options=options, desired_capabilities=capabilities,
                                      executable_path=drivers + "/chromedriver")
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options, firefox_profile=fp, executable_path=drivers + "/geckodriver")
        elif browser_name == "opera":
            options = OperaOptions()
            driver = webdriver.Opera(options=options, desired_capabilities=capabilities,
                                     executable_path=drivers + "/operadriver")
        elif browser_name == "yandex":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(options=options, desired_capabilities=capabilities)
        else:
            raise pytest.UsageError("--browser_name should be chrome, firefox, opera, yandex")

        if maximized:
            driver.maximize_window()
    else:
        executor_url = f"{executor}"

        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "name": "test_opencart",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )

        driver.maximize_window()

    def final():
        logger.info(f"Browser {browser_name} close")
        driver.quit()

    request.addfinalizer(final)
    return driver
