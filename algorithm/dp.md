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
- “优”都是基于之前算出过的值
- 递推[[recurrence]]利用之前已经计算过的东西
  - 即子问题的最优
  - 其实和[[dp#principle of optimality]]道理一样
- 和[[greedy]]联系
  - 如果不需要选，那就是[[greedy]]
  - 但有时只是[[naming]]，不同层次来看dp和[[greedy]]而已
### 优中选优举例
- 01 [[knapspack]]
  - 可重复用物品：m个子问题，每个子问题$O(n)$种“优”
  - 只能用一次：
    - $nm$个子问题
    - 每个子问题常数（3）种“优”，两个`max`操作
- [[floyd]]
  - $n^3$个子问题，每个子问题常数（2）种优，1个`max`操作
  - 属于[[dp#01动规]]，非此即彼
- [[bellman-ford]]
  - $V^2$个子问题，每个子问题表示某个点最多经过若干条边时最短路长度
  - 每个子问题**点的入度**种优
  - 故复杂度$VE$
# 多次退化
- 参考[[general-principles/special-case]]思想，多次退化
- 越来越不贪心，需要存储、优中选优的可能性越来越多
## knapspack
- [[knapspack]]，能体现[[general-principles/special-case]]多次退化
## [[1388-pizza-with-3n-slices]]
- 我们先不考虑首尾相接的问题，认为是“$3n$个元素中找$n$个两两不相邻使和最大”
  - 如果选最大的任意个元素，那就是[[greedy]]，不需要选，一股脑所有数放上即可
  - 如果选最大的任意个不相邻元素，那就是“01”型动态规划，存储两种可能（目前为止最后一个数选了/没选），每次从两种可能优中选优
  - 如果选最大的$n$个不相邻元素，那需要存储的状态更多，也就是之前最后一个数选了/没选，然后最多已经选取了多少个元素
    - 换句话说：你选了太多垃圾元素占“名额”不好
# 计数方案数
- 总方案来自于子问题方案
  - 总方案数来自于子问题方案数
  - 因此无论是判是否存在还是计数，都可以考虑用dp
- [[115-distinct-subsequences]]
## 电话盘
- ```
  1 2 3
  4 5 6
  7 8 9
  * 0 #
  ```
  - 电话盘，全由数字组成，不以0或1开头，且满足“跳马”关系的n位数电话号有多少
  - 最佳当然是dp，效率低的也可以是[[backtrack]]
  - [[graph-for-topo]]
  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  int main(){
      vector<vector<int>> graph;
      graph.push_back(vector<int>{6, 4}); // 0
      graph.push_back(vector<int>{8, 6}); // 1
      graph.push_back(vector<int>{7, 9}); // 2
      graph.push_back(vector<int>{4, 8}); // 3
      graph.push_back(vector<int>{3, 9, 0}); // 4
      graph.push_back(vector<int>{}); // 5
      graph.push_back(vector<int>{1, 7, 0}); // 6
      graph.push_back(vector<int>{2, 6}); // 7
      graph.push_back(vector<int>{1, 3}); // 8
      graph.push_back(vector<int>{2, 4}); // 9

      int length = 7;
      length--;
      vector<int> num_prefices = {0, 0, 1, 1, 1, 1, 1, 1, 1, 1};
      // 0 feasible prefix for valid number with the end of the prefix as 0
      // 1 feasible prefix for valid number with the end of the prefix as 2, namely 2

      while(length-- > 0){
          vector<int> new_num_prefices = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
          for (int i = 0; i <= 9; i++) for (int dst:graph[i]) new_num_prefices[i] += num_prefices[dst];
          num_prefices = new_num_prefices;
          // after 1 iteration
          // 2 feasible prifices for valid number with the end of the prefix as 0, namely 60 and 40
          // 2 feasible prifices for valid number with the end of the prefix as 4, namely 34 and 94
          // etc
      }
      int total = 0;
      for (auto i:num_prefices) total += i;
      cout<<total<<endl;

      return 0;
  }
  ```
# 其它举例
- [[368-largest-divisible-subset]]
  - 讲到不能[[greedy]]，需要优中选优
- https://leetcode.cn/problems/longest-palindromic-substring/
  - 如果普通动规，需要$n^2$
  - 注：[[manacher]]只需要$O(n)$
# [[high-dimension]]
- 有多少维的信息要存储就是多少维的dp
  - [[knapspack]]中有2维的：当前占用重量+已经考察的数组长度
  - [[dp#Pig游戏]]3维：$(我的分数,对方分数,我的浮盈)$
# 注意
- 选用哪个变量
  - 比如https://leetcode.cn/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
    - 需要选择堆编号
  - 比如[[floyd]]，选择“中转站”编号
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