"""
**EXplicit for EXpected**

**IMplicit for IMaginary**
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# def test_example_with_implicit_wait(driver):
#     browser = driver
#     browser.implicitly_wait(10)  # Чекати не більше 10 секунд

#     browser.get("https://www.example.com")

#     # Знаходимо елемент на сторінці
#     heading = browser.find_element(By.TAG_NAME,"h1")

#     # Перевіряємо, чи вірний текст заголовку
#     assert heading.text == "Example Domain"


def test_example_with_explicit_wait(driver):
    driver.get("https://www.example.com")

    # Чекаємо, поки заголовок сторінки з'явиться (не більше 10 секунд)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    # Знаходимо елемент на сторінці після очікування
    heading = driver.find_element(By.TAG_NAME,"h1")

    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"



def webelement(driver, xpath):
    try:
        element = WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException as e:
        raise TimeoutException("За даний час елемент не зявився на сторінці") from e


def test_not_found(driver):
    driver.get("https://www.example.com")
    xpath = '//li[@id="ewuygeb"]'
    element = webelement(driver, xpath)
    element.click()
    # Закриття браузера
    driver.quit()

# 1. presence_of_element_located
# 2. visibility_of_element_located
# 3. element_to_be_clickable
# 4. text_to_be_present_in_element
# 5. title_contains

