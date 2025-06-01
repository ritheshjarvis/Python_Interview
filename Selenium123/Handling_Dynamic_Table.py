"""
Handling a dynamic web table in Selenium with Python—where the number of rows and columns keep changing—involves dynamically locating and iterating through table elements at runtime. Here's how you can handle such cases effectively:

✅ General Approach
Locate the table

Get all rows dynamically

Iterate through each row

Get all columns in each row

🧪 Sample HTML Structure
Imagine a table like this:

html
Copy
Edit
<table id="dataTable">
    <thead>
        <tr><th>Name</th><th>Age</th><th>City</th></tr>
    </thead>
    <tbody>
        <tr><td>John</td><td>30</td><td>New York</td></tr>
        <tr><td>Alice</td><td>25</td><td>London</td></tr>
    </tbody>
</table>
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()
driver.get("https://example.com")  # Replace with actual URL

# Locate the table
table = driver.find_element(By.ID, "dataTable")

# Get all rows in tbody
rows = table.find_elements(By.XPATH, ".//tbody/tr")

# Loop through each row
for row in rows:
    # Get all columns in the current row
    cols = row.find_elements(By.TAG_NAME, "td")

    # Extract and print text from each column
    for col in cols:
        print(col.text, end=" | ")
    print()

# Cleanup
driver.quit()

