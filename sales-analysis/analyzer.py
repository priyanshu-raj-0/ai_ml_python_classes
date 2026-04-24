import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
# df.shape  # Return a tuple representing the dimensionality of the DataFrame.
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# summary = df.describe()
# summary.to_excel("output/data_summary.xlsx", index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")


# opening a csv file using open function

with open("output/sales_with_totals.csv", "r") as f:
    data = f.read()
    print(data)
    

# Opening a json file using open function

with open("output/sales_data.json", "r") as f:
    data = f.read()         # this is a plain text format.
    data = json.load(f)     # this convert plain text format into json format
    print(data)

