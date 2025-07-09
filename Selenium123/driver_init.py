from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Specify the path to the ChromeDriver executable
chrome_driver_path = "/path/to/chromedriver"

# Initialize the Chrome WebDriver with Service
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.implicitly_wait(30)
# driver.maximize_window()

element = driver.find_element(By.ID, "")

element1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable())

driver.fullscreen_window()
