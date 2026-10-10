"""
Локаторы для страницы https://www.saucedemo.com/
Используются CSS и XPath селекторы.
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы авторизации"""
    # CSS-селекторы
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # XPath-селекторы
    LOGO = (By.XPATH, "//div[@class='login_logo']")
    LOGIN_CREDENTIALS = (By.XPATH, "//div[@id='login_credentials']")


class InventoryPageLocators:
    """Локаторы страницы товаров (после входа)"""
    # CSS-селекторы
    INVENTORY_LIST = (By.CSS_SELECTOR, ".inventory_list")
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")

    # XPath-селекторы
    PAGE_TITLE = (By.XPATH, "//span[@class='title']")
    FIRST_ITEM_NAME = (By.XPATH, "(//div[@class='inventory_item_name'])[1]")
    FIRST_ITEM_PRICE = (By.XPATH, "(//div[@class='inventory_item_price'])[1]")


class CartPageLocators:
    """Локаторы страницы корзины"""
    # CSS-селекторы
    CART_LIST = (By.CSS_SELECTOR, ".cart_list")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#continue-shopping")

    # XPath-селекторы
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")