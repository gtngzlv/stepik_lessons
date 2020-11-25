import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def success_registration_test():
    main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
    login_or_register_link_selector = "[id='login_link']"
    email_input_selector = "[name='registration-email']"
    random_number = random.randint(000000000, 999999999)
    string_random_number = str(random_number)
    test_email_input_value = string_random_number + "@mail.ru"
    first_password_input_selector = "[name='registration-password1']"
    second_password_input_selector = "[name=registration-password2']"
    register_button_selector = "[value='Register']"
    success_registration_text_selector = "[class='alertinner wicon']"
    success_registration_text = "Спасибо за регистрацию!"
    logout_link_selector = '[id="logout_link"]'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        login_or_register_link = browser.find_element(By.CSS_SELECTOR, login_or_register_link_selector)
        email_input = browser.find_element(By.CSS_SELECTOR, email_input_selector)
        first_password_input = browser.find_element(By.CSS_SELECTOR, first_password_input_selector)
        second_password_input = browser.find_element(By.CSS_SELECTOR, second_password_input_selector)
        register_button = browser.find_element(By.CSS_SELECTOR, register_button_selector)

        # Act
        login_or_register_link.click()
        email_input.send_keys(test_email_input_value)
        first_password_input.send_keys(string_random_number)
        second_password_input.send_keys(string_random_number)
        register_button.click()

        # Assert
        success_registration_text_persist = WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located(By.CSS_SELECTOR, success_registration_text_selector)
        )
        assert success_registration_text_persist.text in success_registration_text, \
            "Registration failed - success text was changed or another problem appeared"
        logout_link_persist = WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located(By.CSS_SELECTOR, logout_link_selector)
        )
        assert logout_link_persist, "Registration was success, but without login to account"
    finally:
        time.sleep()
        browser.quit()


success_registration_test()
