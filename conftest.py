import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем параметр для выбора языка
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, fr, es, etc...")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")

    # Если параметр забыли указать, выбрасываем ошибку для корректности
    if user_language is None:
        raise pytest.UsageError("--language option is required! (e.g. --language=es)")

    print(f"\nЗапуск Chrome с локализацией: {user_language}...")

    # Настраиваем параметры локализации для Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализируем браузер с настройками
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5) # Неявное ожидание элементов

    yield browser

    print("\nЗакрытие браузера...")
    browser.quit()
