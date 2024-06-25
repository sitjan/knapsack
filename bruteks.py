from itertools import combinations


def bruteforce(weight, profit, capacity):
    n = len(weight)
    optimal_combination = []
    highest_profit = 0
    for i in range(n + 1):  # Changed to n+1 to include all possible combinations
        for combination in combinations(range(n), i):
            total_weight = sum(weight[x] for x in combination)
            total_profit = sum(profit[x] for x in combination)
            if (total_profit > highest_profit and total_weight <= capacity):
                highest_profit = total_profit
                optimal_combination = combination
    return optimal_combination, highest_profit


# Example usage
weights = [10, 20, 30, 40, 50]
profits = [60, 100, 120, 140, 160]
knapsack_capacity = 100

optimal_items, max_profit = bruteforce(weights, profits, knapsack_capacity)

print(f"Knapsack capacity: {knapsack_capacity}")
print(f"Optimal combination of items: {optimal_items}")
print(f"Maximum profit: {max_profit}")

print("\nDetails of selected items:")
total_weight = 0
for i in optimal_items:
    print(f"Item {i}: Weight = {weights[i]}, Profit = {profits[i]}")
    total_weight += weights[i]

print(f"\nTotal weight of selected items: {total_weight}")
