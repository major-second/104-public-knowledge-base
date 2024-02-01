- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
# examples
- 基础
  - `df.groupby(['Animal']).mean()`
- [[multi-index]]
  - 前提：`index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))`
  - `df.groupby(level=0).mean()`
  - `df.groupby(level="Type").mean()`