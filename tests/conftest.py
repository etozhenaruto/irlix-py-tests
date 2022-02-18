import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options



@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'http://109.195.203.123:48883/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--window-size=800,600') # Я понимаю что это юзлес в headless, но так требует задание. Наверное есть способ автоматически выбирать или то или то
    return options
