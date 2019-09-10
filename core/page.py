from abc import abstractmethod
from utils.utils import base_url


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url()

    @abstractmethod
    def open(self):
        pass



