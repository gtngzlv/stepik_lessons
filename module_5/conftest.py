from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help="lets choose language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")

    if language not in ['ru', 'en-GB', 'es', 'fr']:
        raise pytest.UsageError('we dont have such language')

    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print('\n opening chrome for you')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.user_language = language
    yield browser
    print("\n closing browser")
    browser.quit()