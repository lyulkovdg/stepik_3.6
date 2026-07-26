import time
from selenium.webdriver.common.by import By

def test_is_there_an_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза, чтобы успеть проверить язык страницы
    time.sleep(30)

    # Ищем кнопку добавления в корзину с помощью метода find_elements
    # Это предотвратит падение по NoSuchElementException до выполнения assert
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверяем, что кнопка присутствует на странице (список не пустой)
    assert len(buttons) > 0, "Кнопка 'Добавить в корзину' не найдена на странице"
