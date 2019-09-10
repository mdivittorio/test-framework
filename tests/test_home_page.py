from core.test import Test
from pages.home_page import HomePage


class TestHomePage(Test):

    @classmethod
    def setUpClass(cls):
        cls.driver = super().get_driver()
        HomePage(cls.driver).open()

    def test_submit_search(self):
        page = HomePage(self.driver)
        page.search_bar.send_keys('Something')
        page.submit_search.click()
