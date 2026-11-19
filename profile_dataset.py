
import pandas as pd

file_path = "data/OLA_DataSet (1).xlsx"
df = pd.read_excel(file_path, sheet_name="July")

print("\n===== BOOKING STATUS COUNTS =====")
print(df["Booking_Status"].value_counts(dropna=False))

print("\n===== VEHICLE TYPE COUNTS =====")
print(df["Vehicle_Type"].value_counts(dropna=False))

print("\n===== PAYMENT METHOD COUNTS =====")
print(df["Payment_Method"].value_counts(dropna=False))

print("\n===== CANCELLATION VALUES =====")
print("Customer cancellations:")
print(df["Canceled_Rides_by_Customer"].value_counts(dropna=False))

print("\nDriver cancellations:")
print(df["Canceled_Rides_by_Driver"].value_counts(dropna=False))

print("\n===== INCOMPLETE RIDE VALUES =====")
print(df["Incomplete_Rides"].value_counts(dropna=False))

print("\n===== MISSING VALUES BY BOOKING STATUS =====")
print(
    df.groupby("Booking_Status")[
        ["V_TAT", "C_TAT", "Payment_Method",
         "Driver_Ratings", "Customer_Rating",
         "Incomplete_Rides"]
    ].apply(lambda x: x.isnull().sum())
)

print("\n===== NUMERICAL SUMMARY =====")
print(df[[
    "Booking_Value",
    "Ride_Distance",
    "V_TAT",
    "C_TAT",
    "Driver_Ratings",
    "Customer_Rating"
]].describe())

print("\n===== DATE RANGE =====")
print("Start Date:", df["Date"].min())
print("End Date:", df["Date"].max())

print("\n===== PROFILE COMPLETED =====")
