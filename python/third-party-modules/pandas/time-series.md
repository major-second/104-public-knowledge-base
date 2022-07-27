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
  - 切片含两端
## 进阶
- [参考](https://blog.csdn.net/weixin_42033491/article/details/108104305)