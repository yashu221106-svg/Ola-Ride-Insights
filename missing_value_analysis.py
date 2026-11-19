import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/OLA_Cleaned_Data.csv")

print("\n===== MISSING VALUE ANALYSIS =====")

# Missing count and percentage
missing_count = df.isnull().sum()
missing_percentage = (missing_count / len(df)) * 100

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage.round(2)
})

print(missing_report[missing_report["Missing_Count"] > 0])

print("\n===== MISSING VALUES BY BOOKING STATUS =====")

columns = [
    "V_TAT",
    "C_TAT",
    "Payment_Method",
    "Driver_Ratings",
    "Customer_Rating",
    "Incomplete_Rides"
]

print(
    df.groupby("Booking_Status")[columns]
    .apply(lambda group: group.isnull().sum())
)

print("\n===== ANALYSIS COMPLETED =====")