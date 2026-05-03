"""
================================================================================
📊 PANDAS DATAFRAME CREATION & EXPORT TUTORIAL - COMPREHENSIVE GUIDE
================================================================================

📋 TABLE OF CONTENTS (Line Numbers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Library Import                                           → Line 28
2. Dictionary Data Creation                                 → Line 34
3. DataFrame Creation from Dictionary                       → Line 40
4. Display DataFrame                                        → Line 42
5. Export to CSV (Commented)                                → Line 48
6. Export to Excel (Commented)                              → Line 52
7. Export to JSON (Commented)                               → Line 56
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""

# ================================================================================
# 📦 SECTION 1: LIBRARY IMPORT
# ================================================================================
# 📌 Importing the pandas library for data manipulation and analysis
# 🎯 Purpose: Pandas provides DataFrame structure for working with tabular data
import pandas as pd

# ================================================================================
# 📝 SECTION 2: DICTIONARY DATA CREATION
# ================================================================================
# 🗂️ Creating a Python dictionary to hold structured data
# 🔑 Keys: Column names ("Name", "Age", "City")
# 📊 Values: Lists containing data for each column
# ⚡ Note: All lists must have the same length (3 elements each)
data = {
    "Name": ["Ram", 'Shyam', 'Akash'],
    "Age": [19, 20, 30],
    "City": ["Nagpur", 'Mumbai', 'West_Bengal']
}

# ================================================================================
# 🏗️ SECTION 3: DATAFRAME CREATION FROM DICTIONARY
# ================================================================================
# 🔄 Method: pd.DataFrame()
# 📥 Input: Dictionary with column names as keys and data lists as values
# 📤 Output: A pandas DataFrame object stored in variable 'df'
# 🎯 Purpose: Converts dictionary into a structured 2D table format
df = pd.DataFrame(data)

# ================================================================================
# 🖨️ SECTION 4: DISPLAY DATAFRAME
# ================================================================================
# 📺 Function: print()
# 🎯 Purpose: Displays the DataFrame in the console
# 📋 Shows: All rows with index, column headers, and formatted data
print(df)

# ================================================================================
# 💾 SECTION 5: EXPORT TO CSV (COMMENTED OUT)
# ================================================================================
# 📄 Method: df.to_csv()
# 🔧 Parameter: index=False (excludes row index numbers from output file)
# 📁 Output: Creates "output.csv" file in the current directory
# ⚙️ Status: Currently disabled (commented out)
#df.to_csv("output.csv", index=False)

# ================================================================================
# 📊 SECTION 6: EXPORT TO EXCEL (COMMENTED OUT)
# ================================================================================
# 📄 Method: df.to_excel()
# 🔧 Parameter: index=False (excludes row index numbers from output file)
# 📁 Output: Creates "output.xlsx" file in the current directory
# ⚙️ Status: Currently disabled (commented out)
#df.to_excel("output.xlsx", index=False)

# ================================================================================
# 🔗 SECTION 7: EXPORT TO JSON (COMMENTED OUT)
# ================================================================================
# 📄 Method: df.to_json() [Note: Original code has typo 'f' instead of 'df']
# 🔧 Parameter: index=False (excludes row index numbers from output file)
# 📁 Output: Creates "output.json" file in the current directory
# ⚠️ Note: There's a typo in the original code - should be 'df' not 'f'
# ⚙️ Status: Currently disabled (commented out)
#f.to_json("output.json", index=False)


"""
================================================================================
📖 DETAILED EXPLANATION OF CONCEPTS
================================================================================

🔹 WHAT IS A DICTIONARY IN PYTHON?
   - A collection of key-value pairs enclosed in curly braces {}
   - Keys must be unique and immutable (strings, numbers, tuples)
   - Values can be any data type (lists, numbers, strings, etc.)
   - Example: {"Name": ["Ram", "Shyam"], "Age": [19, 20]}

🔹 CREATING A DATAFRAME FROM DICTIONARY:
   - Dictionary keys → DataFrame column names
   - Dictionary values (lists) → DataFrame column data
   - Each list must have the same length
   - Resulting DataFrame:
     
        Name  Age         City
     0   Ram   19       Nagpur
     1 Shyam   20       Mumbai
     2 Akash   30  West_Bengal

🔹 THE print() FUNCTION WITH DATAFRAMES:
   - Displays the entire DataFrame in tabular format
   - Shows index (0, 1, 2) on the left by default
   - Shows column names as headers
   - Automatically formats the output for readability

🔹 EXPORT METHODS LEARNED:

   1️⃣ to_csv() - Export to CSV
      ✅ Pros: Lightweight, universal compatibility, fast
      📊 Use Case: Data exchange, Excel import, database loading
      🔧 Common Parameters:
         - index=False → Don't save row index numbers
         - encoding='utf-8' → Handle special characters
         - sep=',' → Column separator (default is comma)
   
   2️⃣ to_excel() - Export to Excel
      ✅ Pros: Preserves formatting, multiple sheets, business-friendly
      📊 Use Case: Reports, presentations, business analytics
      🔧 Common Parameters:
         - index=False → Don't save row index numbers
         - sheet_name='Sheet1' → Name of the worksheet
         - engine='openpyxl' → Excel engine (auto-detected)
   
   3️⃣ to_json() - Export to JSON
      ✅ Pros: Web-friendly, nested structures, API integration
      📊 Use Case: Web applications, APIs, configuration files
      🔧 Common Parameters:
         - index=False → Don't include index
         - orient='records' → JSON structure format
         - indent=4 → Pretty-print with indentation

🔹 THE index=False PARAMETER:
   - By default, pandas includes row index (0, 1, 2, ...) in exports
   - index=False removes these index numbers from the output file
   - Without it: CSV would have an extra column with 0, 1, 2
   - With it: Only your actual data columns are saved

🔹 FILE NAMING CONVENTION:
   - "output.csv" → File created in current working directory
   - Can use full path: "D:/MyData/output.csv"
   - Extension determines file type (.csv, .xlsx, .json)

🔹 DATA STRUCTURE IN THIS EXAMPLE:
   - 3 columns: Name (string), Age (integer), City (string)
   - 3 rows: Each representing one person's information
   - Mixed data types: Strings and integers in same DataFrame

⚠️ IMPORTANT NOTE:
   - Line 56 has a typo: 'f.to_json()' should be 'df.to_json()'
   - This would cause a NameError if uncommented
   - The variable name is 'df', not 'f'

================================================================================
💡 KEY TAKEAWAYS
================================================================================
✓ DataFrames can be created from Python dictionaries easily
✓ Dictionary keys become column names automatically
✓ All data lists must have equal length for valid DataFrame
✓ Pandas supports export to CSV, Excel, and JSON formats
✓ index=False parameter prevents unwanted index column in exports
✓ print() displays DataFrame in clean, readable table format
================================================================================
"""