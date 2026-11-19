import pandas as pd

df = pd.read_csv("data/OLA_Cleaned_Data.csv")

# Convert date and time columns
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Time"] = pd.to_datetime(
    df["Time"], format="%H:%M:%S", errors="coerce"
).dt.time

print("\n===== DATE VALIDATION =====")
print("Invalid dates:", df["Date"].isna().sum())
print("Earliest date:", df["Date"].min())
print("Latest date:", df["Date"].max())

print("\n===== TIME VALIDATION =====")
print("Invalid times:", df["Time"].isna().sum())
print("Earliest time:", df["Time"].min())
print("Latest time:", df["Time"].max())

print("\n===== DATE AND TIME VALIDATION COMPLETED =====")