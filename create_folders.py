import pandas as pd
import os

# Load Excel file
excel_file = r"C:\Users\User\downloads\test_nest.xlsx" # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Base directory where folders will be created
base_dir = r"C:\Users\User\downloads\output_folders" # Replace with your desired output directory

# Ensure base directory exists
os.makedirs(base_dir, exist_ok=True)

# Loop through each path in the Excel file
for path in df.iloc[:, 0]:  # Use first colum in Excel file
    if pd.isna(path):
        continue
    # Split the path into parts
    parts = str(path).strip().split('/')
    # Build nested folder structure
    current_path = base_dir
    for part in parts:
        current_path = os.path.join(current_path, part)
        os.makedirs(current_path, exist_ok=True)


print("Top folders and subfolders created successfully!")
