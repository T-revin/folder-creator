# Folder Creator Project

This project contains Python scripts to:

1. **Create folders and subfolders** based on an Excel file.
2. **Sort items into subfolders** based on their names.

---

## ✅ Prerequisites

- Python 3 installed on your computer.
- [VS Code](https://code.visualstudio.com/) or any text editor.
- Install required Python packages:

```bash
python -m pip install pandas
pip install pandas openpyxl
```

---

## ✅ Files in This Repository

- `create_folders.py` → Creates folders and subfolders from an Excel file.
- `sort_items.py` → Moves files into the correct subfolders based on their names.

---

## ✅ How It Works

### **Excel File Structure**

Excel file should look like this:

| Path                       |
| -------------------------- |
| HR/Training/Level 4/401/A1 |
| HR/Payroll/Level 5/501/A2  |
| IT/Hardware/Specs/Version1 |

- Each row contains a full folder path separated by `/`.
- This supports unlimited nesting.

---

### Example Behavior:

- `HR/Training/Level 4/401/A1` → Creates nested folders: HR → Training → Level 4 → 401 → A1.

## ✅ How to Run `create_folders.py`

1. Open **VS Code**.
2. Place `create_folders.py` in your project folder.
3. Update the script with your Excel file path and output folder path:

```python
excel_file = r"C:\Users\User\Downloads\nested_paths.xlsx"
base_dir = r"C:\Users\User\Downloads\output_folders"
```

4. Run the script:

```bash
python create_folders.py
```

4. When prompted:
   - Enter the full path to your Excel file (e.g., `C:\Users\User\test.xlsx`).
   - Enter the full path where you want the folders created (e.g., `C:\Users\User\output_folders`).

The script will create the folder structure based on your Excel file.

---

## ✅ How to Run `sort_items.py`

- Place all files you want to sort in a folder called `Items`.
- Filenames should follow the pattern:
  - `TopFolder_Subfolder` for one level.
  - `TopFolder_Subfolder_SubSubfolder` for multiple levels.
- The script will create nested folders if needed.

### ✅ Unlimited nesting:

- "\_" character indicates a new level: `HR_Training_JohnSmith.docx` → goes to `HR/Training/JohnSmith`.

### ✅ Dash Handling in Filenames

The `sort_items.py` script supports filenames with additional identifiers after a dash (`-`).
Anything after the dash is ignored for sorting purposes.

**Example:**

- `HR_Training-50.docx` → moved to `output_folders/HR/Training`
- `IT_Hardware-Extra.pdf` → moved to `output_folders/IT/Hardware`

This allows you to keep extended names without affecting folder assignment.

---

## ✅ Notes

- Use **raw strings** for Windows paths (prefix with `r`), e.g., `r"C:\Users\User\test.xlsx"`.
- If a folder does not exist, the script will skip the file.

---

## ✅ License

This project is open-source. Feel free to modify and share.
