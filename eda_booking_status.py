
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Calculate booking status counts and percentages
status_counts = df["Booking_Status"].value_counts()
status_percentages = (status_counts / len(df) * 100).round(2)

# Display analysis
print("\n===== BOOKING STATUS ANALYSIS =====")

summary = pd.DataFrame({
    "Bookings": status_counts,
    "Percentage": status_percentages
})

print(summary)

print("\nTotal Bookings:", len(df))
print("Successful Bookings:", (df["Booking_Status"] == "Success").sum())
print("Unsuccessful Bookings:", (df["Booking_Status"] != "Success").sum())

# Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(status_counts.index, status_counts.values)

plt.title("OLA Booking Status Distribution - July 2024")
plt.xlabel("Booking Status")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=20, ha="right")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height()):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart
plt.savefig(
    "OUTPUT/booking_status_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully!")
