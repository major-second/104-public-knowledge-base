- 参考
  - [[binary-search]]
  - [[monotonous]]
- ```python
  >>> from bisect import bisect, bisect_left, bisect_right
  >>> bisect_left([1,2,3],2)
  1
  >>> bisect([1,2,3],2)
  2
  ```
- 解说
  - `bisect`出来结果是个指标
  - 把新的`2`插到`1`号位就是左边（`bisect_left`），否则是默认的右边