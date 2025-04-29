import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

page = browser.new_page()

page.goto(url='https://practice.expandtesting.com/shadowdom#google_vignette')



element = page.locator('#my-btn')
print(element.count())
element.first.click()
print(element.nth().text_content())

time.sleep(5)
