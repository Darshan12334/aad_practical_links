import pandas as pd
import time
import matplotlib.pyplot as plt
import streamlit as st

employees = [
    {"id": 1, "name": "mrigaksh", "salary": 70000, "age": 30, "mobile": "1234567890"},
    {"id": 2, "name": "jyot", "salary": 50000, "age": 25, "mobile": "0987654321"},
    {"id": 3, "name": "krish", "salary": 80000, "age": 35, "mobile": "1122334455"},
    {"id": 4, "name": "aisha", "salary": 55000, "age": 28, "mobile": "2223334444"},
    {"id": 5, "name": "vikram", "salary": 90000, "age": 40, "mobile": "3334445555"},
    {"id": 6, "name": "meera", "salary": 67000, "age": 27, "mobile": "4445556666"},
    {"id": 7, "name": "manish", "salary": 72000, "age": 32, "mobile": "5556667777"},
    {"id": 8, "name": "tanya", "salary": 63000, "age": 26, "mobile": "6667778888"},
    {"id": 9, "name": "ravi", "salary": 58000, "age": 29, "mobile": "7778889999"},
    {"id": 10, "name": "kiran", "salary": 81000, "age": 33, "mobile": "8889990000"},
    {"id": 11, "name": "akash", "salary": 52000, "age": 24, "mobile": "1112223333"},
    {"id": 12, "name": "maya", "salary": 76000, "age": 31, "mobile": "9990001111"},
    {"id": 13, "name": "raj", "salary": 82000, "age": 34, "mobile": "0001112222"},
    {"id": 14, "name": "simran", "salary": 68000, "age": 28, "mobile": "3334445555"},
    {"id": 15, "name": "amit", "salary": 49000, "age": 26, "mobile": "4445556666"},
    {"id": 16, "name": "anita", "salary": 83000, "age": 36, "mobile": "5556667777"},
    {"id": 17, "name": "rohit", "salary": 57000, "age": 27, "mobile": "6667778888"},
    {"id": 18, "name": "neha", "salary": 92000, "age": 39, "mobile": "7778889999"},
    {"id": 19, "name": "sunil", "salary": 69000, "age": 30, "mobile": "8889990000"},
    {"id": 20, "name": "richa", "salary": 64000, "age": 25, "mobile": "9990001111"},
    {"id": 21, "name": "deepak", "salary": 73000, "age": 32, "mobile": "1112223333"},
    {"id": 22, "name": "kavita", "salary": 50000, "age": 24, "mobile": "2223334444"},
    {"id": 23, "name": "vishal", "salary": 84000, "age": 35, "mobile": "3334445555"},
    {"id": 24, "name": "pooja", "salary": 62000, "age": 29, "mobile": "4445556666"},
    {"id": 25, "name": "sandeep", "salary": 85000, "age": 38, "mobile": "5556667777"},
    {"id": 26, "name": "jyoti", "salary": 71000, "age": 26, "mobile": "6667778888"},
    {"id": 27, "name": "ajay", "salary": 61000, "age": 28, "mobile": "7778889999"},
    {"id": 28, "name": "priya", "salary": 89000, "age": 37, "mobile": "8889990000"},
    {"id": 29, "name": "sameer", "salary": 78000, "age": 34, "mobile": "9990001111"},
    {"id": 30, "name": "suman", "salary": 67000, "age": 31, "mobile": "1112223333"},
    {"id": 31, "name": "rahul", "salary": 54000, "age": 27, "mobile": "2223334444"},
    {"id": 32, "name": "kajal", "salary": 88000, "age": 39, "mobile": "3334445555"},
    {"id": 33, "name": "harish", "salary": 65000, "age": 29, "mobile": "4445556666"},
    {"id": 34, "name": "aarti", "salary": 74000, "age": 32, "mobile": "5556667777"},
    {"id": 35, "name": "manoj", "salary": 60000, "age": 28, "mobile": "6667778888"},
    {"id": 36, "name": "megha", "salary": 90000, "age": 36, "mobile": "7778889999"},
    {"id": 37, "name": "atul", "salary": 71000, "age": 30, "mobile": "8889990000"},
    {"id": 38, "name": "kanika", "salary": 83000, "age": 33, "mobile": "9990001111"},
    {"id": 39, "name": "deepa", "salary": 56000, "age": 26, "mobile": "1112223333"},
    {"id": 40, "name": "gaurav", "salary": 87000, "age": 35, "mobile": "2223334444"},
    {"id": 41, "name": "payal", "salary": 75000, "age": 28, "mobile": "3334445555"},
    {"id": 42, "name": "yash", "salary": 52000, "age": 25, "mobile": "4445556666"},
    {"id": 43, "name": "swati", "salary": 94000, "age": 40, "mobile": "5556667777"},
    {"id": 44, "name": "avinash", "salary": 66000, "age": 27, "mobile": "6667778888"},
    {"id": 45, "name": "pranav", "salary": 68000, "age": 31, "mobile": "7778889999"},
    {"id": 46, "name": "ritika", "salary": 85000, "age": 34, "mobile": "8889990000"},
    {"id": 47, "name": "karan", "salary": 74000, "age": 29, "mobile": "9990001111"},
    {"id": 48, "name": "reshma", "salary": 59000, "age": 26, "mobile": "1112223333"},
    {"id": 49, "name": "varun", "salary": 87000, "age": 32, "mobile": "2223334444"},
    {"id": 50, "name": "geeta", "salary": 93000, "age": 38, "mobile": "3334445555"}
]


