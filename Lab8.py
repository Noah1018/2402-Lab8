import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load datasets
df_weather = pd.read_csv("city_weather.csv")
sensor_data = np.loadtxt("sensor_readings.csv", delimiter=",", skiprows=1)

# Inspect data
print("Weather DataFrame Head:")
print(df_weather.head())
print("\nWeather DataFrame Info:")
print(df_weather.info())
print("\nWeather DataFrame Shape:", df_weather.shape)
print("Sensor Data Shape:", sensor_data.shape)

# --- Weather Visualizations ---

# Line Plot: AvgTemp by Month for each City
plt.figure(figsize=(10, 6))
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    plt.plot(city_data['Month'], city_data['AvgTemp'], marker='o', label=city)
plt.title('Average Monthly Temperature by City')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.grid()
plt.show()

# Bar Plot: Total Rainfall by City
total_rainfall = df_weather.groupby('City')['Rainfall'].sum()
plt.figure(figsize=(8, 5))
colors = ['blue', 'orange', 'green']
bars = plt.bar(total_rainfall.index, total_rainfall.values, color=colors)
plt.title('Total Rainfall from January to March by City')
plt.xlabel('City')
plt.ylabel('Total Rainfall (mm)')
plt.grid(axis='y')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center')
plt.show()

# Scatter Plot: AvgTemp vs SunshineHours, color-coded by City
plt.figure(figsize=(10, 6))
city_colors = {'Calgary': 'red', 'Vancouver': 'blue', 'Toronto': 'green'}
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    plt.scatter(city_data['AvgTemp'], city_data['SunshineHours'], color=city_colors[city], label=city)
plt.title('Relationship between Average Temperature and Sunshine Hours')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Sunshine Hours')
plt.legend()
plt.grid()
plt.show()

# --- Combined 2×2 Grid of Weather Plots (bottom-right empty) ---
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Subplot 1: Line Plot
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    axs[0, 0].plot(city_data['Month'], city_data['AvgTemp'], marker='o', label=city)
axs[0, 0].set_title('Average Monthly Temperature by City')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Average Temperature (°C)')
axs[0, 0].legend()
axs[0, 0].grid()

# Subplot 2: Bar Plot
bars = axs[0, 1].bar(total_rainfall.index, total_rainfall.values, color=colors)
axs[0, 1].set_title('Total Rainfall from January to March by City')
axs[0, 1].set_xlabel('City')
axs[0, 1].set_ylabel('Total Rainfall (mm)')
axs[0, 1].grid(axis='y')
for bar in bars:
    yval = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center')

# Subplot 3: Scatter Plot
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    axs[1, 0].scatter(city_data['AvgTemp'], city_data['SunshineHours'], color=city_colors[city], label=city)
axs[1, 0].set_title('Relationship between Average Temperature and Sunshine Hours')
axs[1, 0].set_xlabel('Average Temperature (°C)')
axs[1, 0].set_ylabel('Sunshine Hours')
axs[1, 0].legend()
axs[1, 0].grid()

# Leave axs[1, 1] empty
axs[1, 1].axis('off')

# Add suptitle and save before showing
fig.suptitle('Weather and Sensor Data Visualizations', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.savefig('matplotlib_assignment_output.png', dpi=300)
plt.show()

# --- Sensor Data Visualization ---
plt.figure(figsize=(10, 6))
time = sensor_data[:, 0]
markers = ['o', 's', '^']
linestyles = ['-', '--', '-.']
for i in range(1, 4):
    plt.plot(time, sensor_data[:, i], marker=markers[i-1], linestyle=linestyles[i-1], label=f'Sensor {i}')
plt.title('Sensor Readings Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Sensor Reading')
plt.legend()
plt.grid()
plt.show()
