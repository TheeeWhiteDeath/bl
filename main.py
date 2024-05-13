from selenium import webdriver
import time
def open_website_with_proxy(url, proxy):
    # Налаштування драйвера Chrome для використання headless режиму
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('executable_path=./chromedriver.exe')  # Вказуємо шлях до виконуваного файлу драйвера

    # Завантаження драйвера Chrome без запуску браузера
    driver = webdriver.Chrome(options=chrome_options)
    
    # Отримання веб-сторінки
    driver.get(url)
    
    # Закриваємо драйвер
    time.sleep(10)
    driver.quit()
    

url = 'https://www.example.com'
proxy = 'ваш_проксі'


open_website_with_proxy(url, proxy)
