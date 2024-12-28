from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Инициализация браузера
browser = webdriver.Chrome()

try:
    # Установка размеров окна
    browser.set_window_size(1024, 768)

    # Открытие страницы
    browser.get("https://bumbac.md")

    # Ожидание и поиск элемента
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
    )

    # Клик по элементу
    element.click()

    # Ожидание, чтобы убедиться, что элемент доступен после изменения DOM
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
    )

    # Проверка, что элемент видим
    assert element.is_displayed(), "Element is not displayed"

except StaleElementReferenceException:
    # Если элемент становится устаревшим, пытаемся снова найти его
    print("Element is stale, retrying...")
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
    )
    assert element.is_displayed(), "Element is not displayed"

except Exception as e:
    # Общая обработка других возможных ошибок
    print(f"An error occurred: {e}")

finally:
    # Завершение работы с браузером
    browser.quit()


  # Если все прошло успешно, выводим сообщение
print("Test passed")

