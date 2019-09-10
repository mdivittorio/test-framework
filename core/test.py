from unittest import TestCase
from selenium.webdriver.chrome import webdriver
from utils.utils import browser


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.get_driver()

    @staticmethod
    def get_driver() -> webdriver.WebDriver:
        if browser().lower() == 'chrome':
            driver = 'chromedriver'
        else:
            raise NotImplemented(f'Browser {browser} not supported.')
        return webdriver.WebDriver(executable_path=f'../drivers/{driver}')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
