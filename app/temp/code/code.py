import requests
import pandas as pd
import matplotlib.pyplot as plt

# API call to fetch the Apple stock price data
url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-01-09/2023-01-09?adjusted=true&sort=asc&limit=5000&apiKey={YOUR_POLYGON_API_KEY}"
response = requests.get(url)
data = response.json()

# Extract the relevant data from the API response
results = data['results']
timestamps = [pd.Timestamp(result['t'], unit='ms') for result in results]
close_prices = [result['c'] for result in results]

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Date': timestamps, 'Close Price': close_prices})
df.set_index('Date', inplace=True)

# Plot the stock chart
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close Price'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Apple Stock Price Chart')
plt.grid(True)
plt.show()