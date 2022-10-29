# 概述
- 对于[[trivial-case]]（空，0等）往往需要特判
  - 特判既包括你代码的特判，也包括人肉输入特殊数据（空）等做测试集
  - 参考[[general-principles/debug]]
- 拿到问题，优先考虑特判的好处
  - 助于严谨，防止特殊值报错
    - 例如[[finetune]]有提到
  - 助于[[oi-wiki/recursion]]，[[induction]]思考，作为“起步”
  - 检查一些基本情况的正确性，防止特别低级错误
  - 参考[[2-brain-teasers]]，[[introduction]]
- 有时特判可以合并[[化归]]到一般情况，节省代码量
  - 往往规模加一，但合并了特判
  - 例如[[21-merge-two-sorted-lists]]链表头
  - 例如[[2216-minimum-deletions-to-make-array-beautiful]]末尾增加一个
# 例子
- 涉及空
  - [[21-merge-two-sorted-lists]], [[25-merge-k-sorted-lists]]
- 出口（空，0，1等等）
  - [[25-merge-k-sorted-lists]]中，注意“1”是递归出口（[[divide-and-conquer]]的最底层）
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
- 凡是涉及“配对”（pairwise）的，都要特别小心两者相同的情况
  - 例如[[parallelism]]中torch综合应用“算法题”示例中减去`torch.eye(p)`
- 考虑输入为空的情况
  - 例如：`1`出现在二维数组`[[0,1],[1,2],[2,3]]`中的`0, 1`两个子数组，想输出`[0, 1]`
  - 解决方案：`a = 1 == torch.tensor([[0,1],[1,2],[2,3]]); b = a.sum(axis=1)`
  - 但：如果`1`不出现，就崩了