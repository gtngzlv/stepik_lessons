from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

selector_for_add_button = "[class='btn btn-lg btn-primary btn-add-to-basket']"
language_for_add_button = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}


def test_add_to_basket(browser):
    language = browser.user_language
    button_text = language_for_add_button[language]
    browser.get(link)
    add_button = browser.find_element(By.CSS_SELECTOR, selector_for_add_button)
    assert button_text in add_button.text, 'Incorrect button text'