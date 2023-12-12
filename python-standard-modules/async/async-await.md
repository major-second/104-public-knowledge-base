https://www.cnblogs.com/xinghun85/p/9937741.html
async/await is a pattern for asynchronous function scheduling based on [[coroutine]].

The 'async' keyword is used to declare an asynchronous function. The characteristic of an asynchronous function is that it can be suspended during its execution to execute other asynchronous functions. Once the suspension condition (e.g., sleep(5)) is met, i.e., after 5 seconds, it resumes execution. (Compare with [[yield]])

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
```
