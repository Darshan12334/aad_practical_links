import streamlit as st
import numpy as np

def dijkstra(graph, start_node):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start_node] = 0

    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_dist = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        if min_index == -1:  # All reachable nodes are visited
            break

        visited[min_index] = True

        # Update the distances of adjacent nodes
        for j in range(n):
            if graph[min_index][j] != float('inf') and not visited[j]:
                new_dist = distance[min_index] + graph[min_index][j]
                if new_dist < distance[j]:
                    distance[j] = new_dist

    return distance

# Streamlit app
st.title("Shortest Path Finder")

# Input number of nodes
num_nodes = st.number_input("Enter total number of nodes:", min_value=2, max_value=20, value=5, step=1)
nodes = [chr(65 + i) for i in range(num_nodes)]  # Generate node names A, B, C, ...

# Input the start node
start_node = st.selectbox("Select the starting node:", nodes)
start_index = nodes.index(start_node)

# Input the graph data
st.write("Enter the weight matrix (use 'inf' for no direct path):")
weights = []
for i in range(num_nodes):
    row = st.text_input(f"Enter weights for row {nodes[i]} (space-separated):", 
                        " ".join(["inf" if j != i else "0" for j in range(num_nodes)]))
    weights.append([float(x) if x != "inf" else float('inf') for x in row.split()])

graph = np.array(weights)

# Run Dijkstra's algorithm
if st.button("Calculate Shortest Paths"):
    distances = dijkstra(graph, start_index)

    # Display results
    st.write("### Shortest Path Costs:")
    results = {nodes[i]: distances[i] if distances[i] != float('inf') else "inf" for i in range(num_nodes)}
    for dest, cost in results.items():
        st.write(f"{start_node} to {dest}: {cost}")
