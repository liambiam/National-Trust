import csv
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define categories
categories = {
    "Archaeological sites on farmland": ["archaeological", "sites", "farmland", "excavation", "dig", "artifact", "prehistoric", "settlement", "burial", "mound", "field", "survey", "landscape", "prehistoric", "ancient", "rural", "agriculture", "history", "heritage"],
    
    "Forestry and woodland": ["forestry", "woodland", "forest", "trees", "woods", "reserve", "wildlife", "ancient", "tree", "canopy", "management", "conservation", "biodiversity", "ecology", "habitat", "sustainable", "logging", "timber", "ecosystem"],
    
    "Historic assets on floodplains and valley bottoms": ["historic", "assets", "floodplains", "valley", "bottoms", "river", "watercourse", "flood", "plain", "wetland", "archaeological", "sites", "landscape", "heritage", "conservation", "erosion", "settlement", "flora", "fauna", "habitat"],
    
    "Historic parks and gardens": ["historic", "parks", "gardens", "landscape", "design", "heritage", "botanical", "formal", "sculpture", "features", "planting", "layout", "ornamental", "conservation", "restoration", "horticulture", "estate", "country", "stately", "arboretum"],
    
    "Peat, peaty soils and blanket bog": ["peat", "peaty", "soils", "blanket", "bog", "wetland", "marsh", "mire", "peatland", "carbon", "water", "conservation", "ecosystem", "flora", "fauna", "habitat", "sphagnum", "acidic", "peat-cutting", "preservation"],
    
    "Historic landscapes": ["historic", "landscapes", "landscape", "heritage", "conservation", "rural", "urban", "settlement", "countryside", "heritage", "management", "features", "scenic", "view", "interpretation", "preservation", "cultural", "natural", "archaeological", "ecological"],
    
    "Coastal site": ["coastal", "site", "coast", "sea", "shore", "beach", "cliffs", "headland", "estuary", "maritime", "erosion", "conservation", "habitat", "wildlife", "marine", "landscape", "heritage", "seaside", "lighthouse"],
    
    "Archaeological sites in hills": ["archaeological", "sites", "hills", "hilltop", "hillside", "excavation", "dig", "artifact", "prehistoric", "settlement", "landscape", "survey", "ancient", "hillfort", "fortification", "stone", "mound", "burial", "prehistoric"]
}


# Function to classify description into categories
def classify_description(description):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description.lower():
                return category
    return "other"

# Read CSV and classify descriptions
with open('nationaltrust.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        description = row['description']
        classified_category = classify_description(description)
        print(f"ID: {row['id']}, Description: {description}, Category: {classified_category}")
        # Here you can write the classified_category to a new CSV file along with other information
