from selenium import webdriver
from selenium.webdriver.common.options import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.capabilities

element = WebDriverWait(driver)