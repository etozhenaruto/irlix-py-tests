from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import List
from base.seleniumfind import SeleniumFind


class DrinkPageLocators:
    LOCATOR_INGREDIENTS_NAME_BY_CLASS_NAME: str = 'dotted-list__item-name'
    LOCATOR_INGREDIENTS_VALUE_BY_CLASS_NAME: str = 'dotted-list__item-value'
    LOCATOR_DRINK_CARD_DESCRIPTION_BY_CLASS_NANE: str = 'drinks-detail__description'


class DrinkPage(SeleniumFind):
    def __init__(self, driver):
        SeleniumFind.__init__(self)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_some_element_on_start_page(self, class_name: str) -> WebElement:
        return self.is_visible('class_name', class_name)

    def get_some_list_of_elements_start_page(self, class_name: str) -> list[WebElement]:
        return self.are_visible('class_name', class_name)

    # Получаем описание приготовления коктейля
    def get_drink_card_description(self) -> WebElement:
        return self.is_visible('class_name', DrinkPageLocators.LOCATOR_DRINK_CARD_DESCRIPTION_BY_CLASS_NANE)

    # Получаем все имена ингредиентов по имени класса в виде списка веб элементов
    def get_ingredients_name_list_by_class_name(self) -> List[WebElement]:
        return self.are_visible('class_name', DrinkPageLocators.LOCATOR_INGREDIENTS_NAME_BY_CLASS_NAME,
                                'All ingredients name of cocktail')

    # Получаем все значения имен ингредиентов по имени класса в виде списка веб элементов
    def get_ingredients_value_list_by_class_name(self) -> List[WebElement]:
        return self.are_visible('class_name', DrinkPageLocators.LOCATOR_INGREDIENTS_VALUE_BY_CLASS_NAME,
                                'All ingredients value of cocktail')

    # Получаем все значения имен ингредиентов по имени класса в виде текстового списка
    def get_text_ingredients_value(self) -> list[str]:
        return self.get_text_from_webelements(self.get_ingredients_value_list_by_class_name())

    # Получаем все имена ингредиентов по имени класса в виде текстового списка
    def get_text_ingredients_name(self) -> list[str]:
        return self.get_text_from_webelements(self.get_ingredients_name_list_by_class_name())

    # Создаем общий список имя и значение
    def get_dict_name_and_value(self, ingred_name: list[str], ingred_value: list[str]) -> dict:
        list_of_name = ingred_name
        list_of_value = ingred_value
        dict_name_and_value = dict(zip(list_of_name, list_of_value))
        return dict_name_and_value

    # Проверяем наличие желаемых элементов с желаемым значением
    def check_existence_name_and_value_in_cocktail(self, ingredients: dict, expect_ingredients: dict) -> bool:
        print(f"ИНГРЕДИЕНТЫ КОКТЕЙЛЯ: {ingredients}")
        print(f"ОЖИДАЕМЫЙ ИНГРЕДИЕНТ:{expect_ingredients}")
        result = expect_ingredients.items() <= ingredients.items()
        if result:
            print("ДАННЫЙ ИНГРЕДИЕНТ В КОКТЕЙЛЕ ЕСТЬ")
        else:
            print("ДАННОГО ИНГРЕДИЕНТА В КОКТЕЙЛЕ НЕТ")
        return result

    # Делаем значение вейлью сплитом чтоб итерировать
    def get_split_value(self, value: list[str]) -> list[str]:
        join_value = (" ".join(value))
        split_value = join_value.split()
        return split_value
