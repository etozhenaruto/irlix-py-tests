from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from base.seleniumfind import SeleniumFind


class StartPageLocators:
    LOCATOR_TITLE_BY_CLASS_NAME: str = 'title'
    LOCATOR_DRINK_CARD_BY_LINK_TEXT: str = '80'


class StartPageSteps(SeleniumFind):
    def __init__(self, driver):
        SeleniumFind.__init__(self)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_title(self) -> WebElement:
        return self.is_visible('class_name', StartPageLocators.LOCATOR_TITLE_BY_CLASS_NAME,
                               'Main page title element')

    def get_title_text(self) -> str:
        title_text = self.get_title().text
        return title_text

    def get_drink_card_by_text(self) -> WebElement:
        return self.is_visible('partial_link_text', StartPageLocators.LOCATOR_DRINK_CARD_BY_LINK_TEXT,
                               'Cocktail card with alco_value = 80%')

    def get_drink_card_by_name(self, name: str) -> WebElement:
        return self.is_visible('partial_link_text', name)
