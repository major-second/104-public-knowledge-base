# 概述
- 对于[[special-case]]（空，0等）往往需要特判
  - 特判既包括你代码的特判，也包括人肉输入特殊数据（空）等做测试集
  - 参考[[general-principles/debug]]
- 拿到问题，优先考虑特判的好处
  - 助于严谨，防止特殊值报错
    - 例如[[finetune]]有提到
  - 助于[[oi-wiki-basic/recursion]]，[[induction]]思考，作为“起步”
  - 检查一些基本情况的正确性，防止特别低级错误
    - 有时还能发现[[counter-examples]]
    - 有时推广到0，无穷等极限情况，问题本质改变，比如[[5-brownian-motion-and-stochastic-calculus]]中的“何时在1停下”
  - 参考[[2-brain-teasers]]，[[introduction]]
- 有时特判可以合并[[化归]]到一般情况，节省代码量
  - 往往规模加一，但合并了特判
  - 例如[[21-merge-two-sorted-lists]]链表头
  - 例如[[2216-minimum-deletions-to-make-array-beautiful]]末尾增加一个
# 去重
- 带来问题
  - 凡是涉及“配对”（pairwise）的，都要特别小心两者相同的情况
    - 例如[[parallelism]]中torch综合应用“算法题”示例中减去`torch.eye(p)`
    - 例如[[1-two-sum]]
  - [[sort-intro]]提到：重复元素可能带来“排序稳定性”问题
- 去重方法
  - 内层`j`从`i+1`开始而非`i`
  - 维护最近的值，然后每次判断是否和最近的值相同，参考[[loop]]
    - 相同就跳过（往往体现为[[loop]]的`continue`）
    - 不同，就正常运行，同时要更新“最近的值”
  - 内置调包
    - [[algorithm]]中讲的内置`unique(begin, end)`，去除相邻重复的
    - [[associative]]中`unordered_set`等
      - 例如[[200-number-of-islands]]中有
  - 特事特办，单独讨论
    - 例如[[1-two-sum]]的哈希做法
  - 多维护更多属性防止重复（看作不同的）
    - 往往使用[[pair]]
    - 例如[[2343-query-kth-smallest-trimmed-number]]
- 例子
  - [[18-4sum]]
# 其它
- 除数不能为0
  - 如[[679-24-game]]，需要非常仔细讨论0的影响（和搜索方向是前向还是后向有关，参考[[search/misc]]）
- 等于（临界）造成麻烦
  - 例子
    - [[845-longest-mountain-in-array]]
    - [[154-find-minimum-in-rotated-sorted-array-ii]]中，等于的情况大大增多了问题复杂度、时间
  - [[sort-intro]]中稳定性也算这个的例子
- 考虑输入为空的情况
  - [[21-merge-two-sorted-lists]]
  - [[25-merge-k-sorted-lists]]
  - [[430-flatten-a-multilevel-doubly-linked-list]]
  - [[4-median-of-two-sorted-arrays]]中，其中一个输入为空的情形
  - [[686-repeated-string-match]]中，`l_l==0`情形特殊！
  - 一个实际例子
    - `1`出现在二维数组`[[0,1],[1,2],[2,3]]`中的`0, 1`两个子数组，想输出`[0, 1]`
    - 解决方案：`a = 1 == torch.tensor([[0,1],[1,2],[2,3]]); b = a.sum(axis=1)`
    - 但：如果`1`不出现，就崩了
- [[oi-wiki-basic/recursion]]出口（[[divide-and-conquer]]的最底层）往往是特例
  - 往往是空，0，1等等
  - 如[[25-merge-k-sorted-lists]]中，注意“1”也是递归出口
# 图相关
- 环带来麻烦
  - 例如[[topo]]，[[210-course-schedule-ii]]
- 负数带来麻烦，例如[[shortest-path]]中dijkstra
# 具体题目例子
- https://leetcode.cn/problems/can-i-win/submissions/
特判和为0（本来“不拿就够”一般指先手输，但和为0算先手赢）
特判所有数之和小于待求
- https://leetcode.cn/problems/zigzag-conversion/submissions/
3行循环长度4，4行循环长度6，1行循环长度，0？所以要特判！
注：当然这题没必要模拟。因为字符串本来就可以随机访问，又不是链表
- https://leetcode.cn/problems/remove-nth-node-from-end-of-list/submissions/
我写的代码是先看总共5个节点，然后5-2=3，然后`while(--total)`即循环3-1=2次`p=p->next;`走到对应位置
这时，要考虑`total`一来就0的情况！
但是如果用哑节点，那就不需要了（参考官方题解）
- https://leetcode.cn/problems/simplify-path/submissions/
核心部分
```cpp
if (former==".." ){
    if (!p.empty()) p.pop_back();
}
else if (former!="."){
    p.push_back(former);
}
```
- 注意
  - 不能把`!p.empty()`提前到上一级的`if`里
    - 根据题意，并不是说根目录`..`就直接输出`/`，而是根目录`..`就不动，但之后还可能到下级目录！（这是unix操作的常识）
  - 最后还需特判是否为空
    - 空串要手动加上`/`，其它情况末尾不能有`/`