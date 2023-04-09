- https://leetcode.cn/problems/count-good-meals/submissions/
  - 搞错下标和数据内容
    - 第一次：判断`l[i] + l[j]`和`s`（和）的关系，错写成了`i + j`
    - 第二次：题意中的不同菜品，是下标不同，而不是值不同
      - 这还导致了边界情况：最大可能的和应该是最大数的2倍，而不是最大数的2倍减1
    - 第三次：使用[[two-pointers]]，两边逼近时，是要看`i, j`两下标关系，而不是值小于等于或小于来停止
- https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
  - 看清题意！他说每个list先有一个数字表示list长度
  - 不过对于python来说就很简单，直接`input().split()[1:]`即可
- [[overflow]]
- [[float]]误差
- 首尾相接
  - [[1388-pizza-with-3n-slices]]，[[514-freedom-trail]]中的环形数组
- [[off-by-one-errors]]
# zero division
- [[batchnorm]]
- [[679-24-game]]
# uniqueness
- 带来问题
  - 凡是涉及“配对”（pairwise）的，都要特别小心两者相同的情况
    - 例如[[parallelism]]中torch综合应用“算法题”示例中减去`torch.eye(p)`
    - 例如[[1-two-sum]]
  - [[sort-intro]]提到：重复元素可能带来“排序稳定性”问题
  - 题目本来就要求非重，如[[geometry]]格点三角形
- 去重方法
  - 内层`j`从`i+1`开始而非`i`
  - 滑窗去重：[[sliding-window]]
  - python中的`set`
  - 维护最近的值，然后每次判断是否和最近的值相同，参考[[loop]]
    - 相同就跳过（往往体现为[[loop]]的`continue`）
    - 不同，就正常运行，同时要更新“最近的值”
    - 简单例子[[18-4sum]]
    - 比较有意思的例子：[[313-super-ugly-number]]，出现重复了，相应指针直接动，`i`不增（也就是循环体内部`i--`）
  - 内置调包
    - [[algorithm]]中讲的内置`unique(begin, end)`，去除相邻重复的
    - [[associative]]中`unordered_set`等
      - 例如[[200-number-of-islands]]中有
  - 特事特办，单独讨论
    - 例如[[1-two-sum]]的哈希做法
  - 多维护更多属性防止重复（看作不同的）
    - 往往使用[[pair]]
    - 例如[[2343-query-kth-smallest-trimmed-number]]
  - [[encode-decode]]思想，例如[[geometry]]中把排序后三边长（平方，为了防止[[float]]误差）作为唯一标识
  - 数学理论保证无重复，如[[general-principles/special-case]]的倒水题
- 多解性
  - [[685-redundant-connection-ii]]多解选最后的，所以代码中“假设法”必须先假设去除 `lastCausedTwoParentsEdge`而不是先假设去除 `firstCausedTwoParentsEdge`