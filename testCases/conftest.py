from selenium import webdriver
import pytest


@pytest.fixture(params='b')
def set_up(request):

    if request.param == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    return driver
