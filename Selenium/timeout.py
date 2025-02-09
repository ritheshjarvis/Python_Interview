from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

# driver.implicitly_wait(10)
# driver.set_script_timeout(10)
driver.set_page_load_timeout(20)
print(driver.timeouts)
"""
 - set_page_load_timeout() is a Selenium WebDriver method that specifies the maximum amount of time (in seconds),
   that the driver should wait for a page to load when using methods like driver.get().
 - If the page does not load completely within the specified timeout period, Selenium will throw a TimeoutException.
 
- The set_page_load_timeout() setting applies to any navigation that triggers a full page load, 
  not just when you use driver.get(). Here’s what that means:

driver.get() Method:
When you call driver.get(url), Selenium waits for the page to load completely, 
and if it exceeds the timeout you set, it throws a TimeoutException.

Navigation Between Pages:
If you navigate between pages—such as clicking a link that causes a full page load or using navigation commands 
(like driver.navigate().to() in some languages)—the same page load timeout applies. Essentially, any operation 
that triggers a full page load will be subject to the timeout defined by set_page_load_timeout().

AJAX or Partial Page Loads:
Note that this timeout does not apply to asynchronous operations like AJAX calls or content that 
loads dynamically without causing a full page refresh. For those cases, you might need to use explicit waits (like WebDriverWait) to handle the dynamic content.
"""

driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
