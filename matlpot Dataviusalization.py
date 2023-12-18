# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(url)

# Display the first few rows
df.head()
# Check for missing values
print(df.isnull().sum())

# No missing values, no need for additional data cleaning
# Total cases, deaths, and recovered
total_cases = df['Confirmed'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()

# Country with the highest cases, deaths, and recovered
highest_cases_country = df[df['Confirmed'] == df['Confirmed'].max()]['Country'].values[0]
highest_deaths_country = df[df['Deaths'] == df['Deaths'].max()]['Country'].values[0]
highest_recovered_country = df[df['Recovered'] == df['Recovered'].max()]['Country'].values[0]

# Daily new cases for a specific country (e.g., 'US')
daily_new_cases_us = df[df['Country'] == 'US']['Confirmed'].diff().fillna(0)

# Line chart showing the trend globally
df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Confirmed'], label='Confirmed', marker='o')
plt.plot(df['Date'], df['Deaths'], label='Deaths', marker='o')
plt.plot(df['Date'], df['Recovered'], label='Recovered', marker='o')
plt.title('Global COVID-19 Trends')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()
