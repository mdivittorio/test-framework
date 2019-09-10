from unittest import TestCase
from selenium.webdriver.chrome import webdriver


class Test(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.WebDriver(executable_path='../drivers/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
