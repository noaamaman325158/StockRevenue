import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
stock_data = pd.read_csv("indexData.csv")

# Convert the 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Extract the year and month for grouping
stock_data['Month'] = stock_data['Date'].dt.to_period('M')

# Calculate the monthly revenue as the sum of the 'Adj Close' values
monthly_revenue = stock_data.groupby('Month')['Adj Close'].sum().reset_index()

# Generate the graph
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(monthly_revenue['Month'].astype(str), monthly_revenue['Adj Close'], marker='o')

# Labeling the axes
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Revenue')

# Adding a grid
plt.grid(True)

# Rotating the x-axis labels
plt.xticks(rotation=90)

# Setting the x-axis labels format
ax.set_xticks(monthly_revenue['Month'][::12].astype(str))  # Show one label per year to avoid clutter

# Adjusting the layout
plt.tight_layout()

# Display the plot
plt.show()
