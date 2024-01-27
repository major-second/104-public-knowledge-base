- 参考
  - [[adapter#deque]]
  - [[data-structure/deque]]
    - 也可实现循环队列
- 相比[[adapter#deque]]，名字？
  - 所有名字加上`left`，比如`popleft`，`appendleft`等，有点野鸡
    - 默认从右边加减元素（`append` / `pop`）
      - 这个相比队列[[queue]]，肯定也不一致！因为正常队列肯定理应右边append左边pop
  - 个人觉得这个不优美在于破坏两边的[[symmetry#翻转]]，认为右天生正宗，左天生是附加
- [代码](python_deque.py)
- 测试代码
  - 自动循环队列
  - ```python
    >>> from collections import deque
    >>> d = deque([], maxlen=3)
    >>> d.append(1)
    >>> d
    deque([1], maxlen=3)
    >>> d.append(2)
    >>> d.append(3)
    >>> d
    deque([1, 2, 3], maxlen=3)
    >>> d.append(4)
    >>> d
    deque([2, 3, 4], maxlen=3)
    >>> d.popleft()
    2
    >>> d.pop()
    4
    >>> d
    deque([3], maxlen=3)
    ```