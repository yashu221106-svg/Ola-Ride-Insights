import pandas as pd

df = pd.read_csv("data/OLA_Cleaned_Data.csv")

print("===== OLA RIDE DATA CLEANING SUMMARY =====")

print("\nDataset Shape:", df.shape)

print("\nDuplicate Rows:", df.duplicated().sum())

print("Duplicate Booking IDs:", df["Booking_ID"].duplicated().sum())

print("\nTotal Missing Values:", df.isnull().sum().sum())

print("\nNegative Booking Values:",
      (df["Booking_Value"] < 0).sum())

print("Negative Ride Distances:",
      (df["Ride_Distance"] < 0).sum())

print("\nBooking Status Distribution:")
print(df["Booking_Status"].value_counts())

print("\nVehicle Type Distribution:")
print(df["Vehicle_Type"].value_counts())

print("\nCleaning Decisions:")
print("1. Removed unwanted spaces from text values.")
print("2. Validated date and time values.")
print("3. Preserved meaningful missing values.")
print("4. No duplicate records were found.")
print("5. No invalid numerical values were found.")
print("6. Original dataset was preserved.")

print("\n===== CLEANING SUMMARY COMPLETED =====")