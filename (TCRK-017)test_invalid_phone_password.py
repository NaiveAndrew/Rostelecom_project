# Импортируем библиотеки
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # Импортируем модуль time для использования метода sleep
import timeit # Импортируем модуль timeit для использования таймера

# Определяем константы
URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=d379d0dd-4d0f-49bf-a0c5-20f08fc4c397&theme=light&auth_type"
PHONE_TAB = (By.XPATH, "//*[@id='t-btn-tab-phone']")
PHONE_FIELD = (By.XPATH, "//*[@id='username']")
PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//*[@id='kc-login']")
ERROR_MESSAGE = (By.XPATH, "//*[@id='form-error-message']")
FORGOT_PASSWORD = (By.XPATH, "//*[@id='forgot_password']")
EXPECTED_TEXT = "Неверный логин или пароль"
#EXPECTED_COLOR = "orange"

# Создаем фикстуру для запуска драйвера
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Написываем тестовую функцию
def test_invalid_phone_and_password(browser):
    # Открываем страницу авторизации
    browser.get(URL)
    # Находим таб "Телефон" и кликаем по нему
    phone_tab = browser.find_element(*PHONE_TAB)
    phone_tab.click()
    # Находим поле "Мобильный телефон" и вводим некорректное значение
    phone_field = browser.find_element(*PHONE_FIELD)
    phone_field.send_keys("+70000000000")
    # Находим поле "Пароль" и вводим некорректное значение
    password_field = browser.find_element(*PASSWORD_FIELD)
    password_field.send_keys("qwerty12345")
    # Добавляем задержку в 10 секунд для ручного ввода капчи
    print("Пожалуйста, введите капчу в течение 10 секунд")  # Выводим сообщение в консоль
    start = timeit.default_timer()  # Запускаем таймер
    time.sleep(10000)  # Оператор должен ввести капчу в течение этого времени
    stop = timeit.default_timer()  # Останавливаем таймер
    print(f"Вы потратили {stop - start} секунд на ввод капчи")  # Выводим сообщение в консоль
    # Находим кнопку "Войти" и кликаем по ней
    login_button = browser.find_element(*LOGIN_BUTTON)
    login_button.click()
    # Ждем появления сообщения об ошибке и проверяем его текст
    error = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(ERROR_MESSAGE))
    assert error.text == EXPECTED_TEXT, "Неверный текст сообщения об ошибке"
    # Проверяем цвет ссылки "Забыл пароль"
    #forgot_password = browser.find_element(*FORGOT_PASSWORD)
    #assert forgot_password.value_of_css_property("color") == EXPECTED_COLOR, "Неверный цвет ссылки 'Забыл пароль'"