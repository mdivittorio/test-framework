from core.page import Page
from core.element import Element


class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = Element('id=search_query_top', self.driver)
        self.submit_search = Element('css=button[name=submit_search]', self.driver)

    def open(self):
        self.driver.get(self.base_url)
