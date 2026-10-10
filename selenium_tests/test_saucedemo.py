from selenium.webdriver.common.by import By
from locators.saucedemo_locators import LoginPageLocators, InventoryPageLocators


def test_login_page_elements(driver):
    """Проверка элементов страницы авторизации"""
    driver.get("https://www.saucedemo.com/")

    assert driver.find_element(*LoginPageLocators.USERNAME_INPUT).is_displayed()
    assert driver.find_element(*LoginPageLocators.PASSWORD_INPUT).is_displayed()
    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    assert driver.find_element(*LoginPageLocators.LOGO).is_displayed()


def test_successful_login(driver):
    """Проверка успешного входа"""
    driver.get("https://www.saucedemo.com/")

    driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    assert "inventory" in driver.current_url
    assert driver.find_element(*InventoryPageLocators.PAGE_TITLE).text == "Products"