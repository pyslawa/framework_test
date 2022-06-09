import os
import sys
import unittest
import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SYSTEM = sys.platform
PATH_TO_PROJECT = os.path.dirname(os.path.abspath(__file__))

if SYSTEM == 'win32':
    CHROME_DRIVER = "chromedriver.exe"
else:
    CHROME_DRIVER = "chromedriver"

DRIVER_PATH = os.path.join(PATH_TO_PROJECT, '../drivers', CHROME_DRIVER)
IMPLICITLY_WAIT = 3
EXPLICITLY_WAIT = 30

DEFAULT_LOCATOR_TYPE = By.XPATH


UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

if SYSTEM == 'windows':
    CHROME_DRIVER = 'chromedriver.exe'
    FIREFOX_DRIVER = 'geckodriver.exe'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
else:
    CHROME_DRIVER = 'chromedriver'
    FIREFOX_DRIVER = 'geckodriver'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'


# class MainTest(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     @classmethod
#     def setUpClass(self):
#         self.driver_service = Service(executable_path=r"/drivers\chromedriver.exe")
#         # self.driver_service = Service(executable_path=ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=self.driver_service)
#
#     def test_tittle(self):
#         self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
#         title = self.driver.title
#         print(f"Actual title: " + title)
#         assert 'Scouts panel - sign in' == title
#
#     def tearDown(self):
#         pass
#
#     @classmethod
#     def tearDownClass(self):
#         self.driver.quit()

