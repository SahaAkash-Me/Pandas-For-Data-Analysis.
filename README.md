# 🐼 Pandas For Data Analysis

A structured, beginner-friendly Python learning repository covering core Pandas concepts — from loading data to filtering and exploring DataFrames. Each script is heavily commented with explanations, making it ideal as both a learning reference and a revision toolkit.

> 📌 **Author:** Akash Saha | [GitHub](https://github.com/SahaAkash-Me/Pandas-For-Data-Analysis)

---

## 📁 Repository Structure

```
Pandas-For-Data-Analysis/
│
├── Datasets/
│   ├── SampleSuperstore.xlsx       # Retail superstore sales dataset
│   ├── sales_data_sample.csv       # Sales records with Latin-1 encoding
│   └── sample_Data.json            # JSON format sample dataset
│
├── Scripts/
│   ├── 1. app.py                   # Loading data (CSV / Excel / JSON)
│   ├── 2. save.py                  # Creating DataFrames & exporting outputs
│   ├── 3. rows.py                  # head() and tail() — inspecting rows
│   ├── 4. Info.py                  # df.info() — structure & data types
│   ├── 5. Describe.py              # df.describe() — descriptive statistics
│   ├── 6. Shape & Columns.py       # df.shape & df.columns — dimensions
│   ├── 7. Selecting Columns.py     # Single & multiple column selection
│   └── 8. Filtering Rows.py        # Boolean masking with AND / OR conditions
│
├── Outputs/
│   ├── output.csv                  # Sample exported CSV
│   ├── output.xlsx                 # Sample exported Excel file
│   └── output.json                 # Sample exported JSON file
│
└── README.md
```

---

## 📚 Scripts Overview

### 1. `app.py` — Data Loading
Demonstrates how to load data into a pandas DataFrame from three file formats:
- `pd.read_csv()` — for CSV files (with `encoding='latin1'`)
- `pd.read_excel()` — for Excel `.xlsx` files
- `pd.read_json()` — for JSON files

---

### 2. `save.py` — DataFrame Creation & Export
Shows how to create a DataFrame from a Python dictionary and export it to multiple formats:
- `pd.DataFrame(dict)` — build a DataFrame from scratch
- `df.to_csv()` — save as CSV
- `df.to_excel()` — save as Excel
- `df.to_json()` — save as JSON
- `index=False` parameter — exclude row indices from exports

---

### 3. `rows.py` — Row Inspection with head() & tail()
Covers quick row-level previewing of datasets:
- `df.head(n)` — view first N rows (default: 5)
- `df.tail(n)` — view last N rows (default: 5)
- Useful for EDA (Exploratory Data Analysis) on large datasets

---

### 4. `Info.py` — DataFrame Structure
Explains the `df.info()` method for understanding dataset composition:
- Column names and data types (`int64`, `float64`, `object`)
- Non-null value counts (spot missing data early)
- Memory usage

---

### 5. `Describe.py` — Descriptive Statistics
Uses `df.describe()` to generate a statistical summary of numeric columns:

| Metric | Meaning |
|--------|---------|
| `count` | Non-null value count |
| `mean` | Arithmetic average |
| `std` | Standard deviation (spread of data) |
| `min` / `max` | Smallest / largest value |
| `25%` / `50%` / `75%` | Quartile distribution |

---

### 6. `Shape & Columns.py` — Dimensions & Column Names
Covers two essential DataFrame properties:
- `df.shape` → returns `(rows, columns)` as a tuple
- `df.columns` → returns an Index of all column names

---

### 7. `Selecting Columns.py` — Column Selection
Three methods for accessing columns:
- `df['Name']` → returns a **Series** (single column)
- `name_col = df['Name']` → stores column in a variable
- `df[['Name', 'Salary']]` → returns a **DataFrame** (multiple columns)

> ⚠️ Common mistake: `df['Name', 'Salary']` ❌ — always use double brackets `[[]]` for multiple columns.

---

### 8. `Filtering Rows.py` — Boolean Masking
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

> ⚠️ Always wrap each condition in `()`. Use `&` instead of `and`, and `|` instead of `or` inside pandas filters.

---

## 🗂️ Datasets Used

| File | Format | Description |
|------|--------|-------------|
| `SampleSuperstore.xlsx` | Excel | Retail store sales & profit data |
| `sales_data_sample.csv` | CSV | Multi-region sales records (Latin-1 encoded) |
| `sample_Data.json` | JSON | JSON-structured sample dataset |

---

## ⚙️ Requirements

```bash
pip install pandas openpyxl
```

| Library | Purpose |
|---------|---------|
| `pandas` | Core data manipulation |
| `openpyxl` | Reading/writing `.xlsx` files |

> Python 3.7+ recommended.

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/SahaAkash-Me/Pandas-For-Data-Analysis.git

# 2. Navigate into the project
cd Pandas-For-Data-Analysis

# 3. Install dependencies
pip install pandas openpyxl

# 4. Update file paths in scripts to match your local setup, then run
python "Scripts/1. app.py"
```

> **Note:** Scripts currently use absolute Windows paths (e.g. `D:/Python/Pandas/Datasets/`). Update the paths to match your local directory before running.

---

## 🧠 Concepts Covered

- [x] Loading data from CSV, Excel, and JSON
- [x] Creating DataFrames from Python dictionaries
- [x] Exporting DataFrames to CSV, Excel, and JSON
- [x] Inspecting rows with `head()` and `tail()`
- [x] Understanding structure with `df.info()`
- [x] Generating statistics with `df.describe()`
- [x] Checking dimensions with `df.shape` and `df.columns`
- [x] Selecting single and multiple columns
- [x] Filtering rows with boolean masking (`&`, `|`)

---

## 📌 Notes

- All scripts include a detailed **indexed table of contents** and inline comments explaining every step — designed for learners who want to understand the *why*, not just the *how*.
- The `Outputs/` folder contains pre-generated sample export files for reference.

---

*Part of an ongoing Python & Data Analysis learning journey. More topics coming soon.*
