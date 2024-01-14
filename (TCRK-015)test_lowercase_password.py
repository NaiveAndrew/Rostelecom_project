# Импортируем библиотеки
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Определяем константы
URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=8c778bc0-7caf-4855-ae49-171f899d2f59&theme&auth_type"
REGISTER_BUTTON = (By.XPATH, "//*[@id='kc-register']")
PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
SUBMIT_BUTTON = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div[1]/div/form/button")
WARNING_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[4]/div[1]/span")
EXPECTED_TEXT = "Пароль должен содержать хотя бы одну заглавную букву"

# Создаем фикстуру для запуска драйвера
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Написываем тестовую функцию
def test_lowercase_password(browser):
    # Открываем страницу авторизации
    browser.get(URL)
    # Находим ccылку "Зарегистрироваться" и кликаем по ней
    register_button = browser.find_element(*REGISTER_BUTTON)
    register_button.click()
    # Находим поле "Пароль" и вводим строчными буквами латиницу и хотя бы один спецсимвол или цифру
    last_name_field = browser.find_element(*PASSWORD_FIELD) # Находим поле "Пароль"
    last_name_field.send_keys("abcdefghij123") # Вводим строчные и цифру
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    submit_button = browser.find_element(*SUBMIT_BUTTON)
    submit_button.click()
    # Ждем появления предупреждения и проверяем его текст
    warning = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(WARNING_MESSAGE))
    assert warning.text == EXPECTED_TEXT, "Неверный текст предупреждения"