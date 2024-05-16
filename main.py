from selenium import webdriver

# Путь до ChromeDriver
chrome_driver_path = '/data/data/com.termux/files/usr/bin/chromedriver'

# Создание объекта WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Пример использования - открываем Google
driver.get('https://www.google.com')

# Закрываем браузер
driver.quit()
