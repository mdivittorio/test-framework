from core.test import Test
from pages.home_page import HomePage


class TestHomePage(Test):
    def test_submit_search(self):
        page = HomePage(self.driver)
        page.open()
        page.search_bar.send_keys('Something')
        page.submit_search.click()
