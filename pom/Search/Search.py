from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from base.seleniumfind import SeleniumFind


class SearchLocators:
    LOCATOR_SEARCH_BUTTON_BY_CLASS_NAME: str = 'search__button'
    LOCATOR_SEARCH_INPUT_BY_CLASS_NAME: str = 'search__input'
    LOCATOR_SEARCH_RESULTS_BY_CLASS_NAME: str = 'drinks__link'


class SearchSteps(SeleniumFind):
    def __init__(self, driver):
        SeleniumFind.__init__(self)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_search_element(self) -> WebElement:
        return self.is_visible('class_name', SearchLocators.LOCATOR_SEARCH_BUTTON_BY_CLASS_NAME)

    def get_search_input_element(self) -> WebElement:
        return self.is_visible('class_name', SearchLocators.LOCATOR_SEARCH_INPUT_BY_CLASS_NAME)

    # TODO:  def get_search_results(self):
