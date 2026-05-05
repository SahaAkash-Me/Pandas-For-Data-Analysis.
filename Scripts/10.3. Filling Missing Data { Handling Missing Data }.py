# ============================================================
# 📌 INDEX (with Line Numbers)
# ============================================================
# 📦 Import Library ---------------------------- Line 23
# 🧾 Create Dataset (Dictionary) --------------- Lines 27–42
# 🏗️ Convert Dictionary to DataFrame ---------- Line 45
# 📊 Display Original Data -------------------- Line 49
# 🧹 Fill Missing Values (Basic) -------------- Lines 53–58
# 📊 Display After Basic Fill ----------------- Line 60
# 📈 Fill Missing Values with Mean ----------- Lines 64–69
# 📊 Display Final Data ----------------------- Line 71
# ============================================================


# ============================================================
# 🧠 Handling Missing Data using fillna()
# ============================================================
# This script demonstrates different ways to handle missing data
# by filling values instead of removing them.


#fillna()
#fillna(value, inplace=True)
# 🧹 fillna(): Replaces missing (NaN) values with a specified value

import pandas as pd
# 📦 Importing pandas library for data handling


data = {
    "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    # 🧾 Column: Name
    # ❗ Contains missing value (None → treated as NaN)

    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    # 🧾 Column: Age
    # ❗ Contains missing value

    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    # 🧾 Column: Salary
    # ❗ Contains missing value

    "Performance_Score": [85, None, 78, 92, 88, 95, 80, 89]
    # 🧾 Column: Performance Score
    # ❗ Contains missing value
}


df = pd.DataFrame(data)
# 🏗️ Converts dictionary into DataFrame (tabular format)


print(df)
# 📊 Displays original dataset with missing values (NaN)


df['Name'] = df['Name'].fillna('').astype(str)
# 🧹 Fills missing values in 'Name' column with empty string ''
# 🔤 Converts entire column to string type for consistency

df.fillna(0, inplace=True)
# 🧹 Fills ALL remaining missing values in DataFrame with 0
# ⚙️ inplace=True → modifies original DataFrame directly

print(df)
# 📊 Displays dataset after basic filling
# ✅ No NaN values remain (all replaced with '' or 0)


df['Age'].fillna(df['Age'].mean(), inplace=True)
# 📈 Attempts to fill missing values in 'Age' with mean value
# ⚠️ But no effect here because NaNs were already replaced with 0

df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# 📈 Attempts to fill missing values in 'Salary' with mean
# ⚠️ Again, no effect since no NaNs remain

print(df)
# 📊 Final dataset display
# 🧾 Shows fully cleaned data (no missing values)