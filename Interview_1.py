filtered_issues_based_on_release_type = ['jira1', 'jira2']
components_list = ['Backup', 'COP']
filtered_issues_based_on_components = []

for jira in filtered_issues_based_on_release_type:
    jira_components = ['COP1']
    for comp in jira_components:
        if comp in components_list:
            pass
    else:
        filtered_issues_based_on_components.append(jira)

# print(filtered_issues_based_on_components)

list1 = ['abcd', 'xyz']

if 'abc' in list1:
    print('df')

# # https://www.hyrtutorials.com/p/alertsdemo.html
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
#
# driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
# driver.find_element(By.CSS_SELECTOR, "#alertexamples").click()
#
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.alert_is_present())
#
# alert = driver.switch_to.alert
# print("Alert text:", alert.text)
# time.sleep(2)
# print("After timeout")
# alert.accept()
#
# time.sleep(10)
import time


# ------------------------ Playwright -----------------
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
page = browser.new_page()

page.goto('https://testpages.herokuapp.com/styled/alerts/alert-test.html')


page.on("dialog", lambda dialog: print(dialog.message))
page.locator('#alertexamples').click()
time.sleep(10)



