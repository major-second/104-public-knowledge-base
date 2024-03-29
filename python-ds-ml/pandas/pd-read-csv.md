- 前置
    - [[series-dataframe]]
    - [[tabular/source]]
    - [[settings-and-configurations]]
- 参考
  - https://zhuanlan.zhihu.com/p/127376643


# 内容
- `df = pd.read_csv('data.csv')`
  - `header=None`: 没有header
    - `names=<list>`：自动认为没有header且你自己加名字
  - `parse_dates=...`: 直接parse出日期
    - 可以同时利用`index_col`作为[[pandas-index]]
  - `sep, delimiter, delim_whitespace`参数指定delimiter
    - `delim_whitespace=True`等效于`sep='\s+'`不等效于`sep=' '`
    - 参考[[regex]]
  - `skiprows=2, nrows=3`: 如果从0开始编号，则取了2，3，4行
  - `skiprows=lambda x: x > 0 and x % 2 == 0`
- `df.to_csv('data_1.csv')`
  - 注意这两者不“互为逆运算”，因为可能有一列额外的[[pandas-index]]存在
# 拓展
- read_feather, read_parquet, read_excel等都有，不过可能需要不同的包，比如`pyarrow`，`openpyxl`等