import geopandas as gpd

# Load GeoTIFF file
raster_file = '/FME_333C3E30_1713014745663_198470/data/a22baa7c-5809-4a02-87e0-3cf87d4e223a/gblcm10m2021.tif'

# Read National Trust sites data
national_trust_sites = gpd.read_file('nationaltrust.csv')

# Read raster data using Rasterio
raster_data = gpd.read_file(raster_file)

# Extract land use information for each site
land_use = []
for index, site in national_trust_sites.iterrows():
    point = site.geometry.centroid
    land_use_value = raster_data.interpolate(point).values[0]
    land_use.append(land_use_value)

# Add land use information to National Trust sites data
national_trust_sites['land_use'] = land_use

# Write data to CSV with land use information
national_trust_sites.to_csv('nationaltrust_with_land_use.csv', index=False)
