
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Consider only successful bookings
successful_rides = df[df["Booking_Status"] == "Success"].copy()

# Calculate revenue by payment method
payment_revenue = successful_rides.groupby(
    "Payment_Method"
)["Booking_Value"].sum().sort_values(ascending=False)

# Calculate total revenue
total_revenue = successful_rides["Booking_Value"].sum()

# Display results
print("\n===== REVENUE BY PAYMENT METHOD =====")
print(payment_revenue)

print("\nTotal Revenue from Successful Rides: ₹",
      f"{total_revenue:,.2f}")

print("\nHighest Revenue Payment Method:",
      payment_revenue.idxmax())

print("Highest Payment Method Revenue: ₹",
      f"{payment_revenue.max():,.2f}")

# Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(payment_revenue.index, payment_revenue.values)

plt.title("Revenue by Payment Method - July 2024")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue (₹)")

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
    "OUTPUT/revenue_by_payment_method.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nRevenue chart saved successfully!")
