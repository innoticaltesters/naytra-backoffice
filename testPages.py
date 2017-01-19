import unittest
from selenium import webdriver
from LoginPage import *
from testCases import test_cases
from Locators import *
from selenium.webdriver.common.by import By
import time
chromepath ="/usr/local/lib/python3.5/site-packages/selenium/chromedriver"


class TestPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chromepath)
        self.driver.get('http://naytraangularadmin.sia.co.in/#/')


    def test_page_loaded(self):
        print("\n"+str(test_cases(0)))
        page = LoginPage(self.driver)
        self.assertTrue(page.check_page_loaded())


    def test_login_with_valid_user(self):
        print("\n"+str(test_cases(1)))
        mainPage = LoginPage(self.driver)
        login = mainPage.login_with_valid_user("valid_user")
        time.sleep(10)
        self.assertIn("/dashboard",login.get_url())


    def test_login_with_invalid_user(self):
        print("\n"+str(test_cases(2)))
        mainPage = LoginPage(self.driver)
        invalid_login = mainPage.login_with_invalid_user("invalid_user")
        self.assertEquals("Username or Password is Incorrect",invalid_login)


    def test_login_without_password(self):
        print("\n"+str(test_cases(3)))
        mainPage = LoginPage(self.driver)
        no_password = mainPage.login_without_password("pass_blank")
        time.sleep(5)
        self.assertEquals("password required",no_password)


    def test_login_without_username(self):

        print("\n"+str(test_cases(4)))
        mainPage = LoginPage(self.driver)
        no_username = mainPage.login_without_username("user_blank")
        time.sleep(5)
        self.assertEquals("Email Required",no_username)


    def test_without_user_pass(self):
        print("\n"+str(test_cases(5)))
        mainPage = LoginPage(self.driver)
        no_user_pass = mainPage.login_without_credentials("user_pass_blank")
        time.sleep(5)




    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

