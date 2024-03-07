- [[meta-programming]]
  - 联系[[pandas-query]]也是
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html
- 完整文档，哪些操作可以用
  - https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-query
- 用不了的
  - `max, min`
- 可以用的
  - `|`, `&`, `~`（与、或、非）
- `df.loc[df.eval('A + B == C')]`
  - 不要`df.loc['A + B == C']`
- `df = df.eval('C = A + B')`
  - 不要`df.eval('C = A + B')`
    - 这是[[inplace]]问题
-   ```
    df = df.eval(
        '''
    C = A + B
    D = A - B
    '''
    )
    ```
- 部分缓解[[meta-programming]]的坏处（容易出错），兼具方便和实用的写法：
  - `df.eval(f'{col} = {col} + 1')`
  - [[f-string]]