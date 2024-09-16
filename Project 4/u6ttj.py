import folium
import pandas as pd

# Read the CSV file
df = pd.read_csv('nationaltrust_categorized.csv')

# Create a map centered at a specific location
m = folium.Map(location=[52.5, -1.5], zoom_start=6)

# Define colors for sensitivity levels
colors = {
    1: 'green',
    2: 'yellow',
    3: 'red',
    4: 'blue',
    5: 'purple'
}

# Iterate over the rows of the DataFrame
for idx, row in df.iterrows():
    # Check if sensitivity value exists in the colors dictionary
    sensitivity_color = colors.get(row['sensitivity'], 'gray')  # Default to gray if sensitivity not found
    # Add a circle marker for each location
    folium.CircleMarker(
        location=[row['lat'], row['long']],
        popup=row['name'],
        radius=5,  # Adjust the radius as needed
        color=sensitivity_color,
        fill=True,
        fill_color=sensitivity_color
    ).add_to(m)

# Save the map as an image
m.save('map.html')
