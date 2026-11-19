import pandas as pd

# 1. Load the original dataset
file_path = "data/OLA_DataSet (1).xlsx"
df = pd.read_excel(file_path, sheet_name="July")

print("Original dataset shape:", df.shape)

# 2. Remove unwanted spaces from column names
df.columns = df.columns.str.strip()

# 3. Remove unwanted spaces from text values
text_columns = df.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    df[col] = df[col].map(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# 4. Convert Date column into proper datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 5. Check missing values after cleaning
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# 6. Validate the cleaned dataset
print("\n===== CLEANED DATASET VALIDATION =====")
print("Rows and Columns:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())
print("Duplicate Booking IDs:", df["Booking_ID"].duplicated().sum())
print("Invalid Dates:", df["Date"].isnull().sum())

# 7. Save as a separate CSV file
output_path = "data/OLA_Cleaned_Data.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_path)