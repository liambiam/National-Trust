import pandas as pd
from geopy.geocoders import Nominatim

# Load the joined CSV file
joined_df = pd.read_csv("joined_NT_sites.csv")

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="national-trust-locator")

# Function to get coordinates for a location
def get_coordinates(location):
    geo_location = geolocator.geocode(location)
    if geo_location:
        print(geo_location.latitude, geo_location.longitude)
        return geo_location.latitude, geo_location.longitude
    else:
        return None, None

# Apply the function to get coordinates for each location
coordinates = joined_df['Name'].apply(get_coordinates)

# Create a new dataframe with coordinates
coordinates_df = pd.DataFrame(coordinates.tolist(), columns=['Latitude', 'Longitude'])

# Concatenate the original dataframe with the coordinates dataframe
joined_df_with_coordinates = pd.concat([joined_df, coordinates_df], axis=1)

# Save the dataframe with coordinates to a new CSV file
joined_df_with_coordinates.to_csv("joined_file_with_coordinates.csv", index=False)

# Print the first few rows of the dataframe with coordinates
print(joined_df_with_coordinates.head())
