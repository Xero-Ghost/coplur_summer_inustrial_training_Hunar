from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("EmployeeRDDAssignment").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.csv")

header = rdd.first()

employee_rdd = (
    rdd.filter(lambda row: row != header)
       .map(lambda row: row.split(","))
       .map(lambda x: (
           int(x[0]),      # ID
           x[1],           # Name
           x[2],           # Department
           int(x[3])       # Salary
       ))
)

print("\n" + "="*50)
print("EMPLOYEES SORTED BY SALARY (DESCENDING)")
print("="*50)

sorted_employees = employee_rdd.sortBy(
    lambda x: x[3],
    ascending=False
)

for emp in sorted_employees.collect():
    print(emp)

print("\n" + "="*50)
print("DEPARTMENT WISE TOTAL SALARY")
print("="*50)

department_salary = (
    employee_rdd
    .map(lambda x: (x[2], x[3]))
    .reduceByKey(lambda a, b: a + b)
)

for dept, total in department_salary.collect():
    print(f"{dept}: {total}")

top_3 = sorted_employees.take(3)
os.makedirs("output", exist_ok=True)

with open("output/top_three_highest_paid.txt", "w") as file:
    file.write("Top 3 Highest Paid Employees\n")
    file.write("=" * 40 + "\n")

    for emp in top_3:
        file.write(
            f"ID: {emp[0]}, "
            f"Name: {emp[1]}, "
            f"Department: {emp[2]}, "
            f"Salary: {emp[3]}\n"
        )

print("\nTop 3 highest paid employees saved to:")
print("output/top_three_highest_paid.txt")

spark.stop()