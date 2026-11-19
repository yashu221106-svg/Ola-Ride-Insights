
import pandas as pd

file_path = "data/OLA_DataSet (1).xlsx"
df = pd.read_excel(file_path, sheet_name="July")

print("\n===== BOOKING STATUS vs INCOMPLETE RIDES =====")
print(pd.crosstab(
    df["Booking_Status"],
    df["Incomplete_Rides"],
    dropna=False
))

print("\n===== ZERO DISTANCE BY BOOKING STATUS =====")
print(pd.crosstab(
    df["Booking_Status"],
    df["Ride_Distance"].eq(0)
))

print("\n===== INCOMPLETE RIDE DETAILS =====")
print(
    df[df["Incomplete_Rides"] == "Yes"][
        ["Booking_ID", "Booking_Status",
         "Incomplete_Rides_Reason", "Ride_Distance",
         "Booking_Value"]
    ].head(10).to_string(index=False)
)

print("\n===== INCOMPLETE RIDE REASONS =====")
print(df["Incomplete_Rides_Reason"].value_counts(dropna=False))

print("\n===== DATA QUALITY CHECK COMPLETED =====")
