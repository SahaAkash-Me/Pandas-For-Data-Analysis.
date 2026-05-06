# 🐼 Pandas For Data Analysis

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> A structured, beginner-friendly Python learning repository covering core Pandas concepts — from loading data to filtering and exploring DataFrames. Built by a Data Analyst with a background in AML fraud detection and KYC compliance.

---

## 📚 About This Repository

This repository is a **living documentation** of my systematic Python upskilling journey. Each script is heavily commented with indexed explanations, making it ideal as both a **learning reference** and a **revision toolkit**.

As someone working in AML fraud detection and KYC compliance, I've learned that effective data manipulation isn't just about knowing the syntax — it's about building systematic thinking and creating reproducible workflows.

**Philosophy:** Understand the *why*, not just the *how*.

---

## 📁 Repository Structure

```
Pandas-For-Data-Analysis/
│
├── Datasets/
│   ├── SampleSuperstore.xlsx       # Retail superstore sales dataset
│   ├── sales_data_sample.csv       # Sales records with Latin-1 encoding
│   ├── sample_Data.json            # JSON format sample dataset
│   └── placeholder                 # Placeholder file
│
├── Scripts/
│   ├── 1. app.py                              # Loading data (CSV / Excel / JSON)
│   ├── 2. save.py                             # Creating DataFrames & exporting outputs
│   ├── 3. rows.py                             # head() and tail() — inspecting rows
│   ├── 4. Info.py                             # df.info() — structure & data types
│   ├── 5. Describe.py                         # df.describe() — descriptive statistics
│   ├── 6. Shape & Columns.py                  # df.shape & df.columns — dimensions
│   ├── 7. Selecting Columns.py                # Single & multiple column selection
│   ├── 8. Filtering Rows.py                   # Boolean masking with AND / OR conditions
│   ├── 9. Modifying Data.py                   # Updating values in DataFrames
│   ├── 10.1. Missing Data (Handling Missing Data).py    # Detecting missing values
│   ├── 10.2. Handling Missing Data (Handling Missing Data).py  # Dropping NaN values
│   ├── 10.3. Filling Missing Data (Handling Missing Data).py   # Filling missing data
│   ├── 11. Selecting and Filtering Data.py    # Advanced selection techniques
│   ├── 11.1. Summary (Selecting and Filtering Data).py  # Selection summary
│   ├── 11.2. Grp_by.py                        # GroupBy operations
│   ├── 12. Merging and Joining.py             # Combining DataFrames
│   ├── 12.1. Concatenation.py                 # Concatenating DataFrames
│   └── placeholder                            # Placeholder file
│
├── Outputs/
│   ├── output.csv                  # Sample exported CSV
│   ├── output.json                 # Sample exported JSON
│   ├── output.xlsx                 # Sample exported Excel file
│   └── Placeholder                 # Placeholder file
│
└── README.md
```

---

## 📋 Quick Reference Guide

| Script # | Topic | Key Concepts |
|----------|-------|--------------|
| 1 | Data Loading | `read_csv()`, `read_excel()`, `read_json()` |
| 2 | DataFrame Creation & Export | `DataFrame()`, `to_csv()`, `to_excel()`, `to_json()` |
| 3 | Row Inspection | `head()`, `tail()` |
| 4 | Structure Analysis | `info()`, data types, null counts |
| 5 | Statistical Summary | `describe()`, mean, std, quartiles |
| 6 | Dimensions | `shape`, `columns` |
| 7 | Column Selection | Single `[]`, multiple `[[]]` |
| 8 | Row Filtering | Boolean masking, `&`, `\|` operators |
| 9 | Data Modification | Updating values, adding/removing columns |
| 10.1 | Missing Data Detection | `isnull()`, `isna()`, null patterns |
| 10.2 | Missing Data Removal | `dropna()`, axis, how, thresh |
| 10.3 | Missing Data Filling | `fillna()`, `ffill`, `bfill` |
| 11 | Advanced Selection | `.loc[]`, `.iloc[]` |
| 11.1 | Selection Summary | Best practices, comparison |
| 11.2 | GroupBy Operations | `groupby()`, aggregations |
| 12 | Merging & Joining | `merge()`, join types |
| 12.1 | Concatenation | `concat()`, axis parameter |

