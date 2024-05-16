from selenium import webdriver

# Создаем новый экземпляр браузера Chrome
driver = webdriver.Chrome()

# Открываем веб-сайт
driver.get('https://www.google.com')

# Закрываем браузер после использования
driver.quit()
