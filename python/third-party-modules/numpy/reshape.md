- 前置
  - [[numpy-basics#Array Manipulation]]
- 参考[[pytorch/misc/reshape]]，可做比较
- 应用
  - [[line-collection]]中制造一系列线段
  - [[gym/wrapper]]中改变环境的[[spaces]]
- `array.repeat()`常常和`reshape`一起使用
  - 可以和[[misc/reshape]]中的`expand`比较异同
  - `np.array([2,3]).repeat(3,axis=0)`输出`array([2, 2, 2, 3, 3, 3])`
  - `np.array([2,3]).reshape(-1, 2).repeat(3,axis=0) `输出
    ```python
    array([[2, 3],
          [2, 3],
          [2, 3]])
    ```
# 变为一维
- `a.ravel()` [[share-lock]]
  - [ravel词根](https://www.etymonline.com/search?q=ravel)
    - > as threads become unwoven, they get tangled.
    - 两个矛盾的意思
  - unravel也在上面能看到，只有展开的意思
- `a.flatten()` [[general-copy]]
# newaxis
`[:, np.newaxis]`，新增一个axis，相当于`.reshape(-1, 1)`