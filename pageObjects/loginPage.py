from selenium.webdriver.common.by import By
from selenium import webdriver



class Login:

    username_tbx = (By.ID, 'username')
    password_tbx = (By.NAME, 'pwd')
    login_btn = (By.ID, 'loginButton')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_tbx).send_keys(username)
        self.driver.find_element(*self.password_tbx).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

