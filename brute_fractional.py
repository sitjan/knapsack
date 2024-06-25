from itertools import combinations


def brute_fract(weight, profit, capacity):
    n = len(weight)
    highest_profit = 0
    optimal_combination = []
    items = list(range(n))
    frac_value = []
    frac = -1  # Initialize to -1 to signify no fractional item selected

    # Solve 0/1 knapsack first
    for i in range(n + 1):
        for combination in combinations(range(n), i):
            total_weight = sum(weight[x] for x in combination)
            total_profit = sum(profit[x] for x in combination)

            if total_profit > highest_profit and total_weight <= capacity:
                highest_profit = total_profit
                optimal_combination = combination

    # Calculate remaining capacity
    total_weight = sum(weight[x] for x in optimal_combination)
    remaining_capacity = capacity - total_weight

    # Find the best fractional item
    max_frac_value = 0
    for i in items:
        if i not in optimal_combination and weight[i] > 0:
            current_frac_value = (profit[i] / weight[i]) * remaining_capacity
            if current_frac_value > max_frac_value:
                max_frac_value = current_frac_value
                frac = i

    highest_profit += max_frac_value
    return optimal_combination, highest_profit, frac


# Example usage
weights = [10, 20, 25, 30]
profits = [100, 200, 230, 340]
knapsack_capacity = 45

optimal_items, max_profit, fracitem = brute_fract(
    weights, profits, knapsack_capacity)

print(f"Knapsack capacity: {knapsack_capacity}")
print(f"Optimal combination of items: {optimal_items}")
print(f"Maximum profit: {max_profit:.2f}")
print(f"Fractional item of choice: {fracitem}")
