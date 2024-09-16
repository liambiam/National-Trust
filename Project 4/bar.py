import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('nationaltrust_categorized.csv')

# Group the data by category and count the occurrences
category_counts = df['category'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
