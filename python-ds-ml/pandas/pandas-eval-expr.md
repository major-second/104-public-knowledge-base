- [[meta-programming]]
  - 联系[[pandas-query]]也是
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html
- `df.eval('A + B')`
- `df.eval('C = A + B')`
-   ```
    df.eval(
        '''
    C = A + B
    D = A - B
    '''
    )
    ```