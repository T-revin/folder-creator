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

Your Excel file should look like this:

| TopFolder | Sub1     | Sub2        | Sub3       | Sub4       | Sub5    | Sub6        |
| --------- | -------- | ----------- | ---------- | ---------- | ------- | ----------- |
| HR        | Payroll  | Recruitment | Training   | Benefits   | Reports | Compliance  |
| IT        | Hardware | Software    | Networking | Security   | Support | Projects    |
| Finance   | Accounts | Budget      | Audit      | Compliance | Tax     | Investments |

- Column A = Top-level folder name.
- Columns B–G = Subfolders (all directly under the top folder).

---

## ✅ How to Run `create_folders.py`

1. Open **VS Code**.
2. Place `create_folders.py` in your project folder.
3. Run the script:

```bash
python create_folders.py
```

4. When prompted:
   - Enter the full path to your Excel file (e.g., `C:\Users\User\test.xlsx`).
   - Enter the full path where you want the folders created (e.g., `C:\Users\User\output_folders`).

The script will create the folder structure based on your Excel file.

---

## ✅ How to Run `sort_items.py`

1. Make sure your folders are already created.
2. Place all files you want to sort in a folder called `Items`.
3. Run the script:

```bash
python sort_items.py
```

The script will:

- Read each file name in `Items`.
- Move it to the correct subfolder based on the naming pattern `TopFolder_Subfolder`.

Example:

- `HR_Payroll.docx` → moved to `output_folders/HR/Payroll`

---

## ✅ Notes

- Use **raw strings** for Windows paths (prefix with `r`), e.g., `r"C:\Users\User\test.xlsx"`.
- If a folder does not exist, the script will skip the file.

---

## ✅ License

This project is open-source. Feel free to modify and share.
