import pandas as pd
import rasterio

# Load the input CSV file
input_csv = 'nationaltrust.csv'
df = pd.read_csv(input_csv)

# Load the TIFF file
tiff_file = 'FME_333C3E30_1713014745663_198470/data/a22baa7c-5809-4a02-87e0-3cf87d4e223a/gblcm10m2021.tif'
tiff_dataset = rasterio.open(tiff_file)

# Create a new column to store the land use types
df['land_use_type'] = ''

# Loop through the coordinates and extract the land use type
for index, row in df.iterrows():
    x, y = row['long'], row['lat']
    if tiff_dataset.bounds.left <= x <= tiff_dataset.bounds.right and tiff_dataset.bounds.bottom <= y <= tiff_dataset.bounds.top:
        col, row = tiff_dataset.index(x, y)
        land_use_value = tiff_dataset.read(1, window=((row, row+1), (col, col+1)))[0, 0]
        df.at[index, 'land_use_type'] = land_use_value

# Save the updated DataFrame to a new CSV file
output_csv = 'path/to/your/output_with_land_use.csv'
df.to_csv(output_csv, index=False)