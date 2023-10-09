#This project revolves around Python script that takes the price of your favourite trainers from the Nike website and pushes the price into a CSV file
# The aim of this project is to keep track of the price in case there is a price drop You can customise
# it by adding time stamps whenever you push your result into the CSV file.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import pandas as pd
# Get the website using the Chrome web driver
browser = webdriver.Chrome()

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=["Product", "Price"])

# Define a list of websites to scrape
websites = [
    'https://www.nike.com/gb/t/dunk-low-retro-shoe-Kd1wZr/DD1391-103',
    'https://www.nike.com/gb/t/dunk-low-retro-shoe-QgD9Gv/DD1391-100',
    'https://www.nike.com/gb/t/dunk-low-retro-shoes-p6gmkm/DV0833-400'
]

# Loop through the websites
for website in websites:
    browser.get(website)
    try:
        # Attempt to find the price element by its xPath
        price = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PDP"]/div[2]/div/div'))).text
        # If found, extract the text and add to the DataFrame
        df = df.append({"Product": website, "Price": price.text}, ignore_index=True)
        print("Price for", website, ":", price.text)
    except:
        # If the element is not found, print an error message
        print("Price not found for", website)

# Close the browser
browser.quit()

# Save data frame data into an Excel CSV file
df.to_csv(r'PriceList.csv', index=False)
