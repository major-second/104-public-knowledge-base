- [[discrete-continuous]]
- [知乎帖子：回归难点](https://www.zhihu.com/question/59829734/answer/1996265463)
    1. [[discrete-continuous]]导致问题
       1. 要求精细，难度高
       2. 样本不均衡时直接有些“类”（即区间）直接无样本
    2. 值域无穷导致问题：新样本真实label没见过没法外推
- 可能联系（解决方法）：先分[[bucket]]，然后桶内finetune