from testpage import OperationsHelper
import logging


def test_login_invalid_user(browser):
    """Негативный тест попытки входа на сайт несуществующим пользователем"""
    logging.info('Test 1 is starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == '401'
