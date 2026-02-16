from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox

# Знаходження елемента за ID
def test_id(base_url):
    driver:Firefox = base_url
    user_field = driver.find_element(By.ID, "username")
    pass_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login_button")
    assert user_field
    assert pass_field
    assert login_button


def test_xpath(base_url):
    driver:Firefox = base_url
    user_field = driver.find_element(By.XPATH, "//input[@id='username']")
    pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[@id='login_button']")
    assert user_field
    assert pass_field
    assert login_button

def test_css(base_url):
    driver:Firefox = base_url
    user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
    pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")

    assert user_field
    assert pass_field
    assert login_button


def test_xpath_2(base_url):
    driver:Firefox = base_url
    form_element = driver.find_element(By.TAG_NAME, "form")

    # Знаходження елемента за XPath з вказанням значення
    li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")

    # Знаходження елемента за XPath з вказанням iндексу
    li_el2_idx = driver.find_element(By.XPATH, "//li[2]")


def test_fill_field(action):
    driver:Firefox = action
    # Знаходження текстових полів за ID і введення тексту
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("example_username")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("example_password")

    # Знаходження радіо кнопок за ID і вибір варіанта
    male_radio = driver.find_element(By.ID, "male")
    male_radio.click()

    # Знаходження чекбоксу за ID і встановлення прапорця
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()

    # Вибір значення з випадаючого списку за ID
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_visible_text("США")

    # Натискання на кнопку за ID
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
