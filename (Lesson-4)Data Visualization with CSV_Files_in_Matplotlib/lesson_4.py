
### Python Code: lesson_4.py
import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('data.csv')  # replace 'data.csv' with the actual file path
print(data.head())  # display first few rows of the data

# Line Graph Example: Sales Over Time
plt.plot(data['Date'], data['Sales'])
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Scatter Plot Example: Sales vs Advertising Cost
plt.scatter(data['Advertising_Cost'], data['Sales'], color='red')
plt.title('Sales vs Advertising Cost')
plt.xlabel('Advertising Cost')
plt.ylabel('Sales')
plt.show()

# Pie Chart Example: Market Share Over Time
plt.pie(data['Market_Share'], labels=data['Date'], autopct='%1.1f%%')
plt.title('Market Share Over Time')
plt.show()
