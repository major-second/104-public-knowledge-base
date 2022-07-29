算出的东西用完不用删，说不定下次还要用呢？多占空间，节省时间
举例
- [[cache-decorator]]
- python的`lru_cache`装饰器
  - 区别于[[cache-decorator]]，这个是一次运行之内的缓存，不能跨越多次运行
  - 但，如果你的计算不是特别特别久，不建议使用[[cache-decorator]]，否则要不断access硬盘
- [[jupyter-notebook/cache]]