- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
- https://zhuanlan.zhihu.com/p/101284491
# examples
- 基础
  - `df.groupby(['Animal']).mean()`
- [[multi-index]]
  - 前提：`index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))`
  - `df.groupby(level=0).mean()`
  - `df.groupby(level="Type").mean()`
- 常见错误：`df.groupby(a)[b].mean()`可以，但如果一来`df[b]`，你就没a了
# kwargs
- `sort`：默认会排序！可能不需要
- `as_index`：默认对dataframe会把group标准变为index
# 用法
- `for`迭代循环得到 `label, sub_df`
- [[pandas-agg-basics]]中很多都能用
  - `min, max, sum, mean, median, std, var, count`
  - `groupby(key).transform('mean')`: 不改变形状，原来多少row还是多少row，只是把新的加上
- [[pandas-apply]]：以dataframe为单位
  - 效率也一样低
# multiple-columns
- https://datagy.io/pandas-groupby-multiple-columns/
- 需要输入list而不是tuple
  - 联想[[multi-index-loc]] tuple和list语义不同