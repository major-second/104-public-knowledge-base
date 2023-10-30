- 前置
  - [[pandas-index]]
  - [[timestamps]]
# `pd.DatetimeIndex`
```python
df = pd.DataFrame({'a': [10., 20., 30., 40., 50.],
                   'b': [None, None, None, None, 500]},
                  index=pd.DatetimeIndex(['2018-02-27 09:01:00',
                                          '2018-02-27 09:02:00',
                                          '2018-02-27 09:03:00',
                                          '2018-02-27 09:04:00',
                                          '2018-02-27 09:05:00']))
```