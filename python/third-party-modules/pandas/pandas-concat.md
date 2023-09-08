- 前置
  - [[series-dataframe]]
- 可以看[[pandas-cheatsheet]]
    ```python
    import pandas as pd
    df1 = pd.DataFrame({'x': [1,2], 'y': [3,4]}, index=[1,3])
    df2 = pd.DataFrame({'x': [5,6], 'y': [7,8]}, index=[2,4])
    print(pd.concat([df1, df2]))
    print(pd.concat([df1, df2], axis=1))
    ```