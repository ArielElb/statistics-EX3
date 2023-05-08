import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plot
sns.set_style("ticks")
sns.set_palette("husl")

# Read in the data and filter by year
df = pd.read_csv('Tomato.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df = df[df['Year'].between(2014, 2020)]

# Add a column for the month
df['Month'] = df['Date'].dt.month

# Compute the average prices for each month and year
avg_prices = df.groupby(['Year', 'Month'])['Average'].mean()

# Set the number of bars and the range of prices
num_bars = 5
min_price = 15
max_price = 75
bar_width = (max_price - min_price) / num_bars

# Customize the plot
fig, ax = plt.subplots()
ax.hist(avg_prices, bins=num_bars, range=(min_price, max_price), edgecolor='black',
        alpha=0.8)
ax.set_xlabel('Average Tomato Prices', fontweight='bold', fontsize=12, color='#333333')
ax.set_ylabel('Number of Months', fontweight='bold', fontsize=12, color='#333333')
ax.set_title('Histogram of Average Tomato Prices', fontweight='bold', fontsize=14, color='#333333')

# Add a grid to the plot
plt.grid(linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Change the color of the spines
ax.spines['bottom'].set_color('#333333')
ax.spines['top'].set_color('#333333')
ax.spines['left'].set_color('#333333')
ax.spines['right'].set_color('#333333')

# Change the color and font size of the tick labels
plt.xticks(fontsize=10, color='#333333')
plt.yticks(fontsize=10, color='#333333')

# Set the color and font size of the x-axis label
ax.xaxis.label.set_color('#333333')
ax.xaxis.label.set_fontsize(12)
ax.xaxis.label.set_fontweight('bold')

# Set the color and font size of the y-axis label
ax.yaxis.label.set_color('#333333')
ax.yaxis.label.set_fontsize(12)
ax.yaxis.label.set_fontweight('bold')

# Add a legend to the plot
ax.legend(['Tomato Prices'])

plt.show()
