
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful rides
successful_rides = df[
    df["Booking_Status"] == "Success"
].copy()

# Calculate total ride distance by vehicle type
vehicle_distance = successful_rides.groupby(
    "Vehicle_Type"
)["Ride_Distance"].sum().sort_values(ascending=False)

# Select top 5 vehicle types
top_5_vehicles = vehicle_distance.head(5)

print("\n===== TOP 5 VEHICLE TYPES BY TOTAL RIDE DISTANCE =====")
print(top_5_vehicles)

print("\nTotal Distance of Top 5 Vehicles:",
      top_5_vehicles.sum())

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_vehicles.index,
    top_5_vehicles.values
)

plt.title("Top 5 Vehicle Types by Total Ride Distance")
plt.xlabel("Vehicle Type")
plt.ylabel("Total Ride Distance (km)")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/top_5_vehicles_distance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTop 5 vehicle distance chart saved successfully!")
