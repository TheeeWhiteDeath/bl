from selenium import webdriver

# Путь к geckodriver
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"

# Путь к исполняемому файлу Firefox
firefox_binary_path = "/data/data/com.termux/files/home/firefox/firefox-bin"

# Создание экземпляра драйвера
driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_binary=firefox_binary_path)

# Пример использования: открываем сайт Google
driver.get("https://www.google.com")

# Закрываем драйвер после использования
driver.quit()
