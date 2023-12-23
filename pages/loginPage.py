from tests import BaseTest
import unittest
from selenium import webdriver


class BasePage(object):

    def __init__(self, driver, base_url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

class loginTest(unittest.TestCase, BaseTest):

    def __init__(self):
        self.driver = webdriver.Firefox







