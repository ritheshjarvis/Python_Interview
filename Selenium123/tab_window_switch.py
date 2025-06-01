import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
current_window = driver.current_window_handle
print(current_window)

# element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable())
element: WebElement = driver.find_element(By.CSS_SELECTOR, "#newTabBtn")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(3)

wait = WebDriverWait(driver, 30)
element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#newTabBtn")))
element.click()


print("Before Switching ------")
current_window = driver.current_window_handle
print(current_window)

for window in driver.window_handles:
    if window != driver.current_window_handle:
        driver.switch_to.window(window)

print("After Switching ------")
current_window = driver.current_window_handle
print(current_window)

time.sleep(30)

# ------------------- Practice -----------------

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('xyz.com')
driver.implicitly_wait(30)

current_window= driver.current_window_handle

# click operation

for window in driver.window_handles:
    if window != current_window:
        if driver.title == 'xyz':
            driver.switch_to.window(window)

driver.switch_to.default_content()




