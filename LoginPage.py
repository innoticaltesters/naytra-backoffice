from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from Locators import *
import Users
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*LoginPageLocators.LOGO_IMAGE) else False


    def enter_email(self,user):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(Users.get_user(user)["email"])


    def enter_password(self,user):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(Users.get_user(user)["password"])


    def click_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()


    def login(self,user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_button()

    def login_with_valid_user(self,user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_invalid_user(self,user):
        self.login(user)
        time.sleep(3)
        return self.find_element(*LoginPageLocators.ERROR_USER_PASS).text

    def login_without_username(self,user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_USERNAME).text

    def login_without_password(self,user):
        self.login(user)
        time.sleep(5)
        return self.find_element(*LoginPageLocators.ERROR_PASSWORD).text

    def login_without_credentials(self,user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_USERNAME).text and self.find_element(*LoginPageLocators.ERROR_PASSWORD).text


class HomePage(Page):
    pass
