
import requests  # requests library allow use to interact with web services and APIs 
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta 


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=9)        # Timedelta is a class within the built-in datetime module used to represent a duration or the difference between two points in time. it is use to calculate past and future time.

start_date = week_ago.strftime("%Y-%m-%d")  # strftime : it is used to formate datetime.datetime into formated style.
end_date = today.strftime("%Y-%m-%d")
# start_date = week_ago.strftime("%d/%m/%Y, %H:%M:%S")

url = f"https://api.open-meteo.com/v1/forecast?latitude=25.45&longitude=85.53&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
responses = requests.get(url)
data = responses.json()

# print(data["daily"])

daily_data = data["daily"]


#----------------------------------------------------------------------------------------------

df = pd.DataFrame({
    "Date": daily_data["time"],
    "Maximum Temperature": daily_data["temperature_2m_max"],
    "Minimum Temperature" : daily_data["temperature_2m_min"],
})

df["Date"] = pd.to_datetime(df["Date"])

#----------------------------------------------------------------------------------------------

plt.figure(figsize=(10,6))
plt.plot(df["Date"], df["Maximum Temperature"], marker="o", label="Maximum Temperature")
plt.plot(df["Date"], df["Minimum Temperature"], marker="o", label="Minimum Temperature")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Bakhtiyarpur - Past 10 Days")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("weather_cart.png")
plt.show()

# Saving the file in the form of .csv
if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/bakhtiyarpur_weather.csv", index=False)





# Here is the brief explanation of above lines

plt.figure(                     # This line sets up the drawing canvas before you actually start plotting any data.
    figsize=(10,6),             # plt.figure(): This tells Python, I am about to create a new empty window or page for a graph. figsize=(10, 6): This defines the physical size of that window. The numbers represent (width, height) in inches.
    facecolor='skyblue',        # Changes the background color of the entire figure window.
    dpi=100,                    # Sharp resolution
    edgecolor='black',          # Sets the color of the Border color (visible if frameon is True).
    linewidth=5                 # Thickness of the border
)

plt.plot(
    df["Date"], df["Minimum Temperature"],
    color="#1f77b4",      # Modern blue hex code
    marker="o",             # Circle dots
    markersize=10,          # Big dots
    linestyle="--",         # Dashed line
    linewidth=3,            # Thick line
    label="Minimum Temperature",
)
plt.plot(df["Date"], df["Maximum Temperature"],
    color="crimson",        # Specific shade of red
    marker="s",             # Square dots
    markersize=10,          # Big dots
    linestyle=":",          # Dashed line
    linewidth=2,            # Thick line
    alpha=0.6,              # Slightly see-through
    label="Maximum Temperature",
)

plt.xlabel("Date", fontsize=14, fontweight='bold', color='darkgreen')
plt.ylabel("Temperature (°C)", fontsize=14, fontweight='bold', color='darkgreen')
plt.title('Bakhtiyarpur Weather - Past 7 Days', fontsize=18, color='navy', pad=15)
plt.legend(shadow=True, facecolor='white', fontsize='large')

plt.xticks(rotation=45, color="brown")
plt.tight_layout()

plt.savefig("weather_bkp10.jpg")
plt.show()

