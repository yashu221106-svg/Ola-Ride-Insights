
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful bookings
successful_rides = df[df["Booking_Status"] == "Success"].copy()

# Convert Date column into datetime
successful_rides["Date"] = pd.to_datetime(successful_rides["Date"])

# Calculate total ride distance per day
daily_distance = successful_rides.groupby(
    successful_rides["Date"].dt.date
)["Ride_Distance"].sum()

# Display results
print("\n===== DAILY RIDE DISTANCE ANALYSIS =====")
print(daily_distance)

print("\nTotal Ride Distance:", daily_rides.sum() if False else daily_distance.sum())
print("Average Daily Ride Distance:", round(daily_distance.mean(), 2))
print("Highest Daily Ride Distance:", daily_distance.max())
print("Lowest Daily Ride Distance:", daily_distance.min())

print("Highest Distance Date:", daily_distance.idxmax())
print("Lowest Distance Date:", daily_distance.idxmin())

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(
    daily_distance.index,
    daily_distance.values,
    marker="o"
)

plt.title("Total Ride Distance Per Day - July 2024")
plt.xlabel("Date")
plt.ylabel("Total Ride Distance")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/daily_ride_distance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDaily ride distance chart saved successfully!")
