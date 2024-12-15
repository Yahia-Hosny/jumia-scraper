from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import re

# Configure Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")  # Disable browser extensions
options.add_argument("--disable-gpu")  # Disable GPU usage
options.add_argument("--no-sandbox")  # Improve compatibility for low-resource environments
options.add_argument("--disable-dev-shm-usage")  # Optimize for low-resource devices

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open the target URL (Jumia Android phones page)
driver.get("https://www.jumia.com.eg/android-phones/")

# Close any pop-up windows if present
try:
    elem = driver.find_element(By.XPATH, '//*[@id="fi-nl-pop-email"]')  # Locate the email input field in the pop-up
    elem.clear()  # Clear any text in the field
    elem.send_keys(Keys.ESCAPE)  # Send the ESCAPE key to close the pop-up
    time.sleep(1)  # Wait for the action to complete
except Exception as e:
    print("No pop-up found or an error occurred:", e)

# Extract the number of pages for pagination
try:
    last_page_element = driver.find_element(By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[3]/a[4]')
    link = last_page_element.get_attribute("href")  # Get the link of the last page button
    match = re.search(r"=(\d+)#", link)  # Extract the page number using a regular expression
    if match:
        number = match.group(1)
    else:
        number = 20  # Default number of pages if extraction fails
except Exception as e:
    print("Error extracting the number of pages:", e)
    number = 20

# Initialize lists to store product data
product_name_list = []
product_price_list = []

# Loop through all pages and scrape product data
for _ in range(1, int(number)):
    try:
        # Locate all product containers on the page
        products = driver.find_elements(By.CSS_SELECTOR, 'div.info')

        # Extract product names and prices
        product_names = [product.find_element(By.CLASS_NAME, 'name').text for product in products]
        product_prices = [product.find_element(By.CLASS_NAME, 'prc').text for product in products]

        # Append the extracted data to the lists
        product_name_list.extend(product_names)
        product_price_list.extend(product_prices)

        # Click the "Next" button to go to the next page
        target = driver.find_element(By.CSS_SELECTOR, '#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div.pg-w.-ptm.-pbxl > a:nth-child(6)')
        ActionChains(driver).move_to_element(target).click().perform()
        time.sleep(1)  # Wait for the next page to load
    except Exception as e:
        print("Could not find or click the next button:", e)
        break

# Save the scraped data to a CSV file
df = pd.DataFrame({
    'Product Name': product_name_list,
    'Product Price': product_price_list
})
print(df)  # Print the DataFrame to the console
df.to_csv("products.csv", index=False, encoding="utf-8")  # Save data as CSV

# Close the WebDriver
driver.quit()
