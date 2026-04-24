
import os
import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


today = datetime.now()
ten_day_before = today - timedelta(days=9)

today_date = today.strftime("%Y-%m-%d")
ten_day_before_date = ten_day_before.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=25.45&longitude=85.53&start_date={ten_day_before_date}&end_date={today_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

ten_days_data = data["daily"]

df = pd.DataFrame({
    "Date": ten_days_data["time"],
    "Min Temp": ten_days_data["temperature_2m_min"],
    "Max Temp": ten_days_data["temperature_2m_max"]
})

df["Date"] = pd.to_datetime(df["Date"])
df["Average Temp"] = (df["Max Temp"] + df["Min Temp"]) / 2

if not os.path.exists("data"):
    os.makedirs("data")

# df.to_csv("data/temp_data_with_average.csv")

plt.figure(
    figsize=(10,6),
    facecolor="gray",
    edgecolor="black",
)

plt.plot(df["Date"], df["Max Temp"], marker="o", color="red", label="Max Temp")
plt.plot(df["Date"], df["Min Temp"], marker="o", color="b", label="Min Temp")
plt.plot(df["Date"], df["Average Temp"], marker="o", color="g", label="Average Temp")

plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Bakhtiyarpur - Past 10 day Temperature.")
plt.legend(shadow=True, facecolor="white", fontsize="large")

plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("newdata.jpg")
plt.show()

print(f"Average temperature: {df['Average Temp'].mean():.1f}°C")
print("Files saved in 'data' folder")