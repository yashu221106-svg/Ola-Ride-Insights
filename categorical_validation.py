import pandas as pd

df = pd.read_csv("data/OLA_Cleaned_Data.csv")

print("\n===== CATEGORICAL VALIDATION =====")

categorical_columns = [
    "Booking_Status",
    "Vehicle_Type",
    "Payment_Method",
    "Canceled_Rides_by_Customer",
    "Canceled_Rides_by_Driver",
    "Incomplete_Rides",
    "Incomplete_Rides_Reason"
]

for col in categorical_columns:
    print(f"\n===== {col} =====")
    print("Unique values:", df[col].nunique())
    print(df[col].value_counts(dropna=False))

print("\n===== CATEGORICAL VALIDATION COMPLETED =====")