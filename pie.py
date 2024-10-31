import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '/path/to/your/student_test_data.csv'
data = pd.read_csv(file_path)

# Line graph comparing sales over Q1 and Q2 for each product
plt.figure(figsize=(10, 6))
plt.plot(data['Product'], data['Sales_Q1'], marker='o', label='Sales Q1')
plt.plot(data['Product'], data['Sales_Q2'], marker='s', label='Sales Q2')
plt.title('Sales Comparison for Q1 and Q2')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.legend()
plt.grid()
plt.show()

# Scatter plot of advertising cost versus total sales (Q1 + Q2)
plt.figure(figsize=(10, 6))
total_sales = data['Sales_Q1'] + data['Sales_Q2']
plt.scatter(data['Advertising_Cost'], total_sales, c='blue', edgecolor='k')
plt.title('Advertising Cost vs. Total Sales')
plt.xlabel('Advertising Cost')
plt.ylabel('Total Sales (Q1 + Q2)')
plt.grid()
plt.show()

# Pie chart of market share distribution
plt.figure(figsize=(8, 8))
plt.pie(data['Market_Share'], labels=data['Product'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Market Share Distribution')
plt.show()
