import streamlit as st
import numpy as np
import time
import sys
import pandas as pd
sys.setrecursionlimit(20000)

st.title("Calculation Comparison")
num = st.number_input("Enter a number", min_value=1)

def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += n
    return total

def sum_formula(n):
    total = n * (n + 1) / 2
    return total

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)

# Initialize lists to store execution times
time1_list = []
time2_list = []
time3_list = []
x_values = []

for i in range(1, num + 1):
    # Store current input size
    x_values.append(i)
    
    # Measure time for sum_loop
    start = time.time()
    sum_loop(i)
    end = time.time()
    time1_list.append((end - start) * 1000)  # Convert to milliseconds
    
    # Measure time for sum_formula
    start = time.time()
    sum_formula(i)
    end = time.time()
    time2_list.append((end - start) * 1000)
    
    # Measure time for recur_sum
    start = time.time()
    recur_sum(i)
    end = time.time()
    time3_list.append((end - start) * 1000)

# Combine data into a pandas DataFrame for easier plotting
df = pd.DataFrame({
    'Input Size': x_values,
    'Sum Loop Time (ms)': time1_list,
    'Sum Formula Time (ms)': time2_list,
    'Recursive Sum Time (ms)': time3_list
})

# Set Input Size as the index
df.set_index('Input Size', inplace=True)

# Plot the data using a line chart
st.line_chart(df)
