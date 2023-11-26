- 前置 [[async-await]]
  - The 'await' keyword can also be used as an expression. This is useful when you want to use the result of an asynchronous function in your code. Here is an example:
    ```python
    async def calc():
        return 5 + 5

    async def main():
        result = await calc()
        print(result)

    # Python 3.7+
    asyncio.run(main())
    ```
  - "promise" to get an result