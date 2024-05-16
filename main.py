from selenium import webdriver
from fake_useragent import UserAgent
import time

# Указываем путь к исполняемому файлу Firefox
firefox_binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

# Указываем путь к geckodriver
geckodriver_binary = "/data/data/com.termux/files/home/firefox/firefox-bin"

# Инициализируем объект опций для браузера Firefox
options = webdriver.FirefoxOptions()

# Указываем путь к бинарному файлу Firefox
options.binary_location = firefox_binary

# Устанавливаем прокси-сервер
proxy = "185.199.231.45:8382"
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.http", proxy.split(':')[0])
options.set_preference("network.proxy.http_port", int(proxy.split(':')[1]))
options.set_preference("network.proxy.ssl", proxy.split(':')[0])
options.set_preference("network.proxy.ssl_port", int(proxy.split(':')[1]))

# Указываем случайный пользовательский агент
useragent = UserAgent()
random_useragent = useragent.random
options.set_preference("general.useragent.override", random_useragent)

try:
    # Запускаем браузер
    driver = webdriver.Firefox(
        executable_path=geckodriver_binary,
        options=options
    )
    
    # Открываем страницу
    driver.get("https://atomurl.net/myip/")
    
    # Ждем некоторое время для загрузки страницы
    time.sleep(5)

    # Закрываем браузер после использования
    driver.quit()
except Exception as e:
    print(e)
