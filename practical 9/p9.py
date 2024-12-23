import streamlit as st

# Fractional Knapsack function
def fractional_knapsack(W, weights, profits):
    ratio = [p / w for p, w in zip(profits, weights)]
    items = list(range(len(profits)))
    items.sort(key=lambda i: ratio[i], reverse=True)
    
    total_profit = 0.0
    weight_taken = [0] * len(weights)
    
    for i in items:
        if weights[i] <= W:
            weight_taken[i] = 1
            total_profit += profits[i]
            W -= weights[i]
        else:
            weight_taken[i] = W / weights[i]
            total_profit += profits[i] * weight_taken[i]
            break
    
    return total_profit, weight_taken, ratio

# Streamlit UI
st.title("Fractional Knapsack Problem")

# Input data
profits = [280, 100, 120, 120]
weights = [40, 10, 20, 24]
W = 60

# Display input data
st.write("Given the following items:")
st.write("Profits:", profits)
st.write("Weights:", weights)
st.write("Max Weight (W):", W)

# Calculate knapsack solution
total_profit, weight_taken, ratio = fractional_knapsack(W, weights, profits)

# Display results
st.write("Profit:", profits)
st.write("Weight:", weights)
st.write("Ratio (Profit/Weight):", ratio)
st.write("Weight Taken (as fraction):", weight_taken)
st.write("Total Profit:", total_profit)
