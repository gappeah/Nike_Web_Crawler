import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import seaborn as sns

# Set up Selenium WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    service = Service("C:/chromedriver.exe")  # Replace with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to fetch and parse product details
def parse(driver, product_list):
    items = driver.find_elements(By.CSS_SELECTOR, 'div.product-card__body')
    for item in items:
        title_elem = item.find_element(By.CSS_SELECTOR, 'div.product-card__title')
        price_elem = item.find_element(By.CSS_SELECTOR, 'div.product-price')
        link_elem = item.find_element(By.CSS_SELECTOR, 'a.product-card__link-overlay')

        title = title_elem.text.strip()
        price = price_elem.text.strip().replace('£', '').replace(',', '')
        link = 'https://www.nike.com' + link_elem.get_attribute('href')

        product = {
            'Name': title,
            'Price': float(price) if price else 0.0,
            'Link': link
        }
        product_list.append(product)
        print(product)

# Function to scroll and scrape all products
def scrape_all_products(driver, product_name):
    driver.get(f'https://www.nike.com/gb/w?q={product_name.replace(" ", "+")}')
    
    product_list = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        parse(driver, product_list)
        
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(10)  # Wait for more products to load
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    return product_list

# Function to output the scraped data to a CSV
def output(product_list):
    productsdf = pd.DataFrame(product_list)
    csv_path = "Price_Sel.csv"
    productsdf.to_csv(csv_path, index=False)
    print(f'Saved to CSV at {csv_path}')
    return productsdf

# Main function to run the scraping and data visualization process
def main():
    product_name = input("Enter the product name to search on Nike: ")
    
    driver = setup_driver()
    product_list = scrape_all_products(driver, product_name)
    driver.quit()
    
    productsdf = output(product_list)

    # Load the CSV data for visualization
    df = pd.read_csv("Price_Sel.csv")
    
    # Optional: Clean the price data
    df['Price_Clean'] = df['Price']

    # Visualizations for the scraped data
    sns.set(style='whitegrid')

    # Bar plot of product prices
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Name', y='Price_Clean', data=df)
    plt.xticks(rotation=90)
    plt.title('Prices of Products')
    plt.xlabel('Product Name')
    plt.ylabel('Price (£)')
    plt.tight_layout()
    plt.show()

    # Box plot of prices by product name
    plt.figure(figsize=(50, 6))
    sns.boxplot(x='Name', y='Price_Clean', data=df)
    plt.title('Price Distribution by Product')
    plt.xlabel('Product Name')
    plt.ylabel('Price (£)')
    plt.xticks(rotation=90)  # Adjust fontsize here
    # Adjust layout to give more space to the x-axis labels
    plt.tight_layout()

    plt.show()

    # Histogram of price distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Price_Clean'], kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price (£)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()
