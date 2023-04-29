- 参考
  - [[self-similarity]]
  - [[induction]]
  - [[recurrence]]
  - [[oi-wiki-basic/recursion]]
  - [[greedy]]
  - [[5-dp]]

[toc]
# 理解方式
## principle of optimality
- [[5-dp#principle of optimality]]
## 优中选优
- 递推[[recurrence]]利用之前已经计算过的东西
- 优中选优。“优”都是基于之前算出过的值
- 和[[greedy]]联系
  - 如果不需要选，那就是[[greedy]]
  - 但有时只是[[naming]]，不同层次来看dp和[[greedy]]
# 多次退化
- 参考[[general-principles/special-case]]思想，多次退化
- 越来越不贪心，需要存储、优中选优的可能性越来越多
## knapspack
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
- 从[[dp#优中选优]]角度讲，这里都是常数种类的“优”，渐近空间复杂度等于渐近时间复杂度
  - 如只能用一次的背包问题中，三种“优”，两个`max`操作
## [[1388-pizza-with-3n-slices]]
- 我们先不考虑首尾相接的问题，认为是“$3n$个元素中找$n$个两两不相邻使和最大”
  - 如果选最大的任意个元素，那就是[[greedy]]，不需要选，一股脑所有数放上即可
  - 如果选最大的任意个不相邻元素，那就是“01”型动态规划，存储两种可能（目前为止最后一个数选了/没选），每次从两种可能优中选优
  - 如果选最大的$n$个不相邻元素，那需要存储的状态更多，也就是之前最后一个数选了/没选，然后最多已经选取了多少个元素
    - 换句话说：你选了太多垃圾元素占“名额”不好
# 其它举例
- [[368-largest-divisible-subset]]
  - 讲到不能[[greedy]]，需要优中选优
- https://leetcode.cn/problems/longest-palindromic-substring/
  - 如果普通动规，需要$n^2$
  - 注：[[manacher]]只需要$O(n)$
# [[high-dimension]]
- 有多少维的信息要存储就是多少维的dp
  - [[dp#knapspack]]中有2维的：当前占用重量+已经考察的数组长度
  - [[dp#Pig游戏]]3维：$(我的分数,对方分数,我的浮盈)$
# 注意
- 选用哪个变量
  - 比如https://leetcode.cn/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
    - 需要选择堆编号
  - 比如[[shortest-path#floyd]]，选择“中转站”编号
- 注意选择方向
  - 例如[[10-regular-expression-matching]]，从后往前看，即可[[dp#状态压缩]]
# 状态压缩
- 把不需要的扔掉，节省空间
- [[10-regular-expression-matching]]
- [[72-edit-distance]]
# 和其它联系
- 子问题相似性质，和[[self-similarity]]有强联系
- [[calculate-v]]中暴力计算用的就是dp
  - 即使不是暴力计算，整个强化学习中也充满了dp思想
# 01动规
- 是[[general-principles/special-case]]
- 因为“非此即彼”，所以生成路径有时有特殊方法
## Pig游戏
- [Pig游戏规则](https://en.wikipedia.org/wiki/Pig_(dice_game))
  - 任何时候两种选择
    - 摇：摇其它数字得浮盈，摇1浮盈亏掉
    - 也可以选择停下交给对方落袋为安
- 解
  - 这里需要注意[[algorithm/special-case]]：还没摇肯定没理由交给对方。这是动规出口之一
  - 通过生成三维dp表
    - $(我的分数,对方分数,我的浮盈)\to 我赢概率$表
    - 表中并未显式存储每一步行动如何
    - 告诉我最优选择是摇还是不摇？
    - 那直接做一次对比：当前概率和$1-落袋为安轮到对方对方赢概率$ 谁大，即可