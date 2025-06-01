from playwright.sync_api import sync_playwright, expect

playwright = sync_playwright().start()
playwright.selectors.set_test_id_attribute()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
context = browser.new_context()
page = context.new_page()
# page.locator()
page.wait_for_selector()
page.set_default_timeout()
page.set_default_navigation_timeout()
expect.set_options()


# <h3>Sign up</h3>
# <label>
#   <input type="checkbox" /> Subscribe
# </label>
# <br/>
# <button>Submit</button>


page.get_by_label()
page.get_by_role("heading", name="Sign up").filter()
page.get_by_role("button", name="Submit")
page.get_by_role("checkbox", name="Submit")
page.get_by_title()
page.get_by_text()
page.get_by_alt_text()
page.get_by_placeholder()

# --------------- hello -------------------
rows = page.get_by_role("listitem")
count = rows.count()


count = rows.count()
for i in range(count):
    print(rows.nth(i).text_content())
