- 前置[[numpy/basic]]
- 参考[[pytorch/misc/reshape]]，两种可做比较
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