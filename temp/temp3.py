import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
context = browser.new_context()
page = context.new_page()

page.goto('https://www.hyrtutorials.com/p/window-handles-practice.html')
page.set_default_timeout(40000)

with context.expect_page() as new_pages:
    page.locator('#newTabsBtn').click()

# time.sleep(3)


pages = new_pages.value
print(pages)
pages.wait_for_load_state()


all_pages = context.pages
print(all_pages)

for tab in all_pages:
    tab.bring_to_front()
    print(tab.title())