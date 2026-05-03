# ============================================================
# 📋 INDEX
# ============================================================
# 1. Topic Reference (head & tail)  → Line 7
# 2. Import Library                 → Line 8
# 3. Load JSON Dataset              → Line 9
# 4. Display First 10 Rows         → Line 12
# 5. Display Last 10 Rows          → Line 16
# 6. Display First 5 Rows (Default) → Line 20
# 7. Display Last 5 Rows (Default)  → Line 24
# ============================================================


# ─────────────────────────────────────────
# 1️⃣ TOPIC REFERENCE
# head() → shows first N rows (default = 5)
# tail() → shows last  N rows (default = 5)
# Pass any number inside () to override default
# ─────────────────────────────────────────
#head() tail()
#head() 5
#tail(n) 5


# ─────────────────────────────────────────
# 2️⃣ IMPORT LIBRARY
# pandas → core library for data manipulation
# 'pd' is the universally used alias
# ─────────────────────────────────────────
import pandas as pd


# ─────────────────────────────────────────
# 3️⃣ LOAD JSON DATASET
# pd.read_json() → reads a .json file into a DataFrame
# encoding="latin1" → handles special/non-UTF-8 characters
#   (common in datasets with regional or legacy encoding)
# The file path uses Windows-style absolute path (D:/...)
# ─────────────────────────────────────────
df = pd.read_json("D:/Python/Pandas/Datasets/sample_Data.json", encoding="latin1")


# ─────────────────────────────────────────
# 4️⃣ DISPLAY FIRST 10 ROWS
# df.head(10) → returns the first 10 rows
# Useful for quickly checking the top of large datasets
# ─────────────────────────────────────────
print("Display 10 rows of First:")
print(df.head(10))


# ─────────────────────────────────────────
# 5️⃣ DISPLAY LAST 10 ROWS
# df.tail(10) → returns the last 10 rows
# Useful for checking if data ends correctly (no missing rows)
# ─────────────────────────────────────────
print("\nDisplay 10 rows of Last:")
print(df.tail(10))


# ─────────────────────────────────────────
# 6️⃣ DISPLAY FIRST 5 ROWS (DEFAULT)
# df.head() with no argument → defaults to 5 rows
# Standard quick-peek method used in EDA
# ─────────────────────────────────────────
print("\nFirst 5 rows (default):")
print(df.head())


# ─────────────────────────────────────────
# 7️⃣ DISPLAY LAST 5 ROWS (DEFAULT)
# df.tail() with no argument → defaults to 5 rows
# Pair with head() to inspect both ends of your dataset
# ─────────────────────────────────────────
print("\nLast 5 rows (default):")
print(df.tail())