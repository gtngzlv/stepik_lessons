import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def success_registration_test():
    login_registration_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    email_input_selector = "[name='registration-email']"
    random_number = random.randint(000000000, 999999999)
    string_random_number = str(random_number)
    test_email_input_value = string_random_number + "@mail.ru"
    first_password_input_selector = "[name='registration-password1']"
    second_password_input_selector = "[name='registration-password2']"
    register_button_selector = "[value='Register']"
    success_registration_text_selector = "[class='alertinner wicon']"
    success_registration_text = "Спасибо за регистрацию!"
    logout_link_selector = '[id="logout_link"]'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_registration_link)
        email_input = browser.find_element(By.CSS_SELECTOR, email_input_selector)
        first_password_input = browser.find_element(By.CSS_SELECTOR, first_password_input_selector)
        second_password_input = browser.find_element(By.CSS_SELECTOR, second_password_input_selector)
        register_button = browser.find_element(By.CSS_SELECTOR, register_button_selector)

        # Act
        email_input.send_keys(test_email_input_value)
        first_password_input.send_keys(string_random_number)
        second_password_input.send_keys(string_random_number)
        register_button.click()

        # Assert
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, success_registration_text_selector)), message=
            "Registration failed - success text was changed or another problem appeared"
        )

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, logout_link_selector)),
            message="Registration was success, but without login to account"
        )

    finally:
        time.sleep(5)
        browser.quit()


success_registration_test()
