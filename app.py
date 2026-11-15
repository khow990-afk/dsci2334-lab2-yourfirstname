import pandas as pd
import os

file_path = '/content/cafe_sales.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Successfully loaded dataset!")
    print("Shape:", df.shape)
    print("First Date:", df['date'].min())
    print("Last Date:", df['date'].max())
    print("Number of Branches:", df['branch'].nunique())
else:
    print(f"Error: '{file_path}' not found.")

df['total_sar'] = df['unit_price'] * df['quantity']

revenue_per_branch = df.groupby('branch')['total_sar'].sum()
print(revenue_per_branch)

best_selling = df.groupby('product')['quantity'].sum().idxmax()
print("Best-Selling Product:", best_selling)

import matplotlib.pyplot as plt

df['date'] = pd.to_datetime(df['date'])
df['Month'] = df['date'].dt.to_period('M').astype(str)
monthly_revenue = df.groupby('Month')['total_sar'].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue (SAR)')
plt.grid(True)
plt.show()
