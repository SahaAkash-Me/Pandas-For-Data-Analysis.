# ============================================================
# 📋 INDEX
# ============================================================
# 1. Import Library                  → Line 7
# 2. Create Employee Dataset (Dict)  → Line 10
# 3. Build DataFrame                 → Line 20
# 4. Display DataFrame               → Line 23
# 5. Display Shape                   → Line 26
# 6. Display Column Names            → Line 29
# 7. Shape & Columns Reference Notes → Line 32
# ============================================================


# ─────────────────────────────────────────
# 1️⃣ IMPORT LIBRARY
# pandas → core data manipulation library
# 'pd' is the standard alias used globally
# ─────────────────────────────────────────
import pandas as pd


# ─────────────────────────────────────────
# 2️⃣ CREATE EMPLOYEE DATASET (DICTIONARY)
# 8 employees with 4 attributes each:
#   → Name             : employee names (text / object)
#   → Age              : employee ages (int)
#   → Salary           : monthly salary in ₹ (int)
#   → Performance_Score: KPI score out of 100 (int)
# All lists are equal length (8 items) — required for DataFrame
# ─────────────────────────────────────────
data = {
    'Name': ['Ram', 'Shyam', 'Ghanshyam', 'Dharam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    'Age': [28, 34, 22, 30, 29, 40, 25, 32],
    'Salary': [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    'Performance_Score': [85, 90, 78, 92, 88, 95, 80, 89]
}


# ─────────────────────────────────────────
# 3️⃣ BUILD DATAFRAME
# pd.DataFrame(data) → converts dict into 2D tabular structure
# Rows = employees | Columns = attributes
# ─────────────────────────────────────────
df = pd.DataFrame(data)


# ─────────────────────────────────────────
# 4️⃣ DISPLAY DATAFRAME
# Quick visual check to confirm all 8 rows
# and 4 columns loaded correctly
# ─────────────────────────────────────────
print(df)


# ─────────────────────────────────────────
# 5️⃣ DISPLAY SHAPE
# df.shape → returns a tuple (rows, columns)
# No parentheses needed — shape is a property, not a method
# Output here: (8, 4) → 8 employees, 4 attributes
# ─────────────────────────────────────────
print(f"\nShape: {df.shape}")


# ─────────────────────────────────────────
# 6️⃣ DISPLAY COLUMN NAMES
# df.columns → returns an Index object listing all column names
# Useful to verify column names before accessing or renaming them
# Output: Index(['Name', 'Age', 'Salary', 'Performance_Score'], dtype='object')
# ─────────────────────────────────────────
print(f"\nColumn Names: {df.columns}")


# ─────────────────────────────────────────
# 7️⃣ SHAPE & COLUMNS — REFERENCE NOTES
#
# 📐 df.shape
#   → Returns tuple: (rows, columns)
#   → (8, 4) = 8 rows and 4 columns
#   → First number always = rows
#   → Second number always = columns
#   → Property, not a method → no () needed
#
# 🏷️  df.columns
#   → Returns Index object with all column names
#   → Use to check if required columns exist in dataset
#   → Use as a reference before renaming or accessing columns
#   → Convert to list if needed: list(df.columns)
# ─────────────────────────────────────────
"""
Shape returns tuple: (rows, columns)
- df.shape = (8, 4) means 8 rows and 4 columns

Columns returns Index object with all column names
- Use to check if required columns exist
- Use to rename or access specific columns
"""