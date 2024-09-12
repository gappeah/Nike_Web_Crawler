## Nike Web Crawler Project
This project involves web scraping Nike's product pages to extract product names, prices, and links. The project showcases three different implementations of the web crawler using Selenium and BeautifulSoup. It also includes visualization of the scraped data using Matplotlib and Seaborn.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Notable Changes Between the Versions](#notable-changes-between-the-versions)
3. [Detailed Explanation of `Nike_Web_Crawler_bs4.py`](#detailed-explanation-of-nike_web_crawler_bs4py)
4. [Detailed Explanation of `Nike_Web_Crawler_sel.py`](#detailed-explanation-of-nike_web_crawler_selpy)
5. [How to Run the Project Locally](#how-to-run-the-project-locally)
6. [Requirements](#requirements)

---

## Project Overview

The project comprises three different versions of a Nike web crawler, each designed to scrape product details from Nike's website:

- **`Nike_Web_Crawler_Original.py`**: The first version uses **Selenium** to scrape specific Nike product pages.
- **`Nike_Web_Crawler_bs4.py`**: This version is rewritten using **BeautifulSoup** for more efficient page scraping and parsing.
- **`Nike_Web_Crawler_sel.py`**: A revamped **Selenium-based** scraper that crawls search result pages on Nike, scrolling dynamically and fetching multiple products.

## Notable Changes Between the Versions

### 1. **Selenium vs. BeautifulSoup**
- The first and third versions use **Selenium**, while the second version (`Nike_Web_Crawler_bs4.py`) uses **BeautifulSoup**.
- **BeautifulSoup** is faster when dealing with static HTML content, but **Selenium** is required for interacting with dynamic web elements like scrolling and waiting for JavaScript-loaded content.

### 2. **Targeted Pages vs. Search Pages**
- In the original script, specific product pages were targeted, meaning that the product URLs were hardcoded into the script:
  ```python
  websites = [
      'https://www.nike.com/gb/t/dunk-low-retro-shoe-Kd1wZr/DD1391-103',
      'https://www.nike.com/gb/t/dunk-low-retro-shoe-QgD9Gv/DD1391-100',
      ...
  ]
  ```
  However, both the newer scripts scrape search result pages based on user input:
  ```python
  product_name = input("Enter the product name to search on Nike: ")
  ```

### 3. **Headless Mode**
- The **Selenium** version (`Nike_Web_Crawler_sel.py`) can be run in headless mode (without a graphical browser) for faster execution and ease of automation:
  ```python
  options.add_argument("--headless")  # Run in headless mode (no GUI)
  ```

### 4. **Scrolling Mechanism**
- In **`Nike_Web_Crawler_sel.py`**, the scraper scrolls down the page dynamically to load more products, simulating user behavior:
  ```python
  driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
  time.sleep(2)  # Wait for more products to load
  ```

### 5. **Data Visualization**
- Both newer scripts include a data visualization feature using **Matplotlib** and **Seaborn**:
  ```python
  sns.barplot(x='Name', y='Price_Clean', data=df)
  ```

## Detailed Explanation of `Nike_Web_Crawler_bs4.py`

The `Nike_Web_Crawler_bs4.py` script uses the **BeautifulSoup** library to scrape search result pages on Nike's website.

### Key Features:
1. **Generating the Search URL**:
   ```python
   def generate_nike_url(product_name, page_number=1):
       return f'https://www.nike.com/gb/w?q={product_name.replace(" ", "+")}&page={page_number}'
   ```
   This generates a URL based on the product search query entered by the user.

2. **Parsing Product Data**:
   ```python
   results = soup.find_all('div', {'class': 'product-card__body'})
   for item in results:
       title = item.find('div', {'class': 'product-card__title'}).text.strip()
       price = item.find('div', {'class': 'product-price'}).text.strip()
   ```
   This code searches the HTML content for product details like name, price, and links.

3. **Saving Data**:
   The scraped data is saved into a CSV file using pandas:
   ```python
   productsdf.to_csv("Price.csv", index=False)
   ```

4. **Data Visualisation**:
   After saving the data, it is visualised using Seaborn and Matplotlib:
   ```python
   sns.barplot(x='Name', y='Price_Clean', data=df)
   ```

## Differences Data Visualisation in `Nike_Web_Crawler_sel.py` and `Nike_Web_Crawler_bs4.py`


## Detailed Explanation of `Nike_Web_Crawler_sel.py`

The `Nike_Web_Crawler_sel.py` script utilises **Selenium** to handle JavaScript-loaded pages and scroll to load all products on the search result pages.

### Key Features:
1. **Setting Up Selenium WebDriver**:
   The script sets up Selenium WebDriver with headless mode enabled for fast, non-GUI execution:
   ```python
   options = Options()
   options.add_argument("--headless")
   driver = webdriver.Chrome(service=service, options=options)
   ```

2. **Dynamic Scrolling**:
   The script scrolls to the bottom of the page to load more products dynamically:
   ```python
   while True:
       driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
       time.sleep(2)  # Wait for more products to load
   ```

3. **Parsing Product Data**:
   The product details are parsed using Selenium's `find_elements` method:
   ```python
   items = driver.find_elements(By.CSS_SELECTOR, 'div.product-card__body')
   for item in items:
       title = item.find_element(By.CSS_SELECTOR, 'div.product-card__title').text.strip()
   ```

4. **Saving and Visualizing Data**:
   Like the BeautifulSoup version, the scraped data is saved in a CSV and visualized using Seaborn:
   ```python
   df = pd.read_csv("Price_Sel_Drive.csv")
   sns.barplot(x='Name', y='Price_Clean', data=df)
   ```

## How to Run the Project Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/gappeah/nike-web-crawler.git
cd nike-web-crawler
```

### Step 2: Set Up Virtual Environment
It's recommended to set up a virtual environment to manage dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### Step 3: Download ChromeDriver
- Download **ChromeDriver** from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a suitable folder.
- Update the path in the `Nike_Web_Crawler_sel.py`:
  ```python
  service = Service("C:/path_to_your_chromedriver/chromedriver.exe")
  ```

### Step 4: Run the Desired Script
You can run any of the scripts by using:
```bash
python Nike_Web_Crawler_bs4.py  # For BeautifulSoup version
python Nike_Web_Crawler_sel.py  # For Selenium version
```

Follow the prompts for the product name and the number of pages to scrape.

### Step 5: View the Results
- The scraped data will be saved in a CSV file (`Price.csv` or `Price_Sel_Drive.csv`).
- The visualizations will pop up automatically after the scraping is completed.

## Requirements

- Python 3.x
- ChromeDriver (for Selenium versions)
- Python libraries: `Selenium`, `BeautifulSoup`, `pandas`, `matplotlib`, `seaborn`

```bash
pip install selenium beautifulsoup4 pandas matplotlib seaborn
```
