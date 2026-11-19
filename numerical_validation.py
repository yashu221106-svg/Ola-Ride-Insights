import pandas as pd

df = pd.read_csv("data/OLA_Cleaned_Data.csv")

print("\n===== NUMERICAL DATA VALIDATION =====")

# 1. Numerical summary
columns = [
    "Booking_Value",
    "Ride_Distance",
    "V_TAT",
    "C_TAT",
    "Driver_Ratings",
    "Customer_Rating"
]

print("\n===== NUMERICAL SUMMARY =====")
print(df[columns].describe())

# 2. Negative values
print("\n===== NEGATIVE VALUE CHECK =====")
for col in columns:
    print(col, ":", (df[col] < 0).sum())

# 3. Rating validation
print("\n===== RATING VALIDATION =====")
for col in ["Driver_Ratings", "Customer_Rating"]:
    invalid = df[col].notna() & ~df[col].between(1, 5)
    print(col, "outside 1-5:", invalid.sum())

# 4. Zero booking values
print("\n===== ZERO BOOKING VALUE CHECK =====")
print((df["Booking_Value"] == 0).sum())

# 5. Zero ride distance by booking status
print("\n===== ZERO DISTANCE BY STATUS =====")
print(pd.crosstab(
    df["Booking_Status"],
    df["Ride_Distance"].eq(0)
))

print("\n===== NUMERICAL VALIDATION COMPLETED =====")