# ============================================================
# 📌 INDEX (with Line Numbers)
# ============================================================
# 📦 Import Library ---------------------------- Line 21
# 🧾 Create Dataset (Dictionary) --------------- Lines 25–40
# 🏗️ Convert Dictionary to DataFrame ---------- Line 43
# 📊 Display Original Data -------------------- Line 47
# 🧹 Handle Missing Data (dropna) ------------- Line 52
# 📊 Display Cleaned Data --------------------- Line 57
# ============================================================


# ============================================================
# 🧠 Handling Missing Data
# ============================================================
# This script demonstrates how to identify and remove missing
# values from a dataset using pandas.


#dropna()
# 🧹 dropna(): Removes rows that contain missing (NaN) values.

import pandas as pd
# 📦 Importing pandas library for data manipulation and analysis.


data = {
    "Name": ['Ram', 'None', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    # 🧾 Column: Name
    # ⚠️ 'None' here is a STRING, not an actual missing value.

    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    # 🧾 Column: Age
    # ❗ Contains real missing value (None → becomes NaN in pandas)

    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    # 🧾 Column: Salary
    # ❗ Contains missing value

    "Performance_Score": [85, None, 78, 92, 88, 95, 80, 89]
    # 🧾 Column: Performance Score
    # ❗ Contains missing value
}


df = pd.DataFrame(data)
# 🏗️ Converts dictionary into a structured DataFrame (table format).


print(df)
# 📊 Displays original dataset
# 🔍 Rows with missing values (NaN) will be visible here.


df.dropna(inplace=True)
# 🧹 Removes ALL rows that contain ANY missing values
# ⚙️ inplace=True → modifies the original DataFrame directly


print(df)
# 📊 Displays cleaned dataset
# ✅ Only rows WITHOUT missing values remain