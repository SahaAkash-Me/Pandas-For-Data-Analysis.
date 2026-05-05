# ================================================
# INDEX - Pandas Concatenation Tutorial
# ================================================
# Line Numbers (for quick navigation):
#
# 1-10    → Introduction & Setup
# 12-25   → Creating Region1 DataFrame
# 27-40   → Creating Region2 DataFrame
# 45-55   → 1. Vertical Concatenation (Rows)   📚
# 60-70   → 2. Horizontal Concatenation (Columns)   ↔️
#
# Tip: Use Ctrl + F with section names or line numbers to jump easily.
# ================================================


# ================================================
# INTRODUCTION
# ================================================
# Today's Learning: Concatenation in Pandas using pd.concat()
# 
# Concatenation is used to combine two or more DataFrames.
# Unlike merge/join, concat combines data based on position (not keys).
# Two main types:
#   • Vertical (along rows)  → axis=0 (default)
#   • Horizontal (along columns) → axis=1

import pandas as pd


# ================================================
# 1. CREATING SAMPLE DATAFRAMES
# ================================================

#region1
df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ['Gopal', 'Raju']
})
# Explanation: DataFrame containing customers from Region 1


#region2
df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ['Shyam', 'Baburao']
})
# Explanation: DataFrame containing customers from Region 2


# ================================================
# 2. VERTICAL CONCATENATION (Stack Rows) 📚
# ================================================
# Combines DataFrames one below the other (row-wise)
# Default behavior of pd.concat() is vertical (axis=0)
# ignore_index=True resets the index

#concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concat)
# Result: 4 rows × 2 columns. All customers stacked vertically.


# ================================================
# 3. HORIZONTAL CONCATENATION (Side by Side) ↔️
# ================================================
# Combines DataFrames column-wise (axis=1)
# Useful when you want to add columns from different DataFrames
# ignore_index=True will create new column names (0,1,2,...)

#concatenate horizontally
df_concat = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(df_concat)
# Result: 2 rows × 4 columns. Columns from both DataFrames placed side by side.