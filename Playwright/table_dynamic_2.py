from playwright.sync_api import sync_playwright, expect

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=True, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
page = browser.new_page()
page.set_default_navigation_timeout(60000)
page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')

table_element = page.locator('#customers')
expect(table_element, 'Table Element is not loaded').to_be_visible()

header_elements = table_element.locator('tbody tr th span').first
expect(header_elements, 'Header Elements are not visible').to_be_visible()

header_texts = table_element.locator('tbody tr th span').all_inner_texts()
print(header_texts)