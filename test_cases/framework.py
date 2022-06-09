import os
import time
import unittest

from selenium import webdriver

import pages.login_page
from pages import base_page
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

# Jedno pierwszych zadań poradzić sobie z błędem: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def test_log_in_to_the_system(self):
        os.chmod(DRIVER_PATH, 755)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get('https://scouts-test.futbolkolektyw.pl/en')
        driver.fullscreen_window()
        driver.implicitly_wait(IMPLICITLY_WAIT)


        email = 'pati.it.qa@gmail.com'
        password = 'Test-1234'
        scout_login = pages.login_page.LoginPage(driver)
        scout_login.type_in_email(email, password)


