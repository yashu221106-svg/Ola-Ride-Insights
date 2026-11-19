
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Filter rides marked as incomplete
incomplete_rides = df[
    df["Incomplete_Rides"] == "Yes"
].copy()

# Count incomplete ride reasons
incomplete_reasons = (
    incomplete_rides["Incomplete_Rides_Reason"]
    .value_counts()
)

print("\n===== INCOMPLETE RIDES ANALYSIS =====")

print("\nTotal Rides Marked as Incomplete:",
      len(incomplete_rides))

print("\nIncomplete Ride Reasons:")
print(incomplete_reasons)

print("\nBooking Status of Incomplete Rides:")
print(incomplete_rides["Booking_Status"].value_counts())

if not incomplete_reasons.empty:
    print("\nMost Common Incomplete Ride Reason:",
          incomplete_reasons.idxmax())

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    incomplete_reasons.index,
    incomplete_reasons.values
)

plt.title("Reasons for Incomplete Rides")
plt.xlabel("Incomplete Ride Reason")
plt.ylabel("Number of Rides")
plt.xticks(rotation=20, ha="right")

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/incomplete_ride_reasons.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nIncomplete ride chart saved successfully!")
