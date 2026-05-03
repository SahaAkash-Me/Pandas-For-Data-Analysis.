# ============================================================
# 📋 INDEX
# ============================================================
# 1. Import Library                  → Line 7
# 2. Load Large JSON Dataset         → Line 10
# 3. Display Info (Large Dataset)    → Line 13
# 4. Create Small Sample DataFrame   → Line 17
# 5. Display Info (Small Dataset)    → Line 26
# 6. Info Output Reference Notes     → Line 30
# ============================================================


# ─────────────────────────────────────────
# 1️⃣ IMPORT LIBRARY
# pandas → core data manipulation library
# 'pd' is the standard alias used globally
# ─────────────────────────────────────────
import pandas as pd


# ─────────────────────────────────────────
# 2️⃣ LOAD LARGE JSON DATASET
# pd.read_json() → reads a .json file into a DataFrame
# encoding="latin1" → handles special/non-UTF-8 characters
# Windows absolute path used (D:/...)
# ─────────────────────────────────────────
df = pd.read_json("D:/Python/Pandas/Datasets/sample_Data.json", encoding="latin1")


# ─────────────────────────────────────────
# 3️⃣ DISPLAY DATAFRAME INFO (LARGE DATASET)
# df.info() → prints a structural summary of the DataFrame
# Shows: row count, column names, non-null counts, dtypes
# Critical for spotting nulls and wrong data types early
# ─────────────────────────────────────────
print("Displaying the info of dataset:")
print(df.info())


# ─────────────────────────────────────────
# 4️⃣ CREATE SMALL SAMPLE DATAFRAME
# Built from a plain Python dictionary
#   → keys   = column names
#   → values = lists of equal length (3 items each)
# pd.DataFrame(data) converts it into tabular form
# ─────────────────────────────────────────
data = {
    'Name': ['Ram', 'Shyam', 'Ghanshyam'],
    'Age': [10, 20, 30],
    'City': ['Nagpur', 'Mumbai', 'Delhi']
}
df_small = pd.DataFrame(data)


# ─────────────────────────────────────────
# 5️⃣ DISPLAY INFO (SMALL DATASET)
# Same df.info() applied on a manually created DataFrame
# Easier to read and understand the output on small data
# before applying it to large real-world datasets
# ─────────────────────────────────────────
print("\nInfo of small dataset:")
print(df_small.info())


# ─────────────────────────────────────────
# 6️⃣ INFO OUTPUT — REFERENCE NOTES
# A quick legend for reading df.info() output:
#
# 🔢 RangeIndex     → total number of rows in the DataFrame
# 📊 Data columns   → total number of columns
# ✅ Non-Null Count → how many values exist (non-missing) per column
# 🏷️  Dtype          → data type per column
#                      int64   → whole numbers
#                      float64 → decimal numbers
#                      object  → text / mixed types
# 💾 Memory usage   → RAM consumed by the DataFrame
# ─────────────────────────────────────────
"""
Info output shows:
- RangeIndex: Total number of rows
- Data columns: Total number of columns
- Non-Null Count: Values present in each column
- Dtype: Data types (int64, float64, object)
- Memory usage: Space consumed by DataFrame
"""