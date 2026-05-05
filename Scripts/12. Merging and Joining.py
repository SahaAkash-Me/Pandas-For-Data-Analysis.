# ================================================
# INDEX - Pandas DataFrame Joins Tutorial
# ================================================
# Line Numbers (approximate for quick navigation):
#
# 1-10    → Introduction & Setup
# 12-20   → Creating Customer DataFrame
# 22-30   → Creating Orders DataFrame
# 35-45   → 1. Inner Join          🔄
# 50-60   → 2. Outer Join (Full)   🌐
# 65-75   → 3. Left Join           ⬅️
# 80-90   → 4. Right Join          ➡️
# 95-105  → 5. Cross Join          ❌ (Cartesian)
#
# Tip: Use Ctrl+F with section names or line numbers to jump quickly.
# ================================================


# ================================================
# INTRODUCTION
# ================================================
# Today's Learning: Different types of Joins in Pandas
# We will use two sample DataFrames to demonstrate:
# - Inner, Outer, Left, Right, and Cross Joins
# Explanation: Joins combine data from two or more tables based on related columns.
# Pandas uses pd.merge() for this, similar to SQL JOIN operations.


import pandas as pd

# ================================================
# 1. CREATING SAMPLE DATAFRAMES
# ================================================

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})
# Explanation: This DataFrame contains customer details.
# CustomerID 3 (Kalpesh) has no orders → useful to see join behavior.

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})
# Explanation: This DataFrame contains order details.
# CustomerID 4 has an order but is not in customers → useful for right/outer joins.


# ================================================
# 2. INNER JOIN 🔄
# ================================================
# Keeps ONLY matching records from both DataFrames
# Like SQL: INNER JOIN

# inner join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
print('inner join')
print(df_merged)
# Result: Only CustomerID 1 and 2 will appear (common records)


# ================================================
# 3. OUTER JOIN (FULL JOIN) 🌐
# ================================================
# Keeps ALL records from both DataFrames
# NaN values filled for non-matching rows
# Like SQL: FULL OUTER JOIN

# outer join (full join equivalent)
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print('\nouter join')
print(df_merged)
# Result: All CustomerIDs 1,2,3,4 will appear


# ================================================
# 4. LEFT JOIN ⬅️
# ================================================
# Keeps ALL records from LEFT DataFrame (customers)
# Matching records from right, NaN if no match
# Like SQL: LEFT JOIN

# left join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print('\nleft join')
print(df_merged)
# Result: All customers kept, Kalpesh will have NaN for OrderAmount


# ================================================
# 5. RIGHT JOIN ➡️
# ================================================
# Keeps ALL records from RIGHT DataFrame (orders)
# Matching records from left, NaN if no match
# Like SQL: RIGHT JOIN

# right join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print('\nright join')
print(df_merged)
# Result: All orders kept, CustomerID 4 will have NaN for Name


# ================================================
# 6. CROSS JOIN ❌ (Cartesian Product)
# ================================================
# Every row from first DataFrame paired with every row from second
# No 'on' parameter needed
# Warning: Can create very large results (3x3 = 9 rows here)

# cross join (REMOVE 'on')
df_merged = pd.merge(df_customers, df_orders, how="cross")
print('\ncross join')
print(df_merged)
# Result: 3 customers × 3 orders = 9 combinations