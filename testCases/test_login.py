import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.extract_data import ReadConfig
from pageObjects.loginPage import Login


class TestLogin001:

    base_url = ReadConfig.get_url()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    username2 = ReadConfig.get_username2()
    password2 = ReadConfig.get_password2()

    def test_login1(self, set_up):
        driver = set_up
        driver.get(self.base_url)
        lp=Login(driver)
        lp.login(self.username1, self.password1)

    @pytest.mark.skip
    def test_login2(self, set_up):
        driver = set_up
        driver.get(self.base_url)
        lp = Login(driver)
        lp.login(self.username2, self.password2)
