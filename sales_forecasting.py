# sales_forecasting.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

# Step 1: Generate synthetic daily sales data for 2023
date_range = pd.date_range(start='2023-01-01', end='2023-12-31')
sales = np.random.poisson(lam=200, size=len(date_range))
df = pd.DataFrame({'Date': date_range, 'Sales': sales})

# Step 2: Rename columns for Prophet
df = df.rename(columns={'Date': 'ds', 'Sales': 'y'})

# Optional: View first few rows
print("Sample Data:\n", df.head())

# Step 3: Plot the historical sales
plt.figure(figsize=(10, 4))
plt.plot(df['ds'], df['y'], label='Historical Sales')
plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

# Step 4: Create and fit the Prophet model
model = Prophet()
model.fit(df)

# Step 5: Create a DataFrame for future dates (next 30 days)
future = model.make_future_dataframe(periods=30)

# Step 6: Predict future sales
forecast = model.predict(future)

# Step 7: Plot the forecast
model.plot(forecast)
plt.title("Sales Forecast (Next 30 Days)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
