- 最简单：没有重量限制，那就一股脑加上，这是最[[greedy]]的
- 稍微复杂：有重量限制，重量都是整数
  - 那么dp，存储用了多少重量获得多少
  - 这时当然还能[[dp#状态压缩]]
  - ```python
    def solveKnapsack(profits, weights, capacity):
        cap2max_profit = [0] # 0 for 0
        
        for i in range(1, capacity + 1):
            curr_max = cap2max_profit[i - 1]
            for w, p in zip(weights, profits):
                prev_max = cap2max_profit[i - w] if i - w >= 0 else -float('inf') # invalid
                curr_max = max(curr_max, prev_max + p)
            cap2max_profit.append(curr_max)
            
        return cap2max_profit[-1]

    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    capacity = 5
    print(solveKnapsack(profits, weights, capacity))

    weights = [2, 3, 3, 4]
    profits = [4, 5, 7, 7]
    capacity = 5
    print(solveKnapsack(profits, weights, capacity))
    ```
- 最复杂：有重量限制且每种物品只能使用一次
  - 二维dp，状态索引是：目前最高用到的物品编号+重量
  - 核心：利用[[monotonous]]地按顺序添加物品，避免需要存储$2^n$种状态。只需要看还剩下多少种物品可以加
  - ```python
    def solveKnapsack(profits, weights, capacity):
        length = len(profits)
        cap2max_profit = [[0 for _ in range(length)]] # [0][i] = 0 means: weight = 0, allowed to use [0, i]: 0
        for i in range(1, capacity + 1):
            cap2max_profit.append([(i >= weights[0]) * profits[0]]) # [i][0] = profits[0] means: ...
            for j in range(1, length):
                curr_max = max(cap2max_profit[i - 1][j], cap2max_profit[i][j - 1])
                if i - weights[j] >= 0:
                    curr_max = max(curr_max, cap2max_profit[i - weights[j]][j - 1] + profits[j])
                cap2max_profit[-1].append(curr_max)
        return cap2max_profit[-1][-1]

    weights = [2, 3, 3, 4, 4]
    profits = [4, 5, 7, 7, 10]
    capacity = 8
    print(solveKnapsack(profits, weights, capacity))

    weights = [2, 3, 3, 4, 4]
    profits = [4, 5, 7, 7, 8]
    capacity = 8
    print(solveKnapsack(profits, weights, capacity))
    ```