from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.hyrtutorials.com/p/window-handles-practice.html")
    page.set_viewport_size({"width": 1280, "height": 800})

    # Scroll the element into view
    button = page.wait_for_selector("#newTabBtn", timeout=30000)
    button.scroll_into_view_if_needed()
    time.sleep(3)

    print("Before Clicking ------")
    original_page = page


    # Click and wait for new tab to open
    with context.expect_page() as new_tab_info:
        button.click()

    new_tab = new_tab_info.value
    new_tab.wait_for_load_state()

    print("After Switching ------")
    print(f"New tab URL: {new_tab.url}")

    original_page.bring_to_front()


    time.sleep(30)
    browser.close()

# Interview Quesiton - Insight
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
context = browser.new_context()
page = context.new_page()

page.goto('https://www.hyrtutorials.com/p/window-handles-practice.html')
page.set_default_timeout(40000)

with context.expect_page() as new_pages:
    page.locator('#newTabsBtn').click()

pages = new_pages.value
print(pages)
pages.wait_for_load_state()

all_pages = context.pages
print(all_pages)

for tab in all_pages:
    tab.bring_to_front()
    print(tab.title())
