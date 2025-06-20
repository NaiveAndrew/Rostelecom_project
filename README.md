# Rostelecom_project
Автотесты для дипломного проекта Skillfactory. Реальный кейс от компании «Ростелеком Информационные Технологии».
## О проекте

Этот проект содержит примеры автотестов на Python с использованием библиотек pytest и selenium. Автотесты написаны для сайта https://b2c.passport.rt.ru/ и проверяют различные сценарии регистрации и входа в личный кабинет.

## Цель проекта

Целью проекта является демонстрация возможностей автоматизации тестирования веб-приложений с помощью Python, pytest и selenium. Проект также может служить образцом для написания собственных автотестов на Python.

## Функционал проекта

Проект предоставляет следующий функционал:

- Запуск автотестов с помощью команды `pytest`
- Параметризация тестовых данных с помощью декоратора `@pytest.mark.parametrize`
- Использование фикстур для инициализации и завершения тестов с помощью декоратора `@pytest.fixture`
- Использование констант для хранения локаторов элементов и ожидаемых результатов
- Использование методов `find_element`, `send_keys`, `click`, `get`, `current_url` и других для работы с элементами веб-страницы
- Использование классов `WebDriverWait` и `expected_conditions` для ожидания появления или исчезновения элементов
- Использование оператора `assert` для проверки фактических результатов с ожидаемыми

## Примечания
- В ходе экспериментов так и не удалось заставить работать корректно автотест "(TCRK-017)test_invalid_phone_password", были трудности с Captcha из-за множественных попыток логина.
- При работе с данным сайтом баги не были обнаружены, но я описал несколько потенциально возможных багов для подобных сервисов в отчете по ссылке https://docs.google.com/spreadsheets/d/1mHtLX8fBSNpk1gGTl7f5k8LtrKLLDFmK/edit?usp=sharing&ouid=117586209096454247801&rtpof=true&sd=true. Там же можно найти тест-кейсы и описание используемых инструментов.

---

# Rostelecom_project
## Project Description

Autotests created for the Skillfactory diploma project based on a real-world case from Rostelecom Information Technologies.  
This project includes Python-based tests using `pytest` and `selenium` for the website https://b2c.passport.rt.ru/.  
It covers scenarios for user registration and login.

## Project Goal

To demonstrate how to automate web application testing using Python, `pytest`, and `selenium`.  
The project can also serve as a template for writing your own UI tests.

## Features

- Test execution using `pytest`
- Parameterization via `@pytest.mark.parametrize`
- Use of fixtures with `@pytest.fixture` for test setup/teardown
- Constants used for element locators and expected results
- Selenium methods used: `find_element`, `send_keys`, `click`, `get`, `current_url`
- Explicit waits with `WebDriverWait` and `expected_conditions`
- Assertions with `assert` for result validation

## Notes

- The test `(TCRK-017)test_invalid_phone_password` fails due to Captcha after multiple login attempts.
- No actual bugs were found, but [this report](https://docs.google.com/spreadsheets/d/1mHtLX8fBSNpk1gGTl7f5k8LtrKLLDFmK/edit?usp=sharing&ouid=117586209096454247801&rtpof=true&sd=true) includes possible defects, test cases, and tools used.
