
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Filter driver-cancelled rides
driver_cancellations = df[
    df["Booking_Status"] == "Canceled by Driver"
].copy()

# Count cancellation reasons
cancellation_reasons = (
    driver_cancellations["Canceled_Rides_by_Driver"]
    .value_counts()
)

print("\n===== DRIVER CANCELLATION REASONS =====")
print(cancellation_reasons)

print("\nTotal Driver Cancellations:",
      len(driver_cancellations))

print("\nMost Common Cancellation Reason:",
      cancellation_reasons.idxmax())

# Create bar chart
plt.figure(figsize=(11, 6))

plt.bar(
    cancellation_reasons.index,
    cancellation_reasons.values
)

plt.title("Driver Ride Cancellation Reasons")
plt.xlabel("Cancellation Reason")
plt.ylabel("Number of Cancellations")
plt.xticks(rotation=25, ha="right")

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/driver_cancellation_reasons.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDriver cancellation chart saved successfully!")