---

## 📚 Scripts Overview

### **1. `app.py` — Data Loading**
Demonstrates how to load data into a pandas DataFrame from three file formats:
- `pd.read_csv()` — for CSV files (with `encoding='latin1'`)
- `pd.read_excel()` — for Excel `.xlsx` files
- `pd.read_json()` — for JSON files

**Key Learning:** Different file formats require different pandas readers with specific parameters.

---

### **2. `save.py` — DataFrame Creation & Export**
Shows how to create a DataFrame from a Python dictionary and export it to multiple formats:
- `pd.DataFrame(dict)` — build a DataFrame from scratch
- `df.to_csv()` — save as CSV
- `df.to_excel()` — save as Excel
- `df.to_json()` — save as JSON
- `index=False` parameter — exclude row indices from exports

**Key Learning:** DataFrames can be created programmatically and exported to any format for sharing.

---

### **3. `rows.py` — Row Inspection with head() & tail()**
Covers quick row-level previewing of datasets:
- `df.head(n)` — view first N rows (default: 5)
- `df.tail(n)` — view last N rows (default: 5)
- Useful for EDA (Exploratory Data Analysis) on large datasets

**Key Learning:** Always inspect your data before processing — head/tail are your first debugging tools.

---

### **4. `Info.py` — DataFrame Structure**
Explains the `df.info()` method for understanding dataset composition:
- Column names and data types (`int64`, `float64`, `object`)
- Non-null value counts (spot missing data early)
- Memory usage

**Key Learning:** `info()` reveals data quality issues before they become problems in analysis.

---

### **5. `Describe.py` — Descriptive Statistics**
Uses `df.describe()` to generate a statistical summary of numeric columns:

| Metric | Meaning |
|--------|---------|
| `count` | Non-null value count |
| `mean` | Arithmetic average |
| `std` | Standard deviation (spread of data) |
| `min` / `max` | Smallest / largest value |
| `25%` / `50%` / `75%` | Quartile distribution |

**Key Learning:** Statistical summaries help identify outliers and data distribution patterns.

---

### **6. `Shape & Columns.py` — Dimensions & Column Names**
Covers two essential DataFrame properties:
- `df.shape` → returns `(rows, columns)` as a tuple
- `df.columns` → returns an Index of all column names

**Key Learning:** Know your data dimensions before processing — prevents index errors.

---

### **7. `Selecting Columns.py` — Column Selection**
Three methods for accessing columns:
- `df['Name']` → returns a **Series** (single column)
- `name_col = df['Name']` → stores column in a variable
- `df[['Name', 'Salary']]` → returns a **DataFrame** (multiple columns)

> ⚠️ **Common mistake:** `df['Name', 'Salary']` ❌ — always use double brackets `[[]]` for multiple columns.

**Key Learning:** Series vs DataFrame — single brackets return Series, double brackets return DataFrame.

---

### **8. `Filtering Rows.py` — Boolean Masking**
Demonstrates filtering rows using conditions:

```python
# Single condition
df[df['Salary'] > 50000]

# Range filter (AND on same column)
df[(df['Salary'] > 50000) & (df['Salary'] < 80000)]

# Multiple conditions — AND
df[(df['Age'] > 30) & (df['Salary'] > 50000)]

# Multiple conditions — OR
df[(df['Age'] > 35) | (df['Performance_Score'] > 90)]
```

> ⚠️ **Critical:** Always wrap each condition in `()`. Use `&` instead of `and`, and `|` instead of `or` inside pandas filters.

**Key Learning:** Boolean masking is the foundation of data filtering — master this for complex queries.

---

### **9. `Modifying Data.py` — Data Modification**
Demonstrates how to update and modify values in DataFrames:
- Updating single values
- Updating entire columns
- Adding new columns
- Renaming columns
- Deleting columns

**Key Learning:** DataFrames are mutable — you can change values after creation.

---

### **10.1-10.3 Missing Data Series — Handling Missing Data**

#### **10.1. `Missing Data (Handling Missing Data).py`**
Detecting and identifying missing values:
- Using `isnull()` and `isna()`
- Counting missing values per column
- Visualizing missing data patterns

