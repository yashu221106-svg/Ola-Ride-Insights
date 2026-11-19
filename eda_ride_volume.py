
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate daily booking volume
daily_rides = df.groupby(df["Date"].dt.date)["Booking_ID"].count()

# Display daily booking volume
print("\n===== DAILY RIDE VOLUME ANALYSIS =====")
print(daily_rides)

print("\nTotal Bookings:", daily_rides.sum())
print("Average Daily Bookings:", round(daily_rides.mean(), 2))
print("Highest Daily Bookings:", daily_rides.max())
print("Lowest Daily Bookings:", daily_rides.min())

# Find highest and lowest booking dates
print("Date with Highest Bookings:", daily_rides.idxmax())
print("Date with Lowest Bookings:", daily_rides.idxmin())

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(
    daily_rides.index,
    daily_rides.values,
    marker="o"
)

plt.title("Daily Ride Volume - July 2024")
plt.xlabel("Date")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/daily_ride_volume.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDaily ride volume chart saved successfully!")
