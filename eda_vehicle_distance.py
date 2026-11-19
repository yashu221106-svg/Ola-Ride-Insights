
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful bookings
successful_rides = df[df["Booking_Status"] == "Success"].copy()

# Calculate average ride distance by vehicle type
vehicle_distance = successful_rides.groupby(
    "Vehicle_Type"
)["Ride_Distance"].mean().sort_values(ascending=False)

# Display results
print("\n===== AVERAGE RIDE DISTANCE BY VEHICLE TYPE =====")
print(vehicle_distance.round(2))

print("\nVehicle with Highest Average Distance:",
      vehicle_distance.idxmax())

print("Highest Average Distance:",
      round(vehicle_distance.max(), 2))

print("\nVehicle with Lowest Average Distance:",
      vehicle_distance.idxmin())

print("Lowest Average Distance:",
      round(vehicle_distance.min(), 2))

# Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(vehicle_distance.index, vehicle_distance.values)

plt.title("Average Ride Distance by Vehicle Type - July 2024")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Ride Distance")
plt.xticks(rotation=20)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/avg_ride_distance_by_vehicle.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nVehicle distance chart saved successfully!")
