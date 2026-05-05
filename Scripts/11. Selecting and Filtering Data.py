# ============================================================
# 📌 INDEX (with Line Numbers)
# ============================================================
# 📦 Import Library ---------------------------- Line 5
# 🧾 Create Dataset (Dictionary) --------------- Lines 7–11
# 🏗️ Convert to DataFrame --------------------- Line 13
# 🔽 Sort by Single Column (Age Desc) --------- Line 14
# 📊 Display Sorted Data (Single Column) ------ Lines 15–16
# 🔄 Recreate DataFrame ----------------------- Line 18
# 🔽 Sort by Multiple Columns ----------------- Line 19
# 📊 Display Sorted Data (Multi Column) ------- Lines 20–21
# ============================================================


#sorting data
# 🔽 Topic: Sorting data in pandas using sort_values()

#SORTING DATA 1 COLUMN sort_values()
# 🧹 df.sort_values(by="Column Name", True/False, inplace = True)

import pandas as pd
# 📦 Importing pandas library


data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    # 🧾 Column: Name

    "Age": [28, 34, 22],
    # 🧾 Column: Age

    "Salary": [10000, 20000, 30000]
    # 🧾 Column: Salary
}


df = pd.DataFrame(data)
# 🏗️ Creating DataFrame from dictionary

df.sort_values(by="Age", ascending=False, inplace=True)
# 🔽 Sorting by Age in descending order (highest → lowest)
# ⚙️ inplace=True → modifies original DataFrame

print('Sorted Age by Descending')
# 🖨️ Label for output

print(df)
# 📊 Displays sorted DataFrame (single column sorting)


df = pd.DataFrame(data)
# 🔄 Recreating original DataFrame (reset to unsorted state)

df.sort_values(by=['Age', "Salary"], ascending=[True, False], inplace=True)
# 🔽 Sorting by multiple columns:
#    1️⃣ Age → ascending (lowest → highest)
#    2️⃣ Salary → descending (highest → lowest within same Age)

print('Sorted Age by Descending')
# 🖨️ Label for output (⚠️ message says descending but logic is mixed sort)

print(df)
# 📊 Displays sorted DataFrame (multi-column sorting)