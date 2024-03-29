- [[complexity]]
- [[master-theorem]]
- number swap
  - 脑筋急转弯！比如`i+=j;`先，或者`i^=j;`先
- unique element
  - 看清题目，排序了！
- [[horner]]'s algorithm
- moving average
  - [[sliding-window]]，滑动求
  - [[rolling]]是实际实现
- sorting algorithm
  - [[quick-sort]], [[merge-sort]], [[n2-sort]]等
- random permutation
  - 可以先生成随机数列，再排序，类似[[order-statistics]]思想
  - Knuth算法：相当于先随机选一个到1号，再2号……实操是每次$swap(A[i], A[Random(i,n)])$
    - 注意有可能不交换
  - 未知长度文件
    - 比如也生成随机数列再看最大（需要随机空间）
    - 比如第二个数有1/2可能上位，第三个可能1/3上位等等
- search algorithm
  - $\frac {3n}2$找最大最小：先分胜败者组
  - 找第一个非零：相当于排序好的01数组，二分[[binary-search]]
  - 二维情况
    - 法一：$O(n) = 3O(n/2) + O(1)\Rightarrow O(n) = n^{3/2}$
      - 注意不是$n/4$，因为$n$是边长
    - 法二（答案）：从右下角开始，右边最后一列往上搜，直到超过$x$；然后左边往左直到小于$x$……以此类推
      - 思想：一次排除一个集合。联想[[two-pointers]]
- fibonacci numbers
  - 首先是分析简单[[oi-wiki-basic/recursion]]暴力方法的复杂度：也是类似于斐波那契，$\Theta(\phi^n)$
  - 合理的：递推求解，空间换时间，$O(n)$
  - 进阶的：用矩阵乘法（幂），然后[[divide-and-conquer]]快速算幂
    - 注意由于[[float]]误差，不能直接算浮点的幂
- maximum contiguous subarray
  - 我的思路：[[dp]]优中选优，每次看：要不然是只有当前数，要不然是之前的一段加上当前，得到**当前位置结尾的**子串中和最大的
  - 和标答本质一致