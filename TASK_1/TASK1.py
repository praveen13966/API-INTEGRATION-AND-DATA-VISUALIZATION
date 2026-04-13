import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_weather_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast" 
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

data = get_weather_forecast(19.0760, 72.8777) 
if data:
  
    times = pd.to_datetime(data['hourly']['time'])
    temps = data['hourly']['temperature_2m']

    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, color='tab:blue', linewidth=2)
    plt.title("7-Day Temperature Forecast (Mumbai)")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()
