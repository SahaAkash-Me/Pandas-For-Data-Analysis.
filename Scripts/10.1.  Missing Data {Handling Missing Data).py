# ============================================================================
# 📚 INDEX - Missing Data Handling in Pandas (Corrected Line Numbers)
# ============================================================================
# 
# 📍 Section 1: Dataset Creation ---------------- Lines 14–22
# 📍 Section 2: Data Inspection ----------------- Line 28
# 📍 Section 3: Missing Data Detection ---------- Line 36
# 📍 Section 4: Missing Data Count Summary ------ Line 43
# 
# ============================================================================

# ============================================================================
# 📍 SECTION 1: DATASET CREATION
# ============================================================================
# Creating a sample employee dataset with intentional missing values (None)
# to demonstrate pandas missing data detection techniques

import pandas as pd

data = {
    'Name': ['Ram', None, 'Ghanshyam', 'Dharam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    'Age': [28, None, 22, 30, 29, 40, 25, 32],
    'Salary': [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    'Performance_Score': [85, None, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# ============================================================================
# 📍 SECTION 2: DATA INSPECTION
# ============================================================================
# Display the complete DataFrame to visualize where missing values (NaN) exist
print(df)


# ============================================================================
# 📍 SECTION 3: MISSING DATA DETECTION - BOOLEAN MATRIX
# ============================================================================
# Returns a DataFrame of same shape with True where values are missing (NaN)
# and False where values are present
print(df.isnull())

# ============================================================================
# 📍 SECTION 4: MISSING DATA COUNT SUMMARY
# ============================================================================
# Counts total number of missing values in each column
# Useful for quick assessment of data quality
print(df.isnull().sum())