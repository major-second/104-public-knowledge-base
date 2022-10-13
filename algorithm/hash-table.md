核心就是快速（$O(1)$地）查找
- 索引可以看成特殊的哈希（比如
https://leetcode-cn.com/problems/valid-sudoku/submissions/
https://leetcode-cn.com/problems/check-permutation-lcci/
）
- 把字符串对应到一个数的方法：典型就是每次`*171`再`%1000000007`（十位数）。
  - 要每个子串的哈希：$O(n)$弄每个前缀，这样每个子串就容易有了。
- https://leetcode.cn/problems/count-good-meals/submissions/
  - 这题说明涉及求和的，可以维护哈希表表示“某个数字出现多少次”
  - 相比[[双指针]]，这不需要排序