# PySpark Sales Data Analysis Assignment

## Objective

Perform data analysis on a sales dataset using PySpark DataFrames.

---

## Dataset

Location:

```text
data/sales.csv
```

Columns:

- product_id
- product_name
- category
- sales

---

## Operations Performed

### 1. Sort Products by Sales

Sort all products in descending order based on sales.

### 2. Top 3 Products

Display the top 3 products with the highest sales values.

### 3. Filter Products

Filter products having sales greater than 80,000.

### 4. Save Output

Save the filtered results as CSV files in:

```text
output/high_sales_products
```

---

## Running Locally

Install PySpark:

```bash
pip install pyspark
```

Run:

```bash
python app.py
```

---

## Docker Build

Build image:

```bash
docker build -t pyspark-sales .
```

Run container:

```bash
docker run pyspark-sales
```

---

## Expected High Sales Products

| Product | Sales |
|----------|--------|
| Laptop | 150000 |
| Mobile | 95000 |
| TV | 120000 |
| Bed | 90000 |

---

## Author

Assignment Submission