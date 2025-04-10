from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("xyz")

driver.implicitly_wait(30)

driver.find_element(By.ID, "")

element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable())

driver.fullscreen_window()
element.sc