import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# Sorting algorithms
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to time sorting algorithms
def time_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr.copy())
    return time.time() - start_time

# Streamlit app
st.title("Sorting Algorithm Performance Comparison")
st.write("This app compares the performance of Merge Sort, Quick Sort, and Bubble Sort on different input sizes.")

# User input for array sizes
n_values = st.slider("Select the range for the number of elements (n):", 100, 5000, (100, 1000), step=100)
n_steps = st.slider("Step size for increasing n:", 100, 1000, 100)
n_list = list(range(n_values[0], n_values[1] + 1, n_steps))

# Arrays to store timings
merge_times = []
quick_times = []
bubble_times = []

st.write("### Running Comparisons...")
for n in n_list:
    arr = np.random.randint(0, 10000, n)

    # Time each sorting algorithm
    merge_times.append(time_algorithm(merge_sort, arr))
    quick_times.append(time_algorithm(quick_sort, arr))
    bubble_times.append(time_algorithm(bubble_sort, arr))

    st.write(f"Completed for n={n}")

# Plotting results
st.write("### Time Complexity Comparison")
plt.figure(figsize=(10, 6))
plt.plot(n_list, merge_times, label="Merge Sort", color="blue", marker="o")
plt.plot(n_list, quick_times, label="Quick Sort", color="green", marker="x")
plt.plot(n_list, bubble_times, label="Bubble Sort", color="red", marker="s")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
st.pyplot(plt)

st.write("""
    ### Analysis:
    - **Merge Sort**: Expected \(O(n \log n)\) complexity, performs well on large datasets.
    - **Quick Sort**: Also \(O(n \log n)\) on average, but can degrade to \(O(n^2)\) in the worst case.
    - **Bubble Sort**: Expected \(O(n^2)\) complexity, is inefficient on large datasets.
    """)
