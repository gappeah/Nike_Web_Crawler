## Nike Web Crawler Project
This project involves web scraping Nike's product pages to extract product names, prices, and links. The project showcases three different implementations of the web crawler using Selenium and BeautifulSoup. It also includes visualisation of the scraped data using Matplotlib and Seaborn.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Notable Changes Between the Versions](#notable-changes-between-the-versions)
3. [Detailed Explanation of `Nike_Web_Crawler_bs4.py`](#detailed-explanation-of-nike_web_crawler_bs4py)
4. [Detailed Explanation of `Nike_Web_Crawler_sel.py`](#detailed-explanation-of-nike_web_crawler_selpy)
5. [How to Run the Project Locally](#how-to-run-the-project-locally)
6. [Requirements](#requirements)
7. [References](#references)

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

## Differences Data Visualisation in `Nike_Web_Crawler_sel.py` and `Nike_Web_Crawler_bs4.py`
One notable aspect that requires improvement and highlights a significant difference between the two Python scripts is the amount of data available for visualisation. The BeautifulSoup-based script provides a richer dataset compared to the Selenium-driven version. This discrepancy arises because BeautifulSoup retrieves data from static HTML, which is typically more straightforward and complete. In contrast, Selenium interacts with dynamically rendered JavaScript content, which can pose challenges in data extraction.
#### Data Visualisation in `Nike_Web_Crawler_bs4.py`
![Figure_3](https://github.com/user-attachments/assets/e77894cc-7bd3-4f31-a48a-70664f0deb43)
![Figure_2](https://github.com/user-attachments/assets/1443e45e-2a9b-4887-ada6-8059ec279172)
![Figure_1](https://github.com/user-attachments/assets/acc350f5-6a3c-4990-aa39-f408a4152161)

#### Data Visualisation in `Nike_Web_Crawler_sel.py`
![Figure_3_Sel](https://github.com/user-attachments/assets/e97c501b-9d2c-408a-a0e5-5c9126b961ae)
![Figure_2_Sel](https://github.com/user-attachments/assets/59ff511c-6888-42ae-a148-75f38e2e36e4)
![Figure_1_Sel](https://github.com/user-attachments/assets/d31946e6-f845-4fb7-8d35-9d355d7ba9d7)


### Consequences of Using Selenium for Visualisations
Using Selenium to scrape data can lead to less comprehensive datasets for visualisations. This is because JavaScript-driven pages often load content dynamically, meaning that certain data elements may not be immediately available in the HTML source code. As a result, Selenium may require additional steps to interact with the page, such as waiting for elements to load or executing JavaScript, which can complicate the data extraction process.

Moreover, dynamically rendered content can sometimes lead to inconsistencies or missing data, impacting the quality and completeness of the visualisations. Therefore, while Selenium is powerful for handling complex, interactive web pages, it may require more sophisticated handling and additional processing to ensure that the data collected is suitable for creating accurate and insightful visual representations.




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
-  if you encountered the issue, `NoSuchDriverException`, indicates that Selenium could not locate or use the ChromeDriver, which is required to control Chrome for web scraping. Here are a few steps to resolve the issue:
  1. **Ensure ChromeDriver is installed and accessible:**
     - Download the appropriate version of ChromeDriver for your version of Google Chrome from the [ChromeDriver official website](https://sites.google.com/chromium.org/driver/).
     - Make sure the version of ChromeDriver matches your Chrome browser version. You can check your Chrome version by navigating to `chrome://settings/help` in Chrome.
  2. **Set the correct path to ChromeDriver:**
     - In your script, replace `"path_to_chromedriver"` in this line:
     ```python
     service = Service("path_to_chromedriver")  # Replace with your ChromeDriver path
     ```
     with the actual path to your `chromedriver.exe` file. For example:
     ```python
     service = Service("C:/path/to/chromedriver.exe")
     ```
     In this case in my version it will be
     ```python
     service = Service("C:/chromedriver.exe")
     ```
3. **Add ChromeDriver to your system PATH:**
   - Ensure that the directory containing `chromedriver.exe` is added to your system PATH so that it can be found globally. You can follow these steps:
     - Right-click on `This PC` or `My Computer`, select `Properties`, then go to `Advanced system settings`.
     - Click on `Environment Variables`, find the `Path` variable under `System variables`, and click `Edit`.
     - Add the directory where `chromedriver.exe` is located.

4. **Check if the ChromeDriver version matches Chrome:**
   - Chrome updates frequently, and your ChromeDriver must match the installed version of Chrome. If you recently updated Chrome, make sure you update ChromeDriver to the compatible version.

5. **Verify that headless mode is working:**
   - If you're using headless mode (`options.add_argument("--headless")`), try running it in normal mode by commenting out the headless argument. This will allow you to see if the browser is being correctly opened and controlled:
     ```python
     # options.add_argument("--headless")
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

Here’s a reference section you can add to your `README.md` file:

---

## References

1. **Selenium Documentation**:  
   Official documentation for Selenium WebDriver, covering usage, troubleshooting, and best practices.  
   [Selenium Documentation](https://www.selenium.dev/documentation/webdriver/)

2. **ChromeDriver Downloads**:  
   Link to download the latest compatible version of ChromeDriver for your Chrome browser version.  
   [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

3. **BeautifulSoup Documentation**:  
   Detailed guide on using BeautifulSoup for parsing HTML and XML documents in Python.  
   [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

4. **Pandas Documentation**:  
   Guide to using pandas for data manipulation and analysis, including CSV file handling.  
   [Pandas Documentation](https://pandas.pydata.org/docs/)

5. **Matplotlib Documentation**:  
   Comprehensive documentation on using Matplotlib for creating static, animated, and interactive visualizations in Python.  
   [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

6. **Seaborn Documentation**:  
   Official documentation for Seaborn, a Python data visualization library built on top of Matplotlib.  
   [Seaborn Documentation](https://seaborn.pydata.org/)

7. **Headless Chrome**:  
   Information on running Chrome in headless mode, which allows it to run in the background without a GUI.  
   [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)

8. **Web Scraping Best Practices**:  
   Best practices and ethical considerations when scraping websites, including avoiding overloading servers and respecting terms of service.  
   [Web Scraping Best Practices](https://www.scrapingbee.com/blog/web-scraping-best-practices/)
