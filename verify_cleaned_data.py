import pandas as pd

file_path = "data/OLA_Cleaned_Data.csv"

df = pd.read_csv(file_path)

print("\n===== CLEANED CSV VERIFICATION =====")
print("Dataset Shape:", df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== VERIFICATION COMPLETED =====")