from selenium import webdriver

# Путь к драйверу Chrome WebDriver
chrome_driver_path = "./chromedriver"

# Создание экземпляра драйвера Chrome с помощью Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL веб-страницы, которую вы хотите открыть
url = "https://www.example.com"

# Загрузка страницы
driver.get(url)
