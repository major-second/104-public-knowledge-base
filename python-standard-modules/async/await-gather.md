- 前置
  - [[await-expr]]
# Python asyncio.gather() Function
The `asyncio.gather()` function in Python is used to run multiple asynchronous tasks concurrently. When all tasks are completed, it returns a list of results from all the tasks. Here is an example:

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    return 'task1 result'

async def task2():
    await asyncio.sleep(2)
    return 'task2 result'

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

# Python 3.7+
asyncio.run(main()) # I.e. waiting for task1 and task2 to be all completed
```

The `asyncio.gather()` function is similar to the `start` and `join` operations in multiprocessing (refer to [[start-join]]). However, while `start` and `join` are used for running processes concurrently, `asyncio.gather()` is used for running coroutines concurrently. 
- [[process-thread]] vs [[coroutine]]