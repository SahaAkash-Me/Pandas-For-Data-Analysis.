# ============================================================================
# 📚 INDEX - Adding, Updating & Removing Columns in Pandas
# ============================================================================
# 
# 📍 Section 1: Dataset Creation (Lines 12-20)
# 📍 Section 2: Adding Columns - Direct Assignment Method (Lines 23-25)
# 📍 Section 3: Adding Columns - Insert Method with Position Control (Lines 27-31)
# 📍 Section 4: Dataset Recreation for Update Operations (Lines 33-42)
# 📍 Section 5: Updating Columns - Single Cell Update (Lines 44-47)
# 📍 Section 6: Updating Columns - Entire Column Transformation (Lines 50-52)
# 📍 Section 7: Removing Columns - Single Column Deletion (Lines 55-59)
# 📍 Section 8: Removing Columns - Multiple Columns Deletion (Lines 62-65)
# 
# ============================================================================

# ============================================================================
# 📍 SECTION 1: DATASET CREATION
# ============================================================================
# Creating an employee dataset to demonstrate column manipulation operations
# Dataset includes Name, Age, Salary, and Performance Score

import pandas as pd

data = {
    'Name': ['Ram', 'Shyam', 'Ghanshyam', 'Dharam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    'Age': [28, 34, 22, 30, 29, 40, 25, 32],
    'Salary': [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    'Performance_Score': [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)


# ============================================================================
# 📍 SECTION 2: ADDING COLUMNS - DIRECT ASSIGNMENT METHOD
# ============================================================================
# Creating a new 'Bonus' column by calculating 10% of each employee's salary
# This method appends the column at the end of the DataFrame
df["Bonus"] = df["Salary"] * 0.1
print(df)

# ============================================================================
# 📍 SECTION 3: ADDING COLUMNS - INSERT METHOD WITH POSITION CONTROL
# ============================================================================
# Using insert() to add a column at a specific position (index 0 = first column)
# Syntax: df.insert(loc, "Column_Name", Value) where loc = desired position
#df.insert(loc,"Column_Name, Value) loc = location

df.insert(0, "ID", [10,20,30,40,50,60,70,80])
print(df)

# ============================================================================
# 📍 SECTION 4: DATASET RECREATION FOR UPDATE OPERATIONS
# ============================================================================
# Re-creating the original DataFrame to demonstrate update operations
# on a fresh dataset without previous modifications

import pandas as pd

data = {
    'Name': ['Ram', 'Shyam', 'Ghanshyam', 'Dharam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    'Age': [28, 34, 22, 30, 29, 40, 25, 32],
    'Salary': [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    'Performance_Score': [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# ============================================================================
# 📍 SECTION 5: UPDATING COLUMNS - SINGLE CELL UPDATE
# ============================================================================
# Using .loc[] for location-based indexing to update a specific cell
# Syntax: df.loc[row_index, column_name] = new_value
# .loc[] → location based indexing
# df.loc[row_index, column_name] = value
df.loc[0, "Salary"] = 55000
print(df)


# ============================================================================
# 📍 SECTION 6: UPDATING COLUMNS - ENTIRE COLUMN TRANSFORMATION
# ============================================================================
# Applying a 5% salary increment to all employees by multiplying the entire
# 'Salary' column by 1.05 (100% + 5% = 105% = 1.05)
# increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print(df)


# ============================================================================
# 📍 SECTION 7: REMOVING COLUMNS - SINGLE COLUMN DELETION
# ============================================================================
# Using drop() with inplace=True to permanently remove the 'Salary' column
# inplace=True modifies the original DataFrame without creating a copy
# Single Column
print('Removed Single Column')
df.drop(columns = ["Salary"], inplace = True)
print(df)


# ============================================================================
# 📍 SECTION 8: REMOVING COLUMNS - MULTIPLE COLUMNS DELETION
# ============================================================================
# Passing a list of column names to drop() to remove multiple columns at once
# Efficient way to clean up DataFrame by removing unnecessary columns
# Multiple Columns at once
print('Removed Multiple Columns At Once')
df.drop(columns = ["Performance_Score","Age"], inplace = True)
print(df)