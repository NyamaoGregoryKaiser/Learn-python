
### Python Code: lesson_3.py

import pandas as pd
import matplotlib.pyplot as plt

# Load data from an Excel file
data = pd.read_excel('data.xlsx')  # replace 'data.xlsx' with the actual file path
print(data.head())  # display first few rows of the data

# Line Graph Example: Sales Over Time
plt.plot(data['Month'], data['Sales'])
plt.title('Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# Bar Graph Example: Sales by Category
plt.bar(data['Category'], data['Sales'], color='teal')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# Scatter Plot Example: Sales vs Profit
plt.scatter(data['Sales'], data['Profit'], color='green')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

# Pie Chart Example: Market Share by Product
plt.pie(data['Market Share'], labels=data['Product'], autopct='%1.1f%%')
plt.title('Market Share by Product')
plt.show()
