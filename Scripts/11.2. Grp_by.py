# ============================================================
# 📌 INDEX (with Line Numbers) — FINAL CORRECT
# ============================================================
# 📦 Import Library ---------------------------- Line 10
# 🧾 Create Dataset (Dictionary) --------------- Lines 14–24
# 🏗️ Convert to DataFrame --------------------- Line 27
# 🔗 Grouping Data (Single Column) ------------ Line 31
# 🔄 Recreate DataFrame ----------------------- Line 37
# 🔗 Grouping Data (Multiple Columns) --------- Line 41
# 📊 Display Grouped Result ------------------- Line 49
# ============================================================


import pandas as pd
# 📦 Importing pandas library for data analysis


data = {
    "Name": ["Arun", "Varun", "Karun", "Narun", "Marun"],
    # 🧾 Column: Name

    "Age": [28, 34, 22, 34, 28],
    # 🧾 Column: Age
    # 🔁 Contains duplicate values → useful for grouping

    "Salary": [50000, 60000, 45000, 52000, 480000]
    # 🧾 Column: Salary
}


df = pd.DataFrame(data)
# 🏗️ Creating DataFrame from dictionary


grouped = df.groupby("Age")["Salary"].sum()
# 🔗 Grouping data by 'Age'
# ➕ Then selecting 'Salary' column and calculating SUM for each age group
# 📊 Result: Total salary for each unique Age


# Multiple Column Group

df= pd.DataFrame(data)
# 🔄 Recreating DataFrame for fresh grouping

grouped = df.groupby(["Age", "Name"])["Salary"].sum()
# 🔗 Grouping by multiple columns:
#    1️⃣ Age
#    2️⃣ Name
# 📊 Creates hierarchical (multi-level) index

print(grouped)
# 📊 Displays grouped data