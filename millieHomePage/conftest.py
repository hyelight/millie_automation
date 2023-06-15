from lib2to3.pgen2 import driver
from urllib import request
import pytest
from selenium import webdriver

driver = None

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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
     driver.get_screenshot_as_file(name)