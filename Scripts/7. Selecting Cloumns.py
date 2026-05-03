# ============================================================
# 📋 INDEX
# ============================================================
# 1. Import Library                        → Line 7
# 2. Create Employee Dataset (Dict)        → Line 10
# 3. Build DataFrame                       → Line 20
# 4. Display Full DataFrame                → Line 23
# 5. Method 1 — Select Single Column      → Line 27
# 6. Method 2 — Single Column (Variable)  → Line 32
# 7. Method 3 — Select Multiple Columns   → Line 37
# 8. Column Selection Reference Notes     → Line 42
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
# 4️⃣ DISPLAY FULL DATAFRAME
# Baseline view — confirm all 8 rows and
# 4 columns are present before selecting
# ─────────────────────────────────────────
print("Sample Data Frame:")
print(df)


# ─────────────────────────────────────────
# 5️⃣ METHOD 1 — SELECT SINGLE COLUMN (Direct Print)
# df['ColumnName'] → returns a Series (1D structure)
# Series includes the index + values of that column only
# No variable assigned — directly printed
# ─────────────────────────────────────────
print("\nNames: (Single column returns series)")
names = df['Name']
print(names)


# ─────────────────────────────────────────
# 6️⃣ METHOD 2 — SELECT SINGLE COLUMN (Via Variable)
# Same as Method 1 — but column stored in a variable first
# Best practice when reusing the column multiple times
# Avoids repetitive df['Name'] calls across the script
# ─────────────────────────────────────────
print("\nNames (using variable):")
name_col = df['Name']
print(name_col)


# ─────────────────────────────────────────
# 7️⃣ METHOD 3 — SELECT MULTIPLE COLUMNS
# df[['Col1', 'Col2']] → returns a DataFrame (2D structure)
# Double brackets [[ ]] are required:
#   → Outer [ ] = column accessor
#   → Inner [ ] = Python list of column names
# Order of columns in the list = order in output
# ─────────────────────────────────────────
print("\nSubset with Name and Salary:")
subset = df[['Name', 'Salary']]
print(subset)


# ─────────────────────────────────────────
# 8️⃣ COLUMN SELECTION — REFERENCE NOTES
#
# 🔹 Single Column → df['ColumnName']
#   → Returns: Series (1D — index + values)
#   → Use when working with one column at a time
#   → Output has no column header label in display
#
# 🔷 Multiple Columns → df[['Col1', 'Col2']]
#   → Returns: DataFrame (2D — rows + columns)
#   → Always use double brackets [[ ]]
#   → Pass a Python list of column name strings
#   → Column order in output matches list order
#
# ⚠️  Common Mistake:
#   → df['Name', 'Salary']   ❌ → throws KeyError
#   → df[['Name', 'Salary']] ✅ → correct syntax
# ─────────────────────────────────────────
"""
Single column selection:
- df['ColumnName'] returns Series
- Use when working with one column

Multiple column selection:
- df[['Col1', 'Col2']] returns DataFrame
- Use double brackets [[ ]]
- Pass list of column names
"""