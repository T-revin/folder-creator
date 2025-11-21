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

The script expects an Excel file where **column headers define the folder hierarchy**.

- The **Header Name** determines the nesting level and parent folders.
- The **Row Values** determine the specific subfolders to be created at that level.

---

### **Dynamic Nesting Rules**

There are two ways to define where subfolders are created:

#### **1. Generic (Wildcard) - Apply to ALL**
If you use the **generic level name** (e.g., `Level1`, `Dept`, `Team`) in the header path, the new subfolders will be created inside **EVERY** folder at that level.

**Example:**
- Header: `Dept/Team` (where `Dept` is the generic name for the first level)
- Row Values: `Alpha`, `Beta`
- **Result**: `Alpha` and `Beta` folders are created inside **every** Department folder found.

#### **2. Specific - Apply to ONE**
If you use a **specific folder name** in the header path, the new subfolders will be created **ONLY** inside that specific folder.

**Example:**
- Header: `HR/Policies` (where `HR` is a specific folder created in Level 1)
- Row Values: `2024`, `2025`
- **Result**: `2024` and `2025` folders are created **only** inside the `HR` folder. They will NOT be created in `IT` or `Finance`.

---

### **Example Table**

| Dept | Dept/Team | HR/Policies |
| :--- | :--- | :--- |
| HR | Alpha | 2024 |
| IT | Beta | 2025 |

**Resulting Structure:**
```text
HR/
├── Alpha/
├── Beta/
└── Policies/
    ├── 2024/
    └── 2025/

IT/
├── Alpha/
└── Beta/
```
*(Note: `Policies` is NOT created in `IT` because the header was `HR/Policies`, not `Dept/Policies`)*

---

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
