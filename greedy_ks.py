def greedy(weights, profit, capacity):
    n = len(weights)
    combination = []
    ratio = []
    total_weight = 0
    total_profit = 0
    final_profit = 0

    for i in range(len(weights)):
        ratio.append(profit[i]/weights[i])

    for i in range(len(weights)):
        if ratio[i] == max(ratio):
            total_profit += profit[i]
            total_weight += weights[i]
            if (total_weight < capacity and total_profit > final_profit):
                combination.append(weights[i])
                final_profit = total_profit
                del profit[i]
                del weights[i]

    return combination, final_profit

    # Example usage
weights = [10, 20, 30, 40, 50]
profit = [60, 100, 120, 140, 160]
knapsack_capacity = 100

optimal_items, max_profit = greedy(weights, profit, knapsack_capacity)

print(f"Knapsack capacity: {knapsack_capacity}")
print(f"Optimal combination of items: {optimal_items}")
print(f"Maximum profit: {max_profit}")
