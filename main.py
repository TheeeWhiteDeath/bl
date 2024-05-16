from selenium import webdriver
import os

# Путь к geckodriver
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"

# Путь к исполняемому файлу Firefox
firefox_binary_path = "/data/data/com.termux/files/home/firefox/firefox-bin"

# Добавляем путь к geckodriver в переменную окружения PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(geckodriver_path)
print("Path")

# Создание экземпляра драйвера
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary_path  # Указываем путь к исполняемому файлу Firefox
driver = webdriver.Firefox(options=options)
print("Driver") 

# Пример использования: открываем сайт Google
driver.get("https://www.google.com")
print("Get")

# Закрываем драйвер после использования
driver.quit()
