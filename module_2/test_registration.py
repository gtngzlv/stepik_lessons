from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_firstname=browser.find_element_by_xpath("//label[text()='First name*']/following::input")
    input_firstname.send_keys('Ivan')
    input_lastname=browser.find_element_by_xpath("//label[text()='Last name*']/following::input")
    input_lastname.send_keys('Ivanov')
    input_email=browser.find_element_by_xpath("//label[text()='Email*']/following::input")
    input_email.send_keys('ivan@mail.ru')
    input_phone=browser.find_element_by_xpath("//label[text()='Phone:']/following::input")
    input_phone.send_keys('123456')
    input_address=browser.find_element_by_xpath("//label[text()='Address:']/following::input")
    input_address.send_keys('Moscow')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()