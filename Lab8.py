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
