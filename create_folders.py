import pandas as pd
import os

# Load Excel file
excel_file = r"C:\Users\User\downloads\Test_file.xlsx" # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Base directory where folders will be created
base_dir = r"C:\Users\User\downloads\output_folders" # Replace with your desired output directory

# Loop through each row
for index, row in df.iterrows():
    top_folder = str(row[0]).strip()
    top_path = os.path.join(base_dir, top_folder)
    os.makedirs(top_path, exist_ok=True)

    # Loop through subfolder columns
    for subfolder in row[1:]:
        if pd.notna(subfolder):  # Skip empty cells
            subfolder_name = str(subfolder).strip()
            subfolder_path = os.path.join(top_path, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)

print("Top folders and subfolders created successfully!")
