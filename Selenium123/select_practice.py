import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
driver = webdriver.Chrome()

driver.get('https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html')

driver.implicitly_wait(10)

dropdown_element = driver.find_element(By.CSS_SELECTOR, "#ide")

select = Select(dropdown_element)
select.select_by_value('vs')
select.select_by_visible_text('NetBeans')
elements = select.options

dropdown_element.get_attribute()

# for el in elements:
#     print(el.text)

time.sleep(5)