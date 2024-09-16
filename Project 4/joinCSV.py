import pandas as pd

# Load the first CSV file
df1 = pd.read_csv("National_Trust_Open_Data_Land_Always_Open_-3744780538279066630.csv")

# Load the second CSV file
df2 = pd.read_csv("National_Trust_Open_Data_Land_Limited_Access_8599134333039861494.csv")

# Join the two dataframes
joined_df = pd.concat([df1, df2], ignore_index=True)

# Save the joined dataframe to a new CSV file
joined_df.to_csv("joined_NT_sites.csv", index=False)

# Print the first few rows of the joined dataframe
print(joined_df.head())