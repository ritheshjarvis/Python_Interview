from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("xyz")

driver.implicitly_wait(30)

driver.find_element(By.ID, "")
