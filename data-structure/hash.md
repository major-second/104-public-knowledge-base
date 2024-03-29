- https://oi-wiki.org/ds/hash/
  - ```text
    哈希表又称散列表，一种以「key-value」形式存储数据的数据结构。所谓以「key-value」形式存储数据，是指任意的键值 key 都唯一对应到内存中的某个位置。只需要输入查找的键值，就可以快速地找到其对应的 value。可以把哈希表理解为一种高级的数组，这种数组的下标可以是很大的整数，浮点数，字符串甚至结构体。
    ```
  - 核心就是快速（$O(1)$，常数地）查找
  - 实现时是`key - index - value`，相当于[[encode-decode]]成index
# 索引
- 可以看成哈希[[general-principles/special-case]]
  - 键是整数
  - 常数时间复杂度查找确实
  - 此处[[encode-decode]]就是不变
- 参考[[打表]]
## 索引的例子
- [[counting-sort]]
- [[sliding-window]] 值域小时[[character/quantile]]
- [[41-first-missing-positive]]方法一
  - 数组索引就是哈希，[[inplace]]变换不占额外空间
  - 通过正负，用一个`int`同时表示了一个`int`和一个`bool`
    - [[encode-decode]]思想
- [[778-swim-in-rising-water]]
- https://leetcode.cn/problems/valid-sudoku/
  - 81个格子，每个格子以**常数**时间找到对应的地方把相应计数器加一
- https://leetcode.cn/problems/check-permutation-lcci/
  - 对于C++可以把字符方便转化成整数，从而可用索引
  - 对于python，最简单的想法就是弄字典（哈希），这就不是索引了。这也看出索引和哈希的联系
- https://leetcode.cn/problems/count-good-meals/
  - 这题说明涉及求和的，可以维护哈希表表示“某个数字出现多少次”，键是数字，值是多少次
  - 相比[[two-pointers]]，这不需要排序，是更优方法
# [[encode-decode]]技术
- 大整数取模
  - `%1000000007`（十位数）很常见。是个足够大的质数
- 防止编码冲突：取两个不同质数
- 把字符串对应到一个数：相当于[[encode-decode#进制转换]]
  - 典型就是127进制
  - 这样[[reduction]]到大整数
  - 滚动计算：[[30-substring-with-concatenation-of-all-words]]
- 拓展：如果要每个子串的哈希
  - 参考[[partial-sum]]，做减法
  - $O(n)$空间
- 拓展：[[49-group-anagrams]]
  - 把字符串中每个字符各出现多少次对应到一个数，也可以类似操作
  - 即“26位101进制的数，每一位表示这个字母出现多少次”