
from time import sleep
import pytest
from pom.DrinkPage.DrinkPage import DrinkPage
from pom.Search.Search import SearchSteps
from pom.StartPage.StartPage import StartPageSteps




@pytest.mark.usefixtures('setup')
class TestsIrlixpub:


    def test_assert_title_on_startpage(self):
        start = StartPageSteps(self.driver)
        assert start.get_title_text() == 'Главная', "ERROR"

    def test_drinks_card_recipes(self):
        start_page = StartPageSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        start_page.get_drink_card_by_text().click()
        ingredients_name = drink_page.get_text_ingredients_name()
        ingredients_value = drink_page.get_text_ingredients_value()
        all_ingredients = drink_page.get_dict_name_and_value(ingredients_name, ingredients_value)
        drink_page.check_existence_name_and_value_in_cocktail(all_ingredients, {'banana':'50 ml'})
        drink_page.check_existence_name_and_value_in_cocktail(all_ingredients, {'cucumber': '50 ml'})


    def test_description_drink_card(self):
        start_page = StartPageSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        start_page.get_drink_card_by_name('test 2').click()
        drink_card_description = drink_page.get_drink_card_description().text
        expect_drink_card_description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem debitis deleniti deserunt dolorum earum est exercitationem, harum, ipsa iste itaque iusto maiores minima nostrum pariatur provident reiciendis repudiandae sint, voluptates."
        assert drink_card_description == expect_drink_card_description, "or lox"

    def test_size_ingredients(self):
        start_page = StartPageSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        start_page.get_drink_card_by_name('Jhonny').click()
        size_ingredients = len(drink_page.get_ingredients_name_list_by_class_name())
        assert 3 == size_ingredients, "Ingredients size error"

    def test_size_cocktail(self):
        start_page = StartPageSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        start_page.get_drink_card_by_name('Jhonny').click()
        value = drink_page.get_text_ingredients_value()
        int_value = []
        for i in drink_page.get_split_value(value):
            if 'ml' not in i:
                int_value.append(int(i))
        assert 120 == sum(int_value), "or pososaka"


    def test_find_elements(self):
        search = SearchSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        elements_of_find = drink_page.get_some_list_of_elements_start_page('drinks__link')
        assert elements_of_find != 0
        search_button = search.get_search_element()
        search_button.click()
        print(search_button)
        search.get_search_input_element().send_keys("           ")
        sleep(2)


    def test_how_much_ingredients(self):
        start_page = StartPageSteps(self.driver)
        drink_page = DrinkPage(self.driver)
        start_page.get_drink_card_by_name('Jhonny1').click()
        size_ingredients = len(drink_page.get_ingredients_name_list_by_class_name())
        if size_ingredients < 3:
            print("\nЧто то пошло не так")
        else:
            print("\nГуд качает")




















