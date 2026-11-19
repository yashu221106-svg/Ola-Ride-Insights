import pandas as pd

# Original dataset path
file_path = "data/OLA_DataSet (1).xlsx"

# Check Excel workbook sheets
excel_file = pd.ExcelFile(file_path)

print("\n===== WORKBOOK SHEETS =====")
print(excel_file.sheet_names)

# Load the main ride dataset
df = pd.read_excel(file_path, sheet_name="July")

print("\n===== DATASET SHAPE =====")
print("Rows and Columns:", df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INSPECTION COMPLETED =====")