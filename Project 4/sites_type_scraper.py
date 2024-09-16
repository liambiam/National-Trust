import csv
import requests
from bs4 import BeautifulSoup

def get_property_type(website_url):
    # Send a GET request to the website URL
    response = requests.get(website_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the property type on the page
    property_type_tag = soup.find('span', class_='css-1jsn5ue evxn8k12')
    if property_type_tag:
        return property_type_tag.text.strip()
    else:
        return "Property type not found"

# Read data from CSV file
sites_data = []
with open('nationaltrust.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        sites_data.append(row)

# Iterate over each site data and scrape property type
for site_data in sites_data:
    website_url = site_data['website']
    property_type = get_property_type(website_url)
    print(f"{site_data['name']}: {property_type}")