# Linear Search with 1-second delay per check
def linear_search(employees, key, value):
    time.sleep(1)  # Add 1-second delay for each comparison
    for emp in employees:
       
        if emp[key] == value:
            return emp
    return None

# Recursive Binary Search with 1-second delay per comparison
def binary_search(employees, key, value, low, high):
    
    time.sleep(1)  # Add 1-second delay for each comparison
    if low > high:
        return None
    mid = (low + high) // 2
    if employees[mid][key] == value:
        return employees[mid]
    elif employees[mid][key] < value:
        return binary_search(employees, key, value, mid + 1, high)
    else:
        return binary_search(employees, key, value, low, mid - 1)

# Streamlit UI
st.title("Employee Search Application")

# Search for highest salary package
if st.button("Find Highest Salary Package"):
    start_time = time.time()
    employees_sorted = sorted(employees, key=lambda x: x['salary'])
    highest_salary_emp = binary_search(employees_sorted, 'salary', max(emp['salary'] for emp in employees), 0, len(employees_sorted) - 1)
    binary_time = time.time() - start_time
    st.write(f"Highest Salary: {highest_salary_emp['salary']} by {highest_salary_emp['name']} (Binary Search took {binary_time:.4f} seconds)")

# Search for lowest salary using Binary Search
if st.button("Find Lowest Salary"):
    start_time = time.time()
    employees_sorted = sorted(employees, key=lambda x: x['salary'])
    lowest_salary_emp = binary_search(employees_sorted, 'salary', min(emp['salary'] for emp in employees), 0, len(employees_sorted) - 1)
    binary_time = time.time() - start_time
    st.write(f"Lowest Salary: {lowest_salary_emp['salary']} by {lowest_salary_emp['name']} (Binary Search took {binary_time:.4f} seconds)")

# Search for youngest employee
if st.button("Find Youngest Employee"):
    start_time = time.time()
    youngest_emp = min(employees, key=lambda x: x['age'])
    linear_time = time.time() - start_time
    st.write(f"Youngest Employee: {youngest_emp['name']} (Mobile: {youngest_emp['mobile']}) (Linear Search took {linear_time:.4f} seconds)")

# Search for oldest employee's salary
if st.button("Find Oldest Employee Salary"):
    start_time = time.time()
    oldest_emp = max(employees, key=lambda x: x['age'])
    linear_time = time.time() - start_time
    st.write(f"Oldest Employee Salary: {oldest_emp['salary']} (Linear Search took {linear_time:.4f} seconds)")

# Plotting time taken vs n
n_values = []
linear_times = []
binary_times = []

for n in range(1, len(employees) + 1):
    n_values.append(n)
    
    # Measure Linear Search time
    start_time = time.time()
    linear_search(employees[:n], 'id', 1)
    linear_times.append(time.time() - start_time)
    
    # Measure Binary Search time
    employees_sorted = sorted(employees[:n], key=lambda x: x['id'])
    start_time = time.time()
    binary_search(employees_sorted, 'id', 1, 0, n - 1)
    binary_times.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(n_values, linear_times, label="Linear Search Time", marker='o')
plt.plot(n_values, binary_times, label="Binary Search Time", marker='o')
plt.xlabel('Number of Employees (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Taken vs Number of Employees')
plt.legend()
st.pyplot(plt)
