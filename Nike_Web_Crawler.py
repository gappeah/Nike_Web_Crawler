#This project revolves around Python script that takes the price of your favourite trainers from the Nike website and pushes the price into a CSV file
# The aim of this project is to keep track of the price in case there is a price drop You can customise
# it by adding time stamps whenever you push your result into the CSV file.

import urllib.request,urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import requests
import csv


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Define the URL
url = "https://www.nike.com/gb/"

# Read the webpage
response = urllib.request.urlopen(url).read()
soup = BeautifulSoup(response, 'html.parser')

# Find links on the page
link_elements = soup.select("a[href]")

# Create a list to store URLs
urls = []

for link_element in link_elements:
    url = link_element['href']
    if "https://www.nike.com/gb/" in url:
        urls.append(url)

# Initialize the list of discovered URLs with the first page to visit
urls_to_visit = ["https://www.nike.com/gb/"]

# Create an empty list to store product information
products = []

# until all pages have been visited
while len(urls_to_visit) != 0:
    # get the page to visit from the list
    current_url = urls_to_visit.pop(0)

    # crawling logic
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")
    link_elements = soup.select("a[href]")

    product = {}
    product["url"] = current_url

    # You should replace these selectors with the actual ones for your target website
    product["image"] = soup.select_one(".wp-post-image")["src"]
    #product["title"] = soup.select_one(".product_title").text()

    # You need to extract the price from the webpage and assign it to product["price"]

    # Append the product information to the list
    products.append(product)

# Write the product information to a CSV file
with open("products.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["url", "image", "title", "price"])
    for product in products:
        writer.writerow([product["url"], product["image"], product["title"], product.get("price", "N/A")])
