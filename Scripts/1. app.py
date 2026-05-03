"""
================================================================================
📚 PANDAS DATA LOADING TUTORIAL - COMPREHENSIVE GUIDE
================================================================================

📋 TABLE OF CONTENTS (Line Numbers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Library Import                                           → Line 28
2. CSV File Loading (Commented)                             → Line 34
3. Excel File Loading (Commented)                           → Line 38
4. JSON File Loading (Active)                               → Line 42
5. Display Output                                           → Line 44
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""

# ================================================================================
# 📦 SECTION 1: LIBRARY IMPORT
# ================================================================================
# 📌 Importing the pandas library for data manipulation and analysis
# 🎯 Purpose: Pandas provides powerful data structures like DataFrame for handling
#             structured data (CSV, Excel, JSON, SQL, etc.)
import pandas as pd


# ================================================================================
# 📂 SECTION 2: CSV FILE LOADING (COMMENTED OUT)
# ================================================================================
# 💾 Method: pd.read_csv()
# 📄 File Format: Comma-Separated Values (.csv)
# 🔤 Encoding: latin1 (handles special characters in Western European languages)
# ⚙️ Note: This line is currently disabled (commented out)
#df = pd.read_csv("D:/Python/Pandas/Datasets/sales_data_sample.csv", encoding="latin1")


# ================================================================================
# 📊 SECTION 3: EXCEL FILE LOADING (COMMENTED OUT)
# ================================================================================
# 💾 Method: pd.read_excel()
# 📄 File Format: Microsoft Excel Spreadsheet (.xlsx)
# ⚙️ Note: This line is currently disabled (commented out)
#df = pd.read_excel("D:/Python/Pandas/Datasets/SampleSuperstore.xlsx")


# ================================================================================
# 🔗 SECTION 4: JSON FILE LOADING (ACTIVE)
# ================================================================================
# 💾 Method: pd.read_json()
# 📄 File Format: JavaScript Object Notation (.json)
# 🔤 Encoding: latin1 (handles special characters)
# ✅ Status: This is the ACTIVE data loading method
# 📥 What it does: Reads JSON data and converts it into a pandas DataFrame
df = pd.read_json("D:/Python/Pandas/Datasets/sample_Data.json", encoding="latin1")

# ================================================================================
# 🖨️ SECTION 5: DISPLAY OUTPUT
# ================================================================================
# 📺 Function: print()
# 🎯 Purpose: Displays the entire DataFrame content in the console
# 📋 Output: Shows all rows and columns of the loaded JSON data
print(df)


"""
================================================================================
📖 DETAILED EXPLANATION OF CONCEPTS
================================================================================

🔹 WHAT IS PANDAS?
   - A powerful Python library for data analysis and manipulation
   - Built on top of NumPy for fast numerical operations
   - Primary data structure: DataFrame (2D labeled data structure)

🔹 WHAT IS A DATAFRAME?
   - A 2-dimensional table with labeled rows and columns
   - Similar to an Excel spreadsheet or SQL table
   - Can store different data types in different columns

🔹 DATA LOADING METHODS LEARNED:
   
   1️⃣ pd.read_csv() 
      - Reads Comma-Separated Values files
      - Most common format for data exchange
      - Fast and lightweight
   
   2️⃣ pd.read_excel()
      - Reads Microsoft Excel files (.xlsx, .xls)
      - Preserves formatting and multiple sheets
      - Requires openpyxl or xlrd library
   
   3️⃣ pd.read_json()
      - Reads JavaScript Object Notation files
      - Flexible nested data structures
      - Common in web APIs and modern applications

🔹 ENCODING PARAMETER:
   - encoding="latin1" handles special characters (é, ñ, ü, etc.)
   - Prevents UnicodeDecodeError when reading non-ASCII characters
   - Alternative encodings: utf-8, cp1252, iso-8859-1

🔹 FILE PATH FORMAT:
   - Windows: Uses forward slashes (/) or double backslashes (\\)
   - Example: "D:/Python/Pandas/Datasets/file.csv"
   - Absolute path: Full path from drive root

================================================================================
"""