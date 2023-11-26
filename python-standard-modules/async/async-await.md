# Python async/await Keywords
https://www.cnblogs.com/xinghun85/p/9937741.html
async/await is a pattern for asynchronous function scheduling based on [[coroutine]].

The 'async' keyword is used to declare an asynchronous function. The characteristic of an asynchronous function is that it can be suspended during its execution to execute other asynchronous functions. Once the suspension condition (e.g., sleep(5)) is met, i.e., after 5 seconds, it resumes execution. (Compare with [[yield]])

Here is an example:
```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
```

The 'await' keyword is used to declare program suspension. For instance, if an asynchronous program needs to wait for a long time at a certain step, it will be suspended to execute other asynchronous programs.
'await' can only follow an asynchronous program (i.e., a program declared with 'async') or an object with an __await__ attribute. Suppose there are two asynchronous functions, async a and async b. If there is an 'await' in a certain step of a, when the program encounters the keyword 'await b()', the asynchronous program is suspended and another asynchronous program b is executed. This means jumping out from within the function to execute other functions. When the suspension condition disappears, regardless of whether b has finished executing, it must immediately jump out from b and return to the original program to execute the original operation.
(Therefore, in order to be able to suspend b, b must be an asynchronous program!)
Here is an example:
```python
import asyncio

async def a():
    print('Start a ...')
    await b()
    print('... End a!')

async def b():
    print('Start b ...')
    await asyncio.sleep(1)
    print('... End b!')

# Python 3.7+
asyncio.run(a())
```
