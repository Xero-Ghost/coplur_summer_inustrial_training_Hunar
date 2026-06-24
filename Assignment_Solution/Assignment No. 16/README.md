# Employee Dataset Processing Using PySpark RDD

## Assignment Objective

Process employee salary data using PySpark RDD operations.

---

## Operations Performed

### 1. Sort Employees by Salary

Employees are sorted in descending order of salary.

### 2. Department-wise Salary Total

Total salary expenditure for each department is calculated.

### 3. Top 3 Highest Paid Employees

Top three highest-paid employees are identified and stored in an output file.

---

## Dataset

employees.csv

```csv
id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000
```

---

## Project Structure

```text
employee-rdd-assignment/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── data/
│   └── employees.csv
│
└── output/
```

---

## Build Docker Image

```bash
docker build -t employee-rdd-app .
```

---

## Run Docker Container

```bash
docker run --rm employee-rdd-app
```

---

## Expected Department Totals

```text
IT: 170000
HR: 85000
Finance: 130000
```

---

## Expected Top 3 Highest Paid Employees

```text
Priya   Finance   70000
Neha    IT        65000
Rohit   Finance   60000
```

---

## Technologies Used

- Python 3
- Apache Spark 3.5.1
- PySpark
- Docker
- Ubuntu 22.04