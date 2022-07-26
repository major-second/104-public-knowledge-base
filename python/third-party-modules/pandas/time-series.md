- 前置
  - [[pandas/installation]]
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
## 进阶
- [参考](https://blog.csdn.net/weixin_42033491/article/details/108104305)