import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.driver_utilities import WaitActions
from Utilities.extract_data import ReadConfig


base_url = ReadConfig.get_url()
username1 = ReadConfig.get_username1()
password1 = ReadConfig.get_password1()
username2 = ReadConfig.get_username2()
password2 = ReadConfig.get_password2()

@pytest.mark.smoke
@pytest.mark.regression
def test_task(driver):
    driver.find_element(By.ID, 'container_tasks').click()
    assert "Task List" in driver.title


# @pytest.mark.usefixtures("set_up_class")
# class BaseClass:
#     pass
#
# class TestLogin(BaseClass):
#
#     base_url = ReadConfig.get_url()
#     username1 = ReadConfig.get_username1()
#     password1 = ReadConfig.get_password1()
#     username2 = ReadConfig.get_username2()
#     password2 = ReadConfig.get_password2()
#
#
#
#         # driver = set_up
#         # driver.get(self.base_url)
#         # lp = Login(driver)
#         # lp.login(self.username2, self.password2)
#         # assert driver.title == 'actiTIME -  Enter Time-Track'
#
#     def test_task(self, login):
#         driver = self.driver
#         driver.find_element(By.ID, 'container_tasks').click()
#         assert "Task List89" in driver.title
#
#     def test_reports(self, login):
#         driver = self.driver
#         driver.find_element(By.ID, 'container_reports').click()
#         assert "Reports Dashboard" in driver.title

