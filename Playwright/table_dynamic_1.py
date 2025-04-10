from playwright.sync_api import sync_playwright


def test_dynamic_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in UI mode
        page = browser.new_page()
        page.goto("https://example.com")  # Replace with actual URL

        # Locate the table
        table_locator = page.locator("//table[@id='myTable']")  # Adjust based on table structure

        # Extract all headers (Fixed Headers)
        headers = table_locator.locator("thead tr th").all_inner_texts()
        print(f"Headers: {headers}")  # Example: ['ID', 'Name', 'Age', 'Actions']

        # Find all rows (excluding headers)
        rows = table_locator.locator("tbody tr").all()  # Get all row elements dynamically

        for index, row in enumerate(rows):
            # Extract cell values for the current row
            cells = row.locator("td").all_inner_texts()
            print(f"Row {index + 1}: {cells}")  # Example: ['101', 'Alice', '25', 'Edit/Delete']

            # Example: Click "Edit" button if Name is "Alice"
            if "Alice" in cells:
                edit_button = row.locator("button:has-text('Edit')")  # Locate 'Edit' button
                edit_button.click()
                print("Clicked Edit for Alice")
                break  # Stop after first match

        browser.close()


# Run the function
test_dynamic_table()
