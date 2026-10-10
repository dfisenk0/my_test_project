from selenium_tests.locators.main_page import MainPageLocators


def test_open_google(driver):
    """Проверка открытия Google"""
    driver.get("https://www.google.com")
    assert "Google" in driver.title


def test_search_input_exists(driver):
    """Проверка наличия поля поиска"""
    driver.get("https://www.google.com")
    search = driver.find_element(*MainPageLocators.SEARCH_INPUT)
    assert search.is_displayed()