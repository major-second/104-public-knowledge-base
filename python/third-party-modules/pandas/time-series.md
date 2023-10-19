- 前置
  - [[pandas/installation]]
  - [[matplotlib/basics]]
  - [[series-dataframe]]
## 基础
### 准备
- [参考](https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/)
- shell中`wget https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv`即可下载数据（需要[[linux-proxy-client]]代理）
- `import pandas as pd`
- 日期时间参考[[timestamps]]
### 基础命令
- `opsd_daily = pd.read_csv('opsd_germany_daily.csv')`
  - 这是读取`.csv`，参考[[series-dataframe]]
- `df.shape`形状（第0维往往表示多少条数据，第1维表示多少维）
- `df.dtypes`类型
- `df.head(3)`, `df.tail(3)`, `df.sample(3)`看示例
- `pd.concat(<DataFrame组成的表，元组等>)`：参考[[manipulation]]，有点像，在时间维上拼起来
- `.min(), .max(), .mean(), .std(), .quantile(q=[0.25,0.75)`等常见操作
- `.skew(), .kurt()`: [[skewness]], [[kurtosis]]
## 迭代
- 直接`for k in df`得到的是键的列表，类似于迭代字典
- 如果`for k in df.iterrows()`（或`itertuples()`，结果没有指标）可以按行迭代
  - 但如果你（经常）用这个，不妨先看看怎么[[parallelism]]并行，要不然你pandas约等于白学233
- `for k in series`当然是按顺序一个一个来，这点可以看出有1个字段的`DataFrame`和`Series`不同
## 进阶
- [一个参考](https://blog.csdn.net/weixin_42033491/article/details/108104305)
- `groupby`和`shift`，`diff`
  - 首先把`df`分成互相间没关系的若干组，有一列`name`表示
  - 然后例如`df['value_shift'] = df.groupby('name')['value'].shift(1)`，就新增一列，每一个“组”之内进行平移
  - 默认省略参数`1`
  - `diff`作差同理
    - 注：所以如果要未来减现在，那就`-df['key'].diff(-interval)`
- `groupby`和`mean`
  - 比如典型操作：`new_df['x']`是旧的`df['x'].rank(pct=True) * 10 // 1`，即0到9整数，`'y'`也同理
  - 然后`new_df.groupby(['x','y']).mean()`即可获得有二维`index`，针对每个`x,y`组合的均值
- 之前说过排序用`sort_index()`，那想获取序号作为数据怎么办？
  - 可以`data['sorted'] = data['key'].rank(ascending=False, method='first')`
  - 其中`ascending`（布尔）决定排序方向，`method`表示相同的怎么处理，`pct`表示是否以“相对”值展现（在机器学习中要是作为特征，则特别实用）
- `df.resample('5min').first()`：每个5分钟取第一个数据