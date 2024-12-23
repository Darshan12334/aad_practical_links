import streamlit as st
import numpy as np
from itertools import permutations

distance_matrix = np.array([
    [float('inf'), 20, 30, 10, 11],
    [15, float('inf'), 16, 4, 2],
    [3, 5, float('inf'), 2, 4],
    [19, 6, 18, float('inf'), 3],
    [16, 4, 7, 16, float('inf')]
])

def tsp_brute_force(matrix):
    n = len(matrix)
    min_cost = float('inf')
    best_path = []
    cities = range(n)
    
    for perm in permutations(cities[1:]):
        current_path = [0] + list(perm) + [0]
        current_cost = sum(matrix[current_path[i]][current_path[i+1]] for i in range(n))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    
    return min_cost, best_path

st.title("Traveling Salesman Problem (TSP) Solver")
st.write("This app solves the TSP using a brute-force approach for the given distance matrix.")

st.write("### Distance Matrix")
st.write(distance_matrix)

min_cost, path = tsp_brute_force(distance_matrix)

st.write("### Solution")
st.write("Minimum Path Taken:")
for i in range(len(path) - 1):
    st.write(f"{path[i] + 1} – {path[i + 1] + 1} = {distance_matrix[path[i]][path[i + 1]]}")

st.write(f"**Minimum cost:** {min_cost}")
st.write(f"**Path Taken:** {' - '.join(str(city + 1) for city in path)}")
