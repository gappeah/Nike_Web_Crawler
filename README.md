## Nike Web Crawler

**A Python Script to Track Nike Shoe Prices**

### Overview

This Python script utilizes Selenium and Pandas to scrape the prices of Nike shoes from the Nike website and store them in a CSV file. It provides real-time price tracking for a select list of Nike shoes.


https://github.com/gappeah/Nike_Web_Crawler/assets/114095068/14d178bf-18e4-4031-9657-52e78d9d4fe9

![image](https://github.com/gappeah/Nike_Web_Crawler/assets/114095068/525ee6b3-8467-4cf5-9f80-cdcf315f44f5)


### Requirements

1. Python 3.x
2. Selenium webdriver: Install using `pip install selenium`
3. Chrome web driver: Download the appropriate Chrome web driver for your system and place it in the `PATH` or specify its location in the script.
4. Pandas library: Install using `pip install pandas`

### Usage

1. Download the `Nike_Web_Crawler.py` file to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the `Nike_Web_Crawler.py` file.
3. Run the script by entering the following command:
```
python Nike_Web_Crawler.py
```

### Script Functionality

1. The script scrapes the prices of five Nike shoes:
    - Dunk Low Retro Shoe 
    - Dunk Low Retro Shoe 
    - Dunk Low Retro Shoes
    - Air Max 95 Shoes
    - Air Jordan 1 Retro High OG Shoes
This is can be easily replaced with a product from the Nike Website

2. Extracts the shoe name and price from each shoe's product page.
3. Stores the retrieved information in a DataFrame with columns "Product", "Name", "Price", and "Time".
4. Adds a timestamp to the `Time` column to track the price at specific times.
5. Saves the DataFrame data to a CSV file named `PriceList.csv` for future reference.

### Additional Notes

1. The script uses Selenium's WebDriverWait to wait for specific elements to load before attempting to retrieve their content.
2. The `tz_London` variable is used to set the timezone for the timestamp in the `Time` column.
3. The `.get_attribute('innerHTML')` method is used to extract the inner HTML content of the price and product name elements.
4. The `.to_csv()` method is used to save the DataFrame data to a CSV file.

### Updates

1. The original code was rewritten using Selenium instead of BeautifulSoup4 to extract the price data from the website. However, this resulted in a problem where the price data could not be found. The troubleshooting steps included identifying the element to be extracted, placing the ID element with the CSS selector element, and accounting for elements that are dynamically loaded in JavaScript. However, even after these steps were taken, the price data could not be extracted and pushed through the CSV file.
2. It was then decided to modify the code to extract the code using XPath. However, this also failed to extract the price data and push it through the CSV file.
3. It was later discovered on Stack Overflow that the append method was removed from Pandas and was replaced with _append. It was also discovered that text does not work and should be replaced with get_attribute("innerHTML").
4. The final issue was the " " character appearing in front of the price in the CSV file. This was likely due to encoding or character encoding mismatches when writing to the CSV file. To resolve this issue, the code was modified to explicitly specify the encoding when writing to the CSV file using the 'utf-8-sig' encoding, which is a variant of UTF-8 that includes a UTF-8 Byte Order Mark (BOM). This helped some applications recognize the UTF-8 encoding correctly and prevented the " " character from appearing in the CSV file.
5. The code now is in a functioning and operating state with the added function of the timestamp

