import csv
import requests
from bs4 import BeautifulSoup

# List of asset types and their corresponding keywords
asset_types = {
    "Historic houses/mansions": {"keywords": ["mansion", "estate", "hall", "manor"], "sensitivity": 3},
    "Castles": {"keywords": ["castle", "fortress", "keep"], "sensitivity": 4},
    "Cottages": {"keywords": ["cottage", "croft", "thatch"], "sensitivity": 2},
    "Mills": {"keywords": ["mill", "watermill", "windmill"], "sensitivity": 3},
    "Pubs": {"keywords": ["pub", "inn", "alehouse"], "sensitivity": 2},
    "Churches": {"keywords": ["church", "chapel", "cathedral"], "sensitivity": 4},
    "Industrial buildings": {"keywords": ["factory", "mine", "ironworks", "mill"], "sensitivity": 3},
    "Historic landscaped gardens": {"keywords": ["landscaped garden", "ornamental garden", "formal garden"], "sensitivity": 4},
    "Kitchen gardens": {"keywords": ["kitchen garden", "vegetable garden", "walled garden"], "sensitivity": 3},
    "Orchards": {"keywords": ["orchard", "fruit garden"], "sensitivity": 2},
    "Forests/Woodlands": {"keywords": ["forest", "woodland", "wood"], "sensitivity": 5},
    "Moors/Hills": {"keywords": ["moor", "moorland", "hill", "upland"], "sensitivity": 4},
    "Coastline": {"keywords": ["coast", "beach", "shore", "cliff"], "sensitivity": 5},
    "Nature reserves": {"keywords": ["nature reserve", "wildlife reserve"], "sensitivity": 5},
    "Farmland": {"keywords": ["farm", "farmland", "agricultural"], "sensitivity": 3},
    "Archaeological sites/ruins": {"keywords": ["archaeological site", "ruin", "ancient ruin"], "sensitivity": 5},
    "Ancient monuments": {"keywords": ["ancient monument", "prehistoric monument"], "sensitivity": 5},
    "Historic villages": {"keywords": ["historic village", "conservation village"], "sensitivity": 4},
    "Cultural landscapes": {"keywords": ["cultural landscape", "heritage landscape"], "sensitivity": 4},
    "Parks and open spaces": {"keywords": ["park", "open space", "green space"], "sensitivity": 3},
    "Trails/Footpaths": {"keywords": ["trail", "footpath", "walking path"], "sensitivity": 2},
    "Pubs/Inns/Hotels": {"keywords": ["pub", "inn", "hotel"], "sensitivity": 2},
    "Shops": {"keywords": ["shop", "store", "retail"], "sensitivity": 2},
    "Renewable energy sites": {"keywords": ["renewable energy", "solar", "wind", "hydro"], "sensitivity": 3},
    "Conservation property portfolios": {"keywords": ["conservation property", "heritage property"], "sensitivity": 4}
}

# Read the CSV file
rows = []
with open('nationaltrust.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        website = row['website']
        description = row['description']

        # Check the description for asset type keywords
        category = None
        for asset_type, asset_data in asset_types.items():
            keywords = asset_data['keywords']
            for keyword in keywords:
                if keyword in description.lower():
                    category = asset_type
                    sensitivity = asset_data['sensitivity']
                    break
            if category:
                break

        # If the description doesn't provide enough information, check the website
        if not category:
            try:
                response = requests.get(website)
                soup = BeautifulSoup(response.content, "html.parser")
                website_content = soup.get_text().lower()

                for asset_type, asset_data in asset_types.items():
                    keywords = asset_data['keywords']
                    for keyword in keywords:
                        if keyword in website_content:
                            category = asset_type
                            sensitivity = asset_data['sensitivity']
                            break
                    if category:
                        break
            except:
                pass
        print(f"{name}: {category}")
        row['category'] = category
        row['sensitivity'] = sensitivity
        rows.append(row)

# Write the updated data to a new CSV file
fields = rows[0].keys()
with open('nationaltrust_categorized.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("Categorization results saved to 'nationaltrust_categorized.csv'")