**Key Learning:** Always check for missing data before analysis — it affects calculations.

---

#### **10.2. `Handling Missing Data (Handling Missing Data).py`**
Removing missing values:
- `dropna()` — remove rows/columns with NaN
- `axis` parameter — drop rows vs columns
- `how` parameter — 'any' vs 'all'
- `thresh` parameter — minimum non-null values

**Key Learning:** Dropping data loses information — only do it when appropriate.

---

#### **10.3. `Filling Missing Data (Handling Missing Data).py`**
Filling missing values:
- `fillna()` — replace NaN with specific values
- Forward fill (`ffill`) — propagate last valid value
- Backward fill (`bfill`) — use next valid value
- Fill with mean/median/mode

**Key Learning:** Filling preserves data size but introduces assumptions about missing values.

---

### **11. `Selecting and Filtering Data.py` — Advanced Selection**
Advanced selection techniques:
- Using `.loc[]` for label-based indexing
- Using `.iloc[]` for position-based indexing
- Conditional selection with multiple criteria
- Selecting specific rows and columns simultaneously

**Key Learning:** `.loc` uses labels, `.iloc` uses integer positions — know the difference.

---

### **11.1. `Summary (Selecting and Filtering Data).py`**
Comprehensive summary of selection methods:
- Comparison of different selection approaches
- Best practices for data selection
- Common pitfalls and how to avoid them

**Key Learning:** Multiple ways to select data — choose the most readable and maintainable.

---

### **11.2. `Grp_by.py` — GroupBy Operations**
Grouping and aggregating data:
- `groupby()` — split-apply-combine pattern
- Aggregation functions: `sum()`, `mean()`, `count()`, `max()`, `min()`
- Multiple aggregations simultaneously
- Grouping by multiple columns

**Key Learning:** GroupBy is one of the most powerful Pandas features for summarizing data by categories.

---

### **12. `Merging and Joining.py` — Combining DataFrames**
Combining multiple DataFrames:
- `merge()` — SQL-style joins
- Inner, outer, left, and right joins
- Joining on specific columns
- Handling duplicate column names

**Key Learning:** Merging is like SQL JOINs — understand join types to avoid data loss or duplication.

---

### **12.1. `Concatenation.py` — Concatenating DataFrames**
Stacking DataFrames vertically or horizontally:
- `concat()` — combine DataFrames along an axis
- `axis=0` — stack vertically (rows)
- `axis=1` — stack horizontally (columns)
- `ignore_index` parameter — reset index after concatenation

**Key Learning:** Concatenation vs Merging — concat stacks, merge relates data through keys.

---

## 🗂️ Datasets Used

| File | Format | Description |
|------|--------|-------------|
| `SampleSuperstore.xlsx` | Excel | Retail store sales & profit data |
| `sales_data_sample.csv` | CSV | Multi-region sales records (Latin-1 encoded) |
| `sample_Data.json` | JSON | JSON-structured sample dataset |

All datasets are real-world formats with various encoding and structure challenges — perfect for practical learning.

---

## ⚙️ Requirements

```bash
pip install pandas openpyxl
```

| Library | Purpose |
|---------|---------|
| `pandas` | Core data manipulation |
| `openpyxl` | Reading/writing `.xlsx` files |

> **Python Version:** 3.7+ recommended

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/SahaAkash-Me/Pandas-For-Data-Analysis.git

# 2. Navigate into the project
cd Pandas-For-Data-Analysis

# 3. Install dependencies
pip install pandas openpyxl

