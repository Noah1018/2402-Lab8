import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df_weather = pd.read_csv("city_weather.csv")
sensor_data = np.loadtxt("sensor_readings.csv",
delimiter=",", skiprows=1)

print("Weather DataFrame Head:")
print(df_weather.head())
print("\nWeather DataFrame Info:")
print(df_weather.info())
print("\nWeather DataFrame Shape:", df_weather.shape)
print("\nSensor Data Shape:", sensor_data.shape)


#plot x axis month y axis avg temperature one line per city include legend labels title
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


#plot x axis city y axis tptal raninfall (sum across months) distinct colors for bar 
#data labels above bars title total rainfall (jan-mar)
total_rainfall = df_weather.groupby('City')['Rainfall'].sum()
plt.figure(figsize=(8, 5))
bars = plt.bar(total_rainfall.index, total_rainfall.values, color=['blue', 'orange', 'green'])
plt.title('Total Rainfall from January to March by City')
plt.xlabel('City')
plt.ylabel('Total Rainfall (mm)')
plt.grid(axis='y')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')
plt.show()

#scatter plot x axis avg temp  y axis sunshine hours color code by city 
#title relationship between temperature and sunshine
plt.figure(figsize=(10, 6))
colors = {'Calgary': 'red', 'Vancouver': 'blue', 'Toronto': 'green'}
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    plt.scatter(city_data['AvgTemp'], city_data['SunshineHours'], color=colors[city], label=city)   
plt.title('Relationship between Average Temperature and Sunshine Hours')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Sunshine Hours')
plt.legend()
plt.grid()
plt.show()

#combine all 3 plots into a 2x2 grid of subplots leaving one subplot empty
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
# First plot
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    axs[0, 0].plot(city_data['Month'], city_data['AvgTemp'], marker='o', label=city)    
axs[0, 0].set_title('Average Monthly Temperature by City')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Average Temperature (°C)')
axs[0, 0].legend()
axs[0, 0].grid()
# Second plot
total_rainfall = df_weather.groupby('City')['Rainfall'].sum()
bars = axs[0, 1].bar(total_rainfall.index, total_rainfall.values, color=['blue', 'orange', 'green'])
axs[0, 1].set_title('Total Rainfall from January to March by City')
axs[0, 1].set_xlabel('City')
axs[0, 1].set_ylabel('Total Rainfall (mm)')
axs[0, 1].grid(axis='y')
for bar in bars:
    yval = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')
# Third plot
for city in df_weather['City'].unique():
    city_data = df_weather[df_weather['City'] == city]
    axs[1, 0].scatter(city_data['AvgTemp'], city_data['SunshineHours'], color=colors[city], label=city)
axs[1, 0].set_title('Relationship between Average Temperature and Sunshine Hours')
axs[1, 0].set_xlabel('Average Temperature (°C)')
axs[1, 0].set_ylabel('Sunshine Hours')
axs[1, 0].legend()
axs[1, 0].grid()


#3 line plots for sensore 1 2 and 3 vs time
#add grid lengend label and custom line styles
#title sensor readings over time
#labels axes properly and use different markers for each line
plt.figure(figsize=(10, 6))
time = sensor_data[:, 0]
for i in range(1, 4):
    plt.plot(time, sensor_data[:, i], marker=['o', 's', '^'][i-1], linestyle=['-', '--', '-.'][i-1], label=f'Sensor {i}')
plt.title('Sensor Readings Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Sensor Reading')
plt.legend()
plt.grid()
plt.show()


#add suptitle to the entire firgues visualizinf weather and sensor data
#adjust layout to prevent overlap
#save final figure as matplotlib_assignment_output.png, dpi 300
fig.suptitle('Weather and Sensor Data Visualizations', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('matplotlib_assignment_output.png', dpi=300)
plt.show()


