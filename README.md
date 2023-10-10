# Nike_Web_Crawler

This project revolves around Python script that takes the price of your favourite trainers from the Nike website and pushes the price into a CSV file
The aim of this project is to keep track of the price in case there is a price drop You can customise it by adding time stamps whenever you push your result into the CSV file.

The original code was rewritten using Selenium instead of BeautifulSoup4 to extract the price data from the website. However, this resulted in a problem where the price data could not be found. The troubleshooting steps included identifying the element to be extracted, placing the ID element with the CSS selector element, and accounting for elements that are dynamically loaded in JavaScript. However, even after these steps were taken, the price data could not be extracted and pushed through the CSV file.

It was then decided to modify the code to extract the code using XPath. However, this also failed to extract the price data and push it through the CSV file.

It was later discovered on Stack Overflow that the append method was removed from Pandas and was replaced with _append. It was also discovered that text does not work and should be replaced with get_attribute("innerHTML").

The final issue was the " " character appearing in front of the price in the CSV file. This was likely due to encoding or character encoding mismatches when writing to the CSV file. To resolve this issue, the code was modified to explicitly specify the encoding when writing to the CSV file using the 'utf-8-sig' encoding, which is a variant of UTF-8 that includes a UTF-8 Byte Order Mark (BOM). This helped some applications recognize the UTF-8 encoding correctly and prevented the " " character from appearing in the CSV file.

The code now is in a functioning and operating state with the added function of the timestamp


