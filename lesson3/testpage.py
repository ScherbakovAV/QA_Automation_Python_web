from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    """Класс для хранения локаторов"""
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')  # Поле ввода username страницы авторизации
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')  # Поле ввода password страницы авторизации
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')  # Блок ошибки страницы авторизации
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')  # Кнопка Login страницы авторизации


class OperationsHelper(BasePage):
    """Класс, содержащий методы для работы с элементами на веб-страницах"""
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        """Ввод логина в поле ввода username страницы авторизации"""
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        """Ввод пароля в поле ввода password страницы авторизации"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def get_error_text(self):
        """Возврат текста из блока ошибки страницы авторизации"""
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'Founded text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def click_login_button(self):
        """Нажатие кнопки Login страницы авторизации"""
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
