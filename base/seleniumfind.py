from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


class SeleniumFind:
    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def __get_selenium_by(self, find_by: str) -> dict:  # инкапсуляция, сделал это класс приватным
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)



