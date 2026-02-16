from selenium import webdriver

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Firefox() # Використовуйте webdriver.Safari() для Safari
# Використовуйте webdriver.Chrome() для Chrome або webdriver.Firefox() для Firefox

# Відкриття веб-сторінки
driver.get("https://www.example.com")

# Робота з веб-елементами і виконання дій на сторінці

# Закриття браузера
input("Натисніть Enter, щоб закрити браузер...")
driver.quit()