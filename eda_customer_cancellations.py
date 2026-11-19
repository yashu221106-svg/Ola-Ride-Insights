
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Filter customer-cancelled rides
customer_cancellations = df[
    df["Booking_Status"] == "Canceled by Customer"
].copy()

# Count cancellation reasons
cancellation_reasons = (
    customer_cancellations["Canceled_Rides_by_Customer"]
    .value_counts()
)

print("\n===== CUSTOMER CANCELLATION REASONS =====")
print(cancellation_reasons)

print("\nTotal Customer Cancellations:",
      len(customer_cancellations))

print("\nMost Common Cancellation Reason:",
      cancellation_reasons.idxmax())

# Create bar chart
plt.figure(figsize=(11, 6))

plt.bar(
    cancellation_reasons.index,
    cancellation_reasons.values
)

plt.title("Customer Ride Cancellation Reasons")
plt.xlabel("Cancellation Reason")
plt.ylabel("Number of Cancellations")
plt.xticks(rotation=25, ha="right")

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/customer_cancellation_reasons.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCustomer cancellation chart saved successfully!")
