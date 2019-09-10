from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element(WebElement):
    TIMEOUT = 10

    def __init__(self, locator, driver, id_=None):
        super().__init__(driver, id_)
        self._element = None
        self.by = Element.get_by(locator)

    def wait_for_element(self, timeout=TIMEOUT):
        try:
            WebDriverWait(self._parent, timeout).until(EC.presence_of_element_located(self.by))
            self._element = self._parent.find_element(*self.by)
        except TimeoutException:
            raise TimeoutException(f'Element with locator <<{self.by[1]}>> not found after {timeout} seconds.')

    def wait_for_enabled(self, timeout=TIMEOUT):
        try:
            WebDriverWait(self._parent, timeout).until(EC.element_to_be_clickable(self.by))
        except TimeoutException:
            raise TimeoutException(f'Element with locator <<{self.by[1]}>> not enabled within {timeout} seconds.')

    def send_keys(self, value):
        self.wait_for_element()
        self._element.send_keys(value)

    def click(self):
        self.wait_for_element()
        self.wait_for_enabled()
        self._element.click()

    @classmethod
    def get_by(cls, locator):
        loc = locator.split('=', 1)
        if 'xpath' == loc[0]:
            new_by = By.XPATH
        elif 'id' == loc[0]:
            new_by = By.ID
        elif 'css' == loc[0]:
            new_by = By.CSS_SELECTOR
        else:
            raise NotImplemented(f'Element By {loc[0]} not supported.')
        return new_by, loc[1]
