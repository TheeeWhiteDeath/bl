from selenium import webdriver

# Путь к geckodriver
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"

# Создание экземпляра драйвера
driver = webdriver.Firefox(executable_path=geckodriver_path)

# Пример использования: открываем сайт Google
driver.get("https://www.google.com")

# Закрываем драйвер после использования
driver.quit()
