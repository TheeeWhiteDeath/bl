from selenium import webdriver

def open_website_with_proxy(url, proxy):
    # Налаштування драйвера Chrome для використання headless режиму
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Включення headless режиму
    chrome_options.add_argument('--no-sandbox')  # Додаткові налаштування для безпечного запуску у віртуальному середовищі

    # Завантаження драйвера Chrome без запуску браузера
    driver = webdriver.Chrome(options=chrome_options)

    # Отримання веб-сторінки
    driver.get(url)

    # Закриваємо драйвер
    driver.quit()

url = 'https://www.example.com'
proxy = 'ваш_проксі'

open_website_with_proxy(url, proxy)
