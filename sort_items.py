import os
import shutil

# Paths
base_dir = r"C:\Users\User\downloads\output_folders"  # Where folders were created
items_dir = r"C:\Users\User\downloads\Items"          # Folder containing files to sort

# Loop through files in Items folder
for filename in os.listdir(items_dir):
    file_path = os.path.join(items_dir, filename)

    # Skip if not a file
    if not os.path.isfile(file_path):
        continue

    # Split filename by underscore
    parts = filename.split('_')
    if len(parts) < 2:
        print(f"Skipping {filename}: invalid format")
        continue

    top_folder = parts[0]
    subfolder_raw = parts[1].split('.')[0]  # Remove file extension

    # Remove anything after '-' in subfolder name
    subfolder = subfolder_raw.split('-')[0]

    # Build destination path
    dest_path = os.path.join(base_dir, top_folder, subfolder)

    # Check if destination exists
    if os.path.exists(dest_path):
        # Move file
        shutil.move(file_path, os.path.join(dest_path, filename))
        print(f"Moved {filename} to {dest_path}")
    else:
        print(f"Destination folder not found for {filename}: {dest_path}")

print("Sorting complete!")