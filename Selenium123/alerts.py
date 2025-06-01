from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
"""
First switch to alert
alert = driver.switch_to.alert

Common Alert Methods:
alert.accept()
Clicks the "OK" button on the alert.

alert.dismiss()
Clicks the "Cancel" button on confirmation dialogs.

alert.text
Retrieves the text displayed in the alert.

alert.send_keys("text")
Sends keystrokes to a prompt alert.

Optional: Wait for an Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

"""

driver = webdriver.Chrome()

# driver.get('https://demoqa.com/alerts')
driver.get('https://www.hyrtutorials.com/p/alertsdemo.html')
# driver.set_page_load_timeout(10)
driver.implicitly_wait(20)

element = driver.find_element(By.ID, 'confirmBox')




driver.execute_script("arguments[0].scrollIntoView(true);", element)
# action = ActionChains(driver)
#
#
# action.move_to_element(element).click(element).perform()
time.sleep(1)
element.click()
time.sleep(1)
alert = driver.switch_to.alert

alert.accept()

# ---------------------------------------------------------

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.find_element(By.CSS_SELECTOR, "#alertexamples").click()

wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.alert_is_present())

alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
print("After timeout")
alert.accept()

time.sleep(10)