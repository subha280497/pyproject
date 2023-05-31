from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import *


class WaitActions:
    def __init__(self, driver):
        self.driver=driver

    def wait_till_url_changes(self, current_url):
        wait=WebDriverWait(self.driver, 50)
        wait.until(expected_conditions.url_changes(current_url))
