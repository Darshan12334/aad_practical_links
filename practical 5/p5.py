import streamlit as st

def min_coins(target, coins):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_used = [0] * (target + 1)  # To store the coin used to reach each amount

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin  # Store the coin used at this step

    # To get the list of coins used
    if dp[target] == float('inf'):
        return -1, []
    
    result_coins = []
    current_amount = target
    while current_amount > 0:
        result_coins.append(coin_used[current_amount])
        current_amount -= coin_used[current_amount]

    return dp[target], result_coins

# Streamlit UI
st.title("Minimum Coins Calculator")
target = st.number_input("Enter the target amount (in Rs):", min_value=1, step=1, value=9)
coins = [1, 4, 6]

if st.button("Calculate"):
    result, coins_used = min_coins(target, coins)
    if result != -1:
        st.success(f"The minimum number of coins required to make Rs. {target} is: {result}")
        st.write(f"Coins used: {coins_used}")
    else:
        st.error(f"It's not possible to make Rs. {target} with the given coin denominations.")
