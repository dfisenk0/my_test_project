from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")