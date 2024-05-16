from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_with_proxy():
    # Создаем объект ChromeOptions
    options = Options()

    # Устанавливаем User-Agent заголовок
    options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")

    # Устанавливаем язык и регион
    options.add_argument("--lang=en-GB")  # Язык: английский, Регион: Великобритания

    # Настройка прокси
    proxy = Proxy()
    proxy_address = "127.0.0.1:40000"
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_address
    proxy.ssl_proxy = proxy_address
    proxy.socks_proxy = proxy_address

    # Добавляем прокси в опции браузера
    options.add_argument(f'--proxy-server={proxy_address}')

    # Запускаем браузер с нашим User-Agent и прокси
    driver = webdriver.Chrome(options=options)

    driver.get("https://vegas.williamhill.com/")
    time.sleep(5)
    print("Opened")

    join_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="@sitebase/registration-button_hrs-action__registration-button"]')))

    # Нажимаем на кнопку
    join_button.click()
    print('Join clicked')
    time.sleep(8)

    driver.switch_to.frame("cp-registration-frame")

    first_name_field = driver.find_element(By.ID, 'reg-firstName')
    text_to_enter = "First"  
    first_name_field.send_keys(text_to_enter)
    print('Text entered firstname')
    time.sleep(1)

    last_name_field = driver.find_element(By.ID, 'reg-lastName')
    text_to_enter = "Last" 
    last_name_field.send_keys(text_to_enter)
    print('Text entered last name')
    time.sleep(1)

    day_field = driver.find_element(By.ID, 'reg-dobDay')
    text_to_enter = "12" 
    day_field.send_keys(text_to_enter)
    print('Text entered day')
    time.sleep(1)

    dob_month_field = driver.find_element(By.NAME, 'dobMonth')
    value_to_enter = "6" 
    dob_month_field.send_keys(value_to_enter)
    print('Text entered dobMonth')
    time.sleep(1)

    dob_year_field = driver.find_element(By.NAME, 'dobYear')
    year_to_enter = "1990"  
    dob_year_field.send_keys(year_to_enter)
    print('Text entered dobYear')
    time.sleep(1)

    email_field = driver.find_element(By.ID, 'reg-email')
    text_to_enter = "lastgmail@gmail.com" 
    email_field.send_keys(text_to_enter)
    print('Text entered into reg-email')
    time.sleep(2)

    mobile_field = driver.find_element(By.ID, 'reg-mobile')
    text_to_enter = "+1234567890"  
    mobile_field.send_keys(text_to_enter)
    print('Text entered into reg-mobile')
    time.sleep(2)

    search_field = driver.find_element(By.ID, 'reg-search')
    text_to_enter = "4 Drayton Gardens London SW10 9SA"
    search_field.send_keys(text_to_enter)
    print('Text entered into reg-search')

    find_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.sb-button.sb-o-button.sb-o-button--secondary.sb-o-button--normal.cs-component-address-search__button'))
    )
    find_address_button.click()
    print('Find address button clicked')

    address_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="pcaitem pcafirstitem pcaselected"]'))
    )
    address_element.click()
    print('Address element clicked')

    time.sleep(2)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'reg-submit'))
    )
    continue_button.click()
    print('Continue button clicked')

    time.sleep(5)

    driver.quit()



x = 1
for i in range(5):
    register_with_proxy()



