from playwright.sync_api import sync_playwright
import time
def open_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        time.sleep(5)
        # Виконайте тут ваші дії зі сторінкою
        print("done")
        browser.close()


url = 'https://www.example.com'

open_website(url)
