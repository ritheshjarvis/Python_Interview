from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
page = browser.new_page()

page.goto('https://www.saucedemo.com/')
element = page.wait_for_selector('#user-name',)
print(element.bounding_box())