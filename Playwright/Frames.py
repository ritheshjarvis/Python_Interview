'''
Ex:
<iframe src="SingleFrame.html" id="singleframe" name="SingleFrame" style="float: left;height: 300px;width: 600px">

iframe attributes:
id
name
src (URL)

🔍 What are Frames (or iframes) from JavaScript and Browser Perspective?
From both JavaScript and the browser's point of view, a frame (especially an iframe) is essentially a nested browsing context.
It's like embedding a separate webpage (with its own DOM, CSS, and JavaScript environment) within another webpage.
'''

from playwright.sync_api import sync_playwright, Frame, Page

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
page: Page = browser.new_page()

page.goto('https://demo.automationtesting.in/Frames.html')
page.frame_locator('#singleframe').locator('input[type=text]').fill("Hie")

frame: Frame = page.frame(name='SingleFrame')
page.frames
print(frame.url)
print(frame.name)
print(frame)
frame.locator('input[type=text]').fill("Hie")
# ------------------------------- Playwright ends here ------------------------
import re
import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

page = browser.new_page()
# page.set_default_timeout(2000)

page.goto('https://demo.automationtesting.in/Frames.html')

# Identify the frame using frame's name attribute
# frame = page.frame('SingleFrame')
# frame = page.frame(url=r'.*SingleFrame.*')
# frame = page.frame(url=re.compile(".*SingleFrame"))
# frame = page.frame(url='https://demo.automationtesting.in/SingleFrame.html')
# print(frame)
# frame.fill('[type="text"]', 'rithesh here')

print(page.frame)
print(page.main_frame)

# page.frame_locator('[name="SingleFrame"]').locator('[type="text"]').fill('Rithesh here')

time.sleep(5)

"""-----------
Selenium

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class FrameExample {
    public static void main(String[] args) {
        // Assume you have a WebDriver instance named 'driver' already initialized

        // 1. Navigate to the page with frames
        driver.get("https://www.example.com/page-with-frames");

        // 2. Identify the frame by its ID (or name or index)
        String frameId = "my-frame"; // Replace with the actual frame ID

        // 3. Switch to the frame
        driver.switchTo().frame(frameId);

        // 4. Interact with elements inside the frame
        WebElement elementInsideFrame = driver.findElement(By.id("element-id"));
        elementInsideFrame.sendKeys("Some text");

        // 5. Switch back to the main page (if needed)
        driver.switchTo().defaultContent();
    }
}

"""
"""
Nested Frames:

🧾 Scenario
Suppose you have this structure:

<!-- Top-level page -->
<iframe id="outer-frame" src="outer.html"></iframe>

<!-- Content of outer.html -->
<iframe id="inner-frame" src="inner.html"></iframe>

<!-- Content of inner.html -->
<input type="text" id="nestedInput" />
✅ Playwright Python Code: Handling Nested Iframes

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")  # Replace with your real URL

    # Step 1: Access outer iframe
    outer_frame = page.frame_locator("iframe#outer-frame").frame()

    # Step 2: Access inner iframe inside outer iframe
    inner_frame = outer_frame.frame_locator("iframe#inner-frame").frame()

    # Step 3: Interact with element inside the inner iframe
    inner_frame.fill("input#nestedInput", "Hello from nested iframe!")

    browser.close()
🧠 Explanation
frame_locator("iframe#id").frame() is the key method to navigate through nested frames.

You chain them to go deeper, just like navigating nested objects.

📌 Alternative (Non-frame-locator Way)
You can also loop through frames manually:

# List all frames
for frame in page.frames:
    print("Frame:", frame.name, "URL:", frame.url)
Then, select frames based on name, URL, or content:

outer = page.frame(name="outer-frame")
inner = outer.frame(name="inner-frame")
inner.fill("input#nestedInput", "Hello!")
"""