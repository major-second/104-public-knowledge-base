- 前置
  - 常用于[[pd-timestamps]], [[datetime-index]]
  - 防止看到未来信息，[[information-leak]]
- [文档](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.asof.html)

```
>>> df = pd.DataFrame({'a': [10., 20., 30., 40., 50.],
...                    'b': [None, None, None, None, 500]},
...                   index=pd.DatetimeIndex(['2018-02-27 09:01:00',
...                                           '2018-02-27 09:02:00',
...                                           '2018-02-27 09:03:00',
...                                           '2018-02-27 09:04:00',
...                                           '2018-02-27 09:05:00']))
>>> df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
...                           '2018-02-27 09:04:30']))
                      a   b
2018-02-27 09:03:30 NaN NaN
2018-02-27 09:04:30 NaN NaN

>>> df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
...                           '2018-02-27 09:04:30']),
...         subset=['a'])
                        a   b
2018-02-27 09:03:30  30.0 NaN
2018-02-27 09:04:30  40.0 NaN
```
- [merge_asof](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge_asof.html)
  - 注意
    - > direction ‘backward’ (default), ‘forward’, or ‘nearest’ Whether to search for prior, subsequent, or closest matches.
    - 这就是防止[[information-leak]]
  - 使用left的index，且right的时间戳不晚于left