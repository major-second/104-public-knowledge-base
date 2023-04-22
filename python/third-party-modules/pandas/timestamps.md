- 参考
  - [参考](https://blog.csdn.net/weixin_39532362/article/details/93854780)
  - [参考](https://www.jianshu.com/p/1d66d0e6672a)
- 基础使用（自动推断格式）
  - `pd.to_datetime('2018-01-15 3:45pm')`
  - `pd.to_datetime('7/8/1952')`
  - `pd.to_datetime('7/8/1952', dayfirst=True)`
  - `pd.to_datetime(<大整数>, unit='ns')`
    - `pd.to_datetime(0)`输出`Timestamp('1970-01-01 00:00:00')`
    - 这个大整数[[timestamps]]并不是`20220721093000031`这种本质字符串的东西
  - `pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'])`
    - 返回一个序列`DatetimeIndex`
    - 底层：64-bit的整数（纳秒）
- 加速（手动指定格式）
  - 指定格式如`format='%m/%d/%y'`
    - 注意`%Y`是全称`2022`这种，区别于`%y`
  - 相当于[[general-principles/special-case]]思想：有特例，指定特例，效率高
- [[leaky-abstraction]]
  - ```python
    for i in range(1680, 1670, -1):
        try:
            print(pd.to_datetime(f'{i}/01/01 00:00:00'))
        except:
            print(f'{i}/01/01 is not in the range of pd.to_datetime')
    ```
- 拓展例子
1. 
  - `sr = pd.Series([20220721093000030, 20220721093000031])`
  - `sr = pd.to_datetime(sr.astype(str), format='%Y%m%d%H%M%S%f')`
2. 
  - `df['ExchTime'] = pd.to_datetime(df['ExchTime'], unit='ns')`
  - `df.set_index('ExchTime', inplace=True)`
3. 
  - `time`属性。“日期时间”中的“时间”部分
  - `print(pd.Timestamp('00:00:02').time() == pd.to_datetime(2, unit='s').time())`
  - 也可用来`filter`
  - ```python
    mask = pd.Series(index=df.index).fillna(False)
    for start_time, end_time in TIME_RANGES:
        mask |= (start_time <= df.index.time) & (df.index.time <= end_time)
    df = df.loc[mask]
    ```
  - 应用：过滤某些开盘时间、交易中某些时间段等
# `Timedelta`
- 构造间隔`td = pd.Timedelta(weeks=2,days=10,hours=12,minutes=2.4,seconds=10.3)`
  - 使用：可以直接`date1 = date0 + td`
  - 示例：`2.5 * d1 - 1.5 * d2`报错（时刻不能乘法），但`d1 + 1.5 * (d1 - d2)`可以