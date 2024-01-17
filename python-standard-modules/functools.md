- 主要用于[[functional-programming]]
- `reduce`：用于[[functional-programming]]的[[map-reduce]]
  - 注：`map`是直接有的，但是`reduce`需要`from functools import reduce`才有
  - 比如`reduce(lambda x,y: x*y, map(int, ['1', '2', 3.4, 4]))`输出`24`
  - 常见错误：`sum`应该输入list而不是两个元素所以要使用`lambda x,y: sum([x,y])`
    ```python
    from functools import reduce
    print(reduce(lambda x,y: sum([x,y]), [1,2]))
    try:
        print(reduce(sum, [1,2]))
    except TypeError as e:
        print(e)
    ```
- `partial`：用于减少函数元数（[[currying]]）
  - `f = lambda x,y:x+y; g = partial(f, x=1); print(g(y=2))`，输出`3`
- `lru_cache`：参考[[general-principles/cache]]，是个装饰器