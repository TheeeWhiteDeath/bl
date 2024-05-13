from selenium import webdriver
import time
def open_website_with_proxy(url, proxy):
    # Создаем объект ChromeOptions
    chrome_options = webdriver.ChromeOptions()
    
    # Устанавливаем прокси-сервер
    chrome_options.add_argument(f'--proxy-server=http://{proxy}')

    # Создаем экземпляр веб-драйвера Chrome с настроенными опциями
    driver = webdriver.Chrome(options=chrome_options)
    
    # Открываем URL
    driver.get(url)
    time.sleep(10)
    
    # Закрываем браузер
    driver.quit()

url = 'https://2ip.ua/ru/'
proxy = '45.94.47.66:8110'

open_website_with_proxy(url, proxy)
