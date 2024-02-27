# This entrypoint file to be used in development. Start by reading README.md
import sea_level_predictor
from unittest import main
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7, label='Original Data')
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

# Perform linear regression for all data points
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

# Create a line of best fit through the year 2050 using all data points
plt.plot(data['Year'], slope * data['Year'] + intercept, color='red', label='All Data Best Fit Line')

# Filter data from year 2000 to the most recent year
recent_data = data[data['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Create a line of best fit through the year 2050 using data from 2000 onwards
plt.plot(data['Year'], slope_recent * data['Year'] + intercept_recent, color='green', label='2000-onwards Best Fit Line')

# Predict sea level rise in 2050
year_2050 = 2050
sea_level_2050_all_data = slope * year_2050 + intercept
sea_level_2050_recent_data = slope_recent * year_2050 + intercept_recent

# Display predictions
print(f"Predicted sea level rise in 2050 (using all data): {sea_level_2050_all_data:.2f} inches")
print(f"Predicted sea level rise in 2050 (using data from 2000 onwards): {sea_level_2050_recent_data:.2f} inches")

# Show legend and plot
plt.legend()
plt.grid(True)
plt.show()
# Test your function by calling it here
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)