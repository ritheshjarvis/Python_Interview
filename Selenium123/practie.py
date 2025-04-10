import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(2000)

driver.get("https://www.saucedemo.com/")

element = driver.find_element(By.ID, "login-button")

print("Location")
print(element.location)

print("Size")
print(element.size)

print("Rect")
print(element.rect)

print("albel")
print(element.aria_role)
#
# element = driver.find_element(By.ID, "password")
#
# print("Location")
# print(element.location)
#
# print("Size")
# print(element.size)
#
# print("Rect")
# print(element.rect)
#
#
# element = driver.find_element(By.ID, "login-button")
#
# print("Location")
# print(element.location)
#
# print("Size")
# print(element.size)
#
# print("Rect")
# print(element.rect)
#
# # wait = WebDriverWait(driver, 20)
# # text_box_2 = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'txt2')))
# # text_box_2.send_keys("Hie")
# #
# # time.sleep(40)
#
#
#
#
