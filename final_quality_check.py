
import pandas as pd

file_path = "data/OLA_DataSet (1).xlsx"
df = pd.read_excel(file_path, sheet_name="July")

print("\n===== BOOKING ID CHECK =====")
print("Duplicate Booking IDs:", df["Booking_ID"].duplicated().sum())

print("\n===== NEGATIVE VALUE CHECK =====")
for col in ["Booking_Value", "Ride_Distance", "V_TAT", "C_TAT"]:
    print(col, "Negative values:", (df[col] < 0).sum())

print("\n===== RATING VALIDATION =====")
for col in ["Driver_Ratings", "Customer_Rating"]:
    invalid = df[col].notna() & ~df[col].between(1, 5)
    print(col, "Values outside 1–5:", invalid.sum())

print("\n===== ZERO BOOKING VALUE CHECK =====")
print("Zero booking values:", (df["Booking_Value"] == 0).sum())

print("\n===== ZERO DISTANCE CHECK =====")
print("Zero distance rows:", (df["Ride_Distance"] == 0).sum())

print("\n===== UNIQUE CATEGORY VALUES =====")
for col in ["Booking_Status", "Vehicle_Type", "Payment_Method"]:
    print(f"\n{col}:")
    print(sorted(df[col].dropna().unique()))

print("\n===== FINAL QUALITY CHECK COMPLETED =====")
