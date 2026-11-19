import pandas as pd

df = pd.read_csv("data/OLA_Cleaned_Data.csv")

print("\n===== INCOMPLETE RIDE ANALYSIS =====")

print("\nIncomplete Ride Count:")
print(df["Incomplete_Rides"].value_counts(dropna=False))

print("\nIncomplete Rides by Booking Status:")
print(pd.crosstab(
    df["Booking_Status"],
    df["Incomplete_Rides"]
))

print("\nIncomplete Ride Reasons:")
print(df["Incomplete_Rides_Reason"].value_counts(dropna=False))

print("\n===== INCOMPLETE RIDE ANALYSIS COMPLETED =====")