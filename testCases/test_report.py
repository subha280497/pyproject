import pytest
from selenium.webdriver.common.by import By

from Utilities.driver_utilities import WaitActions
from Utilities.extract_data import ReadConfig
from pageObjects.loginPage import Login


@pytest.mark.smoke
def test_report(driver):
    """This function will test the report button"""
    driver.find_element(By.ID, 'container_reports').click()
    assert "Reports Dashboard" in driver.title

@pytest.mark.regression
def test_users(driver):
    """This function will test the user button"""
    driver.find_element(By.ID, 'container_users').click()
    assert "User List" in driver.title


# @pytest.mark.usefixtures("set_up_class")
# class BaseClass:
#     pass
#
# class TestInLogin(BaseClass):
#
#     base_url = ReadConfig.get_url()
#     username1 = ReadConfig.get_username1()
#     password1 = ReadConfig.get_password1()
#     username2 = ReadConfig.get_username2()
#     password2 = ReadConfig.get_password2()
#
#
