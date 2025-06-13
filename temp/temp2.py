import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.hyrtutorials.com/p/window-handles-practice.html')

driver.implicitly_wait(30)



current_window = driver.current_window_handle
al_window = driver.window_handles
print(f'All window first {al_window}')
print(f'First Window Handle {current_window}')


driver.find_element(By.ID, 'newTabsBtn').click()

all_window = driver.window_handles
print(f'All window after: {all_window}')








time.sleep(5)