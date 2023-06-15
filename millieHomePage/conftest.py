from lib2to3.pgen2 import driver
from urllib import request
import pytest
from selenium import webdriver

# Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

# Options
from selenium.webdriver.chrome.options import Options

# DriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):
    
    global driver

    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == 'firefox':
        firefox_service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)

    elif browser_name == 'edge':
        edge_service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service)

    driver.implicitly_wait(5)

    driver.get('https://hyelight.github.io/millie/')
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.quit()