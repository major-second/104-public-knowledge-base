- [[queue]]
  - 原生list无法实现头部$O(1)$插入删除，需要用到这里的`Queue`（也就是FIFO，狭义的队列）
- [参考](https://docs.python.org/3/library/queue.html)
- `queue.Queue(), queue.LifoQueue(), queue.PriorityQueue(), queue.SimpleQueue()`

```python
>>> from queue import Queue  
>>> q = Queue()
>>> q.put(1)
>>> q.get()
1
>>> q.empty()
True
```