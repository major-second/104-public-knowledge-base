- 可以常和[[numpy/quantile]]等连用
  - `df.quantile(x)`
  - `df.quantile([x, y])`
- [参考](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.clip.html)
- 按`index`方向
  - 逐行看
  - `df.clip(series, series + 4, axis=0)`
    - 其中`series`可以有[[nan]]表示忽略
  - 可能需要index去重
- 另一个方向`columns`，逐列看
  - 相当于[[feature-engineering]]手段