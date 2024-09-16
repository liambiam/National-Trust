import csv
import json
import urllib.request

# Fetch JSON data from the National Trust API
url = 'https://www.nationaltrust.org.uk/api/search/places?query=&lat=52&lon=0&milesRadius=1000&maxPlaceResults=1000'
response = urllib.request.urlopen(url)
json_data = response.read().decode('utf-8')

# Parse JSON data
data = json.loads(json_data)

# Write data to CSV file with UTF-8 encoding
with open('nationaltrust.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['id', 'name', 'town', 'county', 'lat', 'long', 'description', 'website'])

    for place in data['multiMatch']['results']:
        csv_writer.writerow([
            place.get('id', {}).get('value', ''),
            place.get('title', ''),
            place.get('town', ''),
            place.get('county', ''),
            place.get('location', {}).get('lat', ''),
            place.get('location', {}).get('lon', ''),
            place.get('description', ''),
            place.get('websiteUrl', '') 
        ])
