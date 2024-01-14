# Импортируем библиотеки
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LOGIN_PASSWORD import email
from LOGIN_PASSWORD import password

# Определяем константы
URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=d379d0dd-4d0f-49bf-a0c5-20f08fc4c397&theme=light&auth_type"
EMAIL_TAB = (By.XPATH, "//*[@id='t-btn-tab-mail']") # Добавил константу для таба "email"
EMAIL_FIELD = (By.XPATH, "//*[@id='username']") # Добавил константу для поля "Электронная почта"
PASSWORD_FIELD = (By.XPATH, "//*[@id='password']") # Добавил константу для поля "Пароль"
LOGIN_BUTTON = (By.XPATH, "//*[@id='kc-login']") # Добавил константу для кнопки "Войти"
ACCOUNT_DETAILS = (By.XPATH, "/html/body/div/main/div/div[2]/div[1]/h3[1]") # Добавил константу для элемента "Учетные данные"
PERSONAL_CABINETS = (By.XPATH, "/html/body/div/main/div/div[2]/div[3]/h3") # Добавил константу для элемента "Личные кабинеты"
SECURITY = (By.XPATH, "/html/body/div/main/div/div[2]/div[1]/h3[2]") # Добавил константу для элемента "Безопасность"
EXPECTED_TEXTS = ["Учетные данные", "Личные кабинеты", "Безопасность"] # Добавил константу для ожидаемых текстов

# Создаем фикстуру для запуска драйвера
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Написываем тестовую функцию
def test_login_with_correct_email_and_password(browser):
    # Открываем страницу с формой авторизации
    browser.get(URL)
    # Находим таб "email" и кликаем по нему
    email_tab = browser.find_element(*EMAIL_TAB) # Находим таб "email"
    email_tab.click() # Кликаем по нему
    # Находим поле "Электронная почта" и вводим валидный email
    email_field = browser.find_element(*EMAIL_FIELD) # Находим поле "Электронная почта"
    email_field.send_keys(email) # Вводим валидный email
    # Находим поле "Пароль" и вводим валидный пароль
    password_field = browser.find_element(*PASSWORD_FIELD) # Находим поле "Пароль"
    password_field.send_keys(password) # Вводим валидный пароль
    # Находим кнопку "Войти" и кликаем по ней
    login_button = browser.find_element(*LOGIN_BUTTON) # Находим кнопку "Войти"
    login_button.click() # Кликаем по ней
    # Ждем появления элементов "Учетные данные", "Личные кабинеты" и "Безопасность" и проверяем их тексты
    account_details = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ACCOUNT_DETAILS))
# Ждем, пока элемент "Учетные данные" не станет видимым

    assert account_details.text == EXPECTED_TEXTS[0], "Неверный текст элемента 'Учетные данные'"
# Проверяем, что текст совпадает с ожидаемым
    personal_cabinets = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(PERSONAL_CABINETS))
# Ждем, пока элемент "Личные кабинеты" не станет видимым
    assert personal_cabinets.text == EXPECTED_TEXTS[1], "Неверный текст элемента 'Личные кабинеты'"
# Проверяем, что текст совпадает с ожидаемым
    security = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(SECURITY))
# Ждем, пока элемент "Безопасность" не станет видимым
    assert security.text == EXPECTED_TEXTS[2], "Неверный текст элемента 'Безопасность'"
# Проверяем, что текст совпадает с ожидаемым