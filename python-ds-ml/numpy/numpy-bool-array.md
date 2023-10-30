# 前置
- [[dtype]]
- [[numpy-basics#Comparison]]运算得到布尔array
- [官方文档](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_)
  - `bool_`就是`bool8`，即8个bit
# 用作判断
- 直接用作判断条件是“ambiguous”，会报错，也就是不能直接`if <array>`
- 你想想，你这个`if <array>`到底是表示是否空还是是否全`False`，还是什么呢，确实不清楚嘛
# 应用
- 可以`(a > 0) * a`得到`a`的正的部分
  - 说明布尔数组可被强制类型转换成整数
- 可以`np.where()`筛出为`True`的那些下标，这些下标排成一列，结合[[numpy-indexing]]
- 结合[[numpy/quantile]]，`max`等可以找到[[numpy/quantile]]位置
  - 求分位数时会在靠近的数间作插值，所以必须用`<`而非`==`
# 操作
- 可（隐式）强制类型转换为整数
- 不能使用一元`-`变成`-1`和`0`组成的数组（报错）
- 但可用
  - 一元`~`（否定）
  - 二元`&`（与）、`|`（或）
    - 不是`&&`、`||`