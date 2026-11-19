
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful bookings
successful_rides = df[df["Booking_Status"] == "Success"].copy()

# Calculate total booking value for each customer
customer_revenue = successful_rides.groupby(
    "Customer_ID"
)["Booking_Value"].sum().sort_values(ascending=False)

# Select top 5 customers
top_5_customers = customer_revenue.head(5)

# Display results
print("\n===== TOP 5 CUSTOMERS BY BOOKING VALUE =====")
print(top_5_customers)

print("\nTotal Booking Value of Top 5 Customers: ₹",
      f"{top_5_customers.sum():,.2f}")

print("\nHighest Spending Customer:",
      top_5_customers.idxmax())

print("Highest Booking Value: ₹",
      f"{top_5_customers.max():,.2f}")

# Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(
    top_5_customers.index.astype(str),
    top_5_customers.values
)

plt.title("Top 5 Customers by Booking Value - July 2024")
plt.xlabel("Customer ID")
plt.ylabel("Total Booking Value (₹)")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"₹{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/top_5_customers_by_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTop 5 customers chart saved successfully!")
