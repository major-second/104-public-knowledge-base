- 前置
  - [[pandas/installation]]
  - [[matplotlib/basics]]
## 基础
- [参考](https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/)
- shell中`wget https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv`即可下载数据（需要[[linux]]代理）
### 日期时间
- `import pandas as pd`
- 基础使用（自动推断格式）
  - `pd.to_datetime('2018-01-15 3:45pm')`
  - `pd.to_datetime('7/8/1952')`
  - `pd.to_datetime('7/8/1952', dayfirst=True)`
  - `pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'])`
    - 返回一个序列`DatetimeIndex`
    - 底层：64-bit的整数（纳秒）
- 加速：指定格式如`format='%m/%d/%y'`
### 基础命令
- `opsd_daily = pd.read_csv('opsd_germany_daily.csv')`
  - 读取`.csv`
- `.shape`形状（第0维往往表示多少条数据，第1维表示多少维）
- `.dtypes`类型
- `.head(3)`, `.tail(3)`, `.sample(3)`看示例
### `index`
- 有了日期时间，即可利用pandas自动读日期时间的功能，设置index
  - 如果日期字段名是`Date`
  - 则`opsd_daily = opsd_daily.set_index('Date')`
  - 此时可再看`.shape, .dtypes, .sample(3)`的变化
- `.index`取出index序列
- 二合一过程（读取和设置`index`）：`opsd_daily = pd.read_csv('opsd_germany_daily.csv', index_col=0, parse_dates=True)`
  - `0`号栏此时对应`Date`
- 有了index，此时可以用`.loc['2014-01-20']`，乃至`.loc['2014-01-20':'2014-01-22']`，`.loc['2006-12']`等和时间相关的feature
- loc很多坑，[参考文档](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?highlight=loc#pandas.DataFrame.loc)
  - 和普通的`[]`不同，`.loc[]`**切片含两端**
  - 普通的`[]`只能取`[start:end]`这样，不能单取一个`[0]`这样（因为单取针对的是取键, key）
  - `.loc`默认是“绝对”的索引，而不是相对
    - `.loc[0]`中的0是某个数据条目的一个属性，而不是其在某个序列中的排序
    - 也就是“二次”切片时不能“相对”切。例如`d.loc[3:4]`的结果就不能再`.loc[0]`了！
    - 所以`.loc`似乎天然适合用于处理关于日期时间的索引切片
  - `.loc[单个]`和`.loc[start:end]`出来的数据类型不一样（这点不同于python原生字符串切片）
    - 所以对两种出来结果再切片时效果也当然不同
## 进阶
- [参考](https://blog.csdn.net/weixin_42033491/article/details/108104305)