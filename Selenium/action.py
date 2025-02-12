from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""ActionChains are a way to automate low level interactions such as mouse
movements, mouse button actions, key press, and context menu interactions.
This is useful for doing more complex actions like hover over and drag and
drop.

Generate user actions.
   When you call methods for actions on the ActionChains object,
   the actions are stored in a queue in the ActionChains object.
   When you call perform(), the events are fired in the order they
   are queued up.

ActionChains can be used in a chain pattern::

    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

Or actions can be queued up one by one, then performed.::

    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

    actions = ActionChains(driver)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()

Either way, the actions are performed in the order they are called, one after
another.
"""

driver.get("https://demoqa.com/droppable")
driver.set_page_load_timeout(10)

action = ActionChains(driver)

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(source, target)
action.perform()

time.sleep(10)

