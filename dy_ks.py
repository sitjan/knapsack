def knapSack(capacity, weight, profit, n):
    dp = [0 for i in range(capacity + 1)]

    for i in range(1, n + 1):
        for w in range(capacity, 0, -1):
            if weight[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + profit[i - 1])

    return dp[capacity]


# Example usage
if __name__ == '__main__':
    weights = [10, 20, 25, 30]
    profits = [100, 200, 230, 340]
    capacity = 45
    n = len(profits)
    max_profit = knapSack(capacity, weights, profits, n)
    print(f"Highest profit: {max_profit}")
