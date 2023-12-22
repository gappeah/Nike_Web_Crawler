from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import pandas as pd
import time
from datetime import datetime
import pytz

svc = Service(executable_path=binary_path)

# Get the website using the Chrome web driver
browser = webdriver.Chrome(service=svc)

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=["Product", "Name", "Price","Time"])

# Define a list of websites to scrape
websites = [
    'https://www.nike.com/gb/t/dunk-low-retro-shoe-Kd1wZr/DD1391-103',
    'https://www.nike.com/gb/t/dunk-low-retro-shoe-QgD9Gv/DD1391-100',
    'https://www.nike.com/gb/t/dunk-low-retro-shoes-p6gmkm/DV0833-400',
    'https://www.nike.com/gb/t/air-max-95-shoes-4h4CP9/FQ1235-002',
    'https://www.nike.com/gb/t/air-jordan-1-retro-high-og-shoes-lZQrDX/DZ5485-051'
]

# Loop through the websites
for website in websites:
    browser.get(website)
    try:
        # Attempt to find the price element by its xPath and product name
        price = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PDP"]/div[2]/div/div[4]/div[1]/div/div[2]/div/div/div/div/div')))
        product_name = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div/h1')))

        # Get the timezone object for London
        tz_London = pytz.timezone('Europe/London')

        # Get the current time in London
        datetime_London = datetime.now(tz_London)

        # If found, extract the text and add time to the DataFrame
        df = df._append({"Product": website, "Name": product_name.get_attribute('innerHTML'), "Price": price.get_attribute('innerHTML'),"Time": datetime_London.strftime("%H:%M:%S")}, ignore_index=True)
        print("Price for", website, ":","Product Name: " + product_name.get_attribute('innerHTML'), "Price: " + price.get_attribute('innerHTML'), "London time:", datetime_London.strftime("%H:%M:%S"))
    except:
        # If the element is not found, print an error message
        print("Price or Product was not found for", website)

# Close the browser
browser.quit()

# Save data frame data into an Excel CSV file
df.to_csv(r'PriceList.csv', index=False, encoding='utf-8-sig')