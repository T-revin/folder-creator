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

    # Remove extension for folder parsing
    name_without_ext = os.path.splitext(filename)[0]

    # Split filename by underscore
    parts = filename.split('_')
    if len(parts) < 2:
        print(f"Skipping {filename}: invalid format")
        continue

    # Handle dash in last part (ignore anything after '-')
    cleaned_parts = [p.split('-')[0] for p in parts]

    # Build nested destination path
    dest_folder = base_dir
    for part in cleaned_parts:
        dest_folder = os.path.join(dest_folder, part)

    # Ensure destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # Check if destination exists
    if os.path.exists(dest_path):
        # Move file
        shutil.move(file_path, os.path.join(dest_path, filename))
        print(f"Moved {filename} to {dest_path}")
    else:
        print(f"Destination folder not found for {filename}: {dest_path}")

print("Sorting complete!")