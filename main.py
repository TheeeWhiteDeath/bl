from selenium import webdriver

# Путь к geckodriver
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"

# Путь к исполняемому файлу Firefox
firefox_binary_path = "/data/data/com.termux/files/home/firefox/firefox.exe"

# Создание экземпляра драйвера
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary_path  # Указываем путь к исполняемому файлу Firefox
driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Пример использования: открываем сайт Google
driver.get("https://www.google.com")

# Закрываем драйвер после использования
driver.quit()
