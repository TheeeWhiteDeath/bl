from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import requests
import os

def register_with_proxy():
    # Создаем объект ChromeOptions
    options = Options()

    # Устанавливаем User-Agent заголовок
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")

    # Устанавливаем язык и регион
    options.add_argument("--lang=en-GB")  # Язык: английский, Регион: Великобритания

    # Настройка прокси
    proxy = Proxy()
    proxy_address = "169.254.130.224:40000"
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_address
    proxy.ssl_proxy = proxy_address
    proxy.socks_proxy = proxy_address

    # Добавляем прокси в опции браузера
    options.add_argument(f'--proxy-server={proxy_address}')

    # Запускаем браузер с нашим User-Agent и прокси
    driver = webdriver.Chrome(options=options)

    driver.get("https://2ip.io/")
    time.sleep(5)
    driver.execute_script("document.body.style.zoom='0.5'")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    screenshot_file = os.path.join(current_directory, "screenshot.png")
    driver.save_screenshot(screenshot_file)
    driver.quit()
    # Отправляем скриншот через Telegram API бота
    bot_token = '6678247634:AAE2eUY73oZ0UeuZYTy3Gdq6LfOKAAz9bCM'
    chat_id = '1350650566'

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': open(screenshot_file, 'rb')}
    params = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=params)

    if response.status_code == 200:
        print("Скриншот успешно отправлен!")
    else:
        print("Ошибка при отправке скриншота:", response.text)




register_with_proxy()
