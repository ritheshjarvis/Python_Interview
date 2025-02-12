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
Sends keystrokes to a prompt alert."""

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


time.sleep(3)
