# generate_data.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate a date range for the year 2023
date_range = pd.date_range(start='2023-01-01', end='2023-12-31')

# Create a smooth sine wave to simulate seasonal trends in sales
wave = np.sin(np.linspace(0, 4 * np.pi, len(date_range)))  # A sine wave with 2 full periods
wave = wave * 50  # Scale the sine wave to have a bigger effect (adjust amplitude)

# Add some random noise to make it more realistic
noise = np.random.normal(0, 20, len(date_range))  # Random noise with a mean of 0 and std deviation of 20

# Final sales data: combine wave and noise
sales = 200 + wave + noise  # Base sales of 200, plus wave and noise

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Sales': sales})

# Save the data to CSV
df.to_csv('synthetic_sales_data_wavy.csv', index=False)

# Plot to check the data
plt.figure(figsize=(10, 6))
plt.plot(date_range, sales, label='Sales')
plt.title("Synthetic Sales Data with Wavy Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

print("CSV file 'synthetic_sales_data_wavy.csv' has been generated.")
