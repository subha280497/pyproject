import os.path

import pytest_html
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Utilities.driver_utilities import WaitActions
from Utilities.extract_data import ReadConfig
from pageObjects.loginPage import Login

base_url = ReadConfig.get_url()
username1 = ReadConfig.get_username1()
password1 = ReadConfig.get_password1()
username2 = ReadConfig.get_username2()
password2 = ReadConfig.get_password2()


# @pytest.fixture(params='y')
# def set_up_method(request):
#     if request.param == 'edge':
#         driver = webdriver.Edge()
#     else:
#         driver = webdriver.Chrome()
#
#     return driver



@pytest.fixture(scope='session', autouse=True, params=("ch", "ed"))
def driver(request):
    print("test stated")
    global web_driver
    if request.param == "ch":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        web_driver = webdriver.Chrome(options=options)

    elif request.param == "ed":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        web_driver = webdriver.Edge(options=options)

    yield web_driver
    web_driver.quit()

    print("test ended")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--headless")

@pytest.fixture(scope="class")
def run_headless(request):
    request.config.getoption("--headless")






@pytest.fixture(scope='class')
def set_up_class(request, browser='chrome', run_headless=None):
    global web_driver
    if browser=='edge':
        options = webdriver.EdgeOptions()
        if run_headless==True:
            options.add_argument("--headless=new")
        web_driver = webdriver.Edge(options=options)
    else:
        options = webdriver.ChromeOptions()
        if run_headless==True:
            options.add_argument("--headless=new")
        web_driver = webdriver.Chrome(options=options)
    request.cls.driver = web_driver
    return web_driver


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url(base_url))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = report.nodeid.replace("::","-").replace("testCases/", "").replace(".py","")+".png"
#             # destination_file = os.path.join(report_directory, file_name)
#
#             web_driver.save_screenshot("Reports\\ScreenShots\\"+str(file_name))
#             print(file_name)
#             if file_name:
#                 destination_file=".\\ScreenShots\\"+str(file_name)
#                 html = "<div><img src='%s' alt='screenshot' style='width:300px; height=200px' onclick='window.open(this.src)' align='right'/></div>"%destination_file
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra


@pytest.hookimpl()
def pytest_html_report_title(report):
    report.title = "actitime report by subha"



@pytest.fixture(scope='function', autouse=True)
def login(driver):
    driver.implicitly_wait(10)
    driver.get(base_url)
    current_url = driver.current_url
    lp = Login(driver)
    lp.login(username1, password1)
    wa = WaitActions(driver)
    wa.wait_till_url_changes(current_url)
    assert 'Enter Time-Track' in driver.title
    yield
    driver.find_element(By.ID, 'logoutLink').click()