# 4. Update file paths in scripts to match your local setup
# Then run any script:
python "Scripts/1. app.py"
```

> ⚠️ **Important:** Scripts currently use absolute Windows paths (e.g., `D:/Python/Pandas/Datasets/`). Update these paths to match your local directory structure before running.

---

## 🧠 Concepts Covered

### ✅ **Foundation (Scripts 1-8)**
- [x] Loading data from CSV, Excel, and JSON
- [x] Creating DataFrames from Python dictionaries
- [x] Exporting DataFrames to CSV, Excel, and JSON
- [x] Inspecting rows with `head()` and `tail()`
- [x] Understanding structure with `df.info()`
- [x] Generating statistics with `df.describe()`
- [x] Checking dimensions with `df.shape` and `df.columns`
- [x] Selecting single and multiple columns
- [x] Filtering rows with boolean masking (`&`, `|`)

### ✅ **Data Manipulation (Scripts 9-10)**
- [x] Modifying DataFrame values and columns
- [x] Detecting missing data with `isnull()` and `isna()`
- [x] Removing missing data with `dropna()`
- [x] Filling missing data with `fillna()`, `ffill`, `bfill`

### ✅ **Advanced Selection & Grouping (Scripts 11-12)**
- [x] Label-based indexing with `.loc[]`
- [x] Position-based indexing with `.iloc[]`
- [x] GroupBy operations and aggregations
- [x] Merging DataFrames (inner, outer, left, right joins)
- [x] Concatenating DataFrames vertically and horizontally

---

## 🎯 Coming Next

The foundation and intermediate phases are **complete**! Next topics on the roadmap:

- [ ] **Time Series Analysis** — Working with dates, timestamps, and temporal data
- [ ] **Data Visualization** — Creating plots with Matplotlib/Seaborn
- [ ] **Advanced Transformations** — `apply()`, `map()`, `applymap()` functions
- [ ] **Pivot Tables** — Reshaping data with `pivot()` and `pivot_table()`
- [ ] **String Operations** — Text manipulation with `.str` accessor
- [ ] **Window Functions** — Rolling averages and expanding calculations
- [ ] **Performance Optimization** — Efficient data processing techniques

---

## 💡 Why This Repository?

### For Me:
- **Accountability** — Building in public keeps me consistent
- **Reference** — Quick lookup for common patterns and techniques  
- **Portfolio** — Demonstrating hands-on commitment to continuous learning

### For Others:
- **Learning Resource** — Follow along if you're learning Pandas
- **Code Reference** — Every script is indexed and commented for clarity
- **Real Datasets** — Practice with actual data formats and encoding challenges

---

## 📝 Documentation Style

All scripts include a detailed **indexed table of contents** and inline comments explaining every step:

```python
# [001] Import pandas library
import pandas as pd

# [002] Load CSV with Latin-1 encoding
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# [003] Display first 5 rows to verify load
print(df.head())
```

This structure makes it easy to:
- Jump to specific concepts
- Understand the reasoning behind each step
- Use as a quick reference during real projects

---

## 🎓 My Background

I'm a Data Analyst with hands-on experience in:
- **AML (Anti-Money Laundering)** fraud detection
- **KYC (Know Your Customer)** compliance  
- Risk assessment and data-driven decision making

This repository reflects my approach to systematic skill development in data analysis.

---

## 🤝 Contributions & Feedback

While this is primarily a personal learning repository, I welcome:

- **⭐ Stars** — If you find this helpful
- **🐛 Issues** — If you spot errors or have suggestions
- **💬 Discussions** — Share what topics you'd like to see covered next
- **🔀 Forks** — Feel free to adapt this for your own learning journey

---

## 📌 Notes

- All scripts include detailed **indexed comments** explaining every step — designed for learners who want to understand the *why*, not just the *how*.
- The `Outputs/` folder contains **pre-generated sample export files** for reference.
- File paths in scripts are currently Windows-based — update them to match your OS.

---

## 📬 Connect With Me

- **GitHub**: [@SahaAkash-Me](https://github.com/SahaAkash-Me)
- **LinkedIn**: [Akash Saha](https://www.linkedin.com/in/akash-saha)
- **Repository**: [Pandas For Data Analysis](https://github.com/SahaAkash-Me/Pandas-For-Data-Analysis)

---

## 🙏 Acknowledgments

- **Wes McKinney** — Creator of Pandas
- The **Pandas Development Team** — For this incredible library
- The **Data Science Community** — For continuous learning resources and inspiration

---

## 📊 Repository Stats

- **Scripts**: 17 (Foundation through Advanced topics)
- **Datasets**: 3 real-world formats (CSV, Excel, JSON)
- **Topics Covered**: Data loading → Manipulation → Missing data → GroupBy → Merging
- **Status**: ✅ Foundation & Intermediate complete | 🚀 Advanced topics in progress

---

**⚡ Learning in Public | Building Systematically | One Script at a Time**

*Last Updated: May 2026*
