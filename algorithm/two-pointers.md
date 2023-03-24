- [[11-container-with-most-water]]
    - 双指针之间包括了“可能”范围
    - 过程中不断去除不可能的组合
      - 移动一次指针，实际上是除去了一组以某个为边的组合
      - 例如移动左指针（脚标位置）从1到2，右指针处于5，那就是`(1, 4), (1, 3), (1, 2)`这些组合都不可能成立，不用考虑了
- https://leetcode.cn/problems/3sum-closest/
    - 同样的道理，移动一次指针，实际上是除去了一组以某个为边的组合
- 变种：求使得`A[i] != A[j]`最大`j-i`
  - 此时你`[1, 1, 1, 2, 2, 2, 1, 1]`，左边移到3号，右边移到5号
  - 并不是说直接5和3了，而是“3到末尾”和“5到开头”比较
  - 也就是右边指针从7移到6，没有排除(3,7)，只排除了(0,7), (1,7), (2,7)
  - 所以这个是错的
    ```python
    def solution(A):
        N = len(A)
        left, right = 0, N - 1
        while 1:
            if A[left] != A[right]:
                return right - left
            if left + 1 >= right:
                return 0
            if A[left] != A[left + 1] or A[right] != A[right - 1]:
                return right - left - 1
            left += 1
            right -= 1
    ```
- 注意
  - `while(lo<hi)`，不要写`!=`，比较保险！