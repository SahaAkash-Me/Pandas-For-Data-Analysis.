# ============================================================
# 📋 INDEX
# ============================================================
# 1. Import Library                          → Line 7
# 2. Create Employee Dataset (Dict)          → Line 10
# 3. Build DataFrame                         → Line 20
# 4. Display Full DataFrame                  → Line 23
# 5. Filter — Single Condition               → Line 27
# 6. Filter — Salary Range (AND → &)         → Line 32
# 7. Filter — Multiple Conditions (AND)      → Line 39
# 8. Filter — Multiple Conditions (OR)       → Line 45
# 9. Filtering Syntax Reference Notes        → Line 51
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
# 4 columns are present before filtering
# ─────────────────────────────────────────
print("Sample Data Frame:")
print(df)


# ─────────────────────────────────────────
# 5️⃣ FILTER — SINGLE CONDITION
# df[df['Column'] > value] → Boolean masking
# Step 1: df['Salary'] > 50000 → produces True/False for each row
# Step 2: df[...] → keeps only rows where result is True
# Returns a filtered DataFrame (not a Series)
# ─────────────────────────────────────────
print("\nEmployees with Salary greater than 50000:")
high_salary = df[df['Salary'] > 50000]
print(high_salary)


# ─────────────────────────────────────────
# 6️⃣ FILTER — SALARY RANGE (AND → &)
# Range filter = AND logic applied to the same column twice
#   → First condition  sets the lower bound (> 50000)
#   → Second condition sets the upper bound (< 80000)
# Both conditions wrapped in () — required by pandas
# Returns only rows where Salary falls between the two values
# ─────────────────────────────────────────
print("\nEmployees with Salary greater than 50000 but less than 80000:")
range_filtered = df[(df['Salary'] > 50000) & (df['Salary'] < 80000)]
print(range_filtered)


# ─────────────────────────────────────────
# 7️⃣ FILTER — MULTIPLE CONDITIONS (AND → &)
# Both conditions must be True for a row to be included
# Each condition wrapped in () — required by pandas
# & replaces Python's 'and' keyword inside DataFrame filters
# Output: only rows where Age > 30 AND Salary > 50000
# ─────────────────────────────────────────
print("\nFiltering rows with Salary > 50000 AND Age > 30:")
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print(filtered)


# ─────────────────────────────────────────
# 8️⃣ FILTER — MULTIPLE CONDITIONS (OR → |)
# At least ONE condition must be True to include the row
# | replaces Python's 'or' keyword inside DataFrame filters
# Output: rows where Age > 35 OR Performance_Score > 90
# Wider net than AND — typically returns more rows
# ─────────────────────────────────────────
print("\nEmployees older than 35 OR Performance Score > 90:")
filtered_or = df[(df['Age'] > 35) | (df['Performance_Score'] > 90)]
print(filtered_or)


# ─────────────────────────────────────────
# 9️⃣ FILTERING SYNTAX — REFERENCE NOTES
#
# 🔹 Single Condition:
#   → df[df['Column'] > value]
#   → Evaluates one rule across all rows
#
# 🔵 Range Filter (same column, two bounds):
#   → df[(df['Col'] > low) & (df['Col'] < high)]
#   → Lower bound + Upper bound on one column
#
# 🔷 Multiple AND  →  &
#   → df[(condition1) & (condition2)]
#   → BOTH must be True → stricter, fewer rows returned
#
# 🔶 Multiple OR   →  |
#   → df[(condition1) | (condition2)]
#   → ONE must be True → looser, more rows returned
#
# ⚠️  Critical Rules:
#   → Always wrap each condition in ( ) parentheses
#   → Use & instead of 'and'  ❌ → df[cond1 and cond2]
#   → Use | instead of 'or'   ❌ → df[cond1 or cond2]
#   → Skipping () causes: TypeError: ambiguous truth value
# ─────────────────────────────────────────
"""
Filtering Syntax:
- Single condition: df[df['Column'] > value]
- Range filter: df[(df['Col'] > low) & (df['Col'] < high)]
- Multiple AND: df[(condition1) & (condition2)]
- Multiple OR: df[(condition1) | (condition2)]
Boolean Operators:
- & (AND): Both conditions must be True
- | (OR): At least one condition must be True
- Always use parentheses () around each condition
"""