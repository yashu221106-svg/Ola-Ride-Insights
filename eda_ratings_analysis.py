
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful rides
successful_rides = df[df["Booking_Status"] == "Success"].copy()

# Calculate average ratings by vehicle type
ratings = successful_rides.groupby("Vehicle_Type")[
    ["Driver_Ratings", "Customer_Rating"]
].mean()

print("\n===== RATINGS ANALYSIS =====")
print(ratings.round(2))

print("\nOverall Average Driver Rating:",
      round(successful_rides["Driver_Ratings"].mean(), 2))

print("Overall Average Customer Rating:",
      round(successful_rides["Customer_Rating"].mean(), 2))

# Create comparison chart
ratings.plot(kind="bar", figsize=(11, 6))

plt.title("Average Customer vs Driver Ratings by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.xticks(rotation=45)
plt.legend(["Driver Rating", "Customer Rating"])
plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/ratings_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nRatings chart saved successfully!")
