# ============================================================
# 📋 INDEX
# ============================================================
# 1. Import Library                    → Line 7
# 2. Create Employee Dataset (Dict)    → Line 10
# 3. Build DataFrame                   → Line 20
# 4. Display Sample DataFrame          → Line 23
# 5. Display Descriptive Statistics    → Line 27
# 6. Describe Output — Reference Notes → Line 31
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
# 4️⃣ DISPLAY SAMPLE DATAFRAME
# Quick visual check to confirm data loaded correctly
# Shows all 8 rows with auto-generated index (0–7)
# ─────────────────────────────────────────
print("Sample Data Frame:")
print(df)


# ─────────────────────────────────────────
# 5️⃣ DISPLAY DESCRIPTIVE STATISTICS
# df.describe() → auto-summarises all numeric columns
# Skips non-numeric columns (e.g. 'Name') automatically
# Covers: Age, Salary, Performance_Score
# ─────────────────────────────────────────
print("\nDescriptive Statistics:")
print(df.describe())


# ─────────────────────────────────────────
# 6️⃣ DESCRIBE OUTPUT — REFERENCE NOTES
# A full legend for reading df.describe() output:
#
# 🔢 count → total non-null values in the column
# 📐 mean  → arithmetic average of all values
# 📉 std   → standard deviation (how spread out values are)
#              • Small std = data clustered near the mean (consistent)
#              • Large std = data widely spread (varied)
# ⬇️  min   → smallest value in the column
# 📊 25%   → 1st quartile: 25% of values fall below this
# 📊 50%   → median: the true middle value (not affected by outliers)
# 📊 75%   → 3rd quartile: 75% of values fall below this
# ⬆️  max   → largest value in the column
# ─────────────────────────────────────────
"""
Describe output explanation:
- count: Number of non-null values
- mean: Average of all values
- std: Standard deviation (spread of data)
- min: Minimum value
- 25%: First quartile (lowest 25% threshold)
- 50%: Median (middle value)
- 75%: Third quartile (top 25% threshold)
- max: Maximum value

Standard Deviation (std):
- Small std = Data points close to mean (consistent)
- Large std = Data points spread out (varied)
"""