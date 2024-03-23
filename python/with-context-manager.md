- 示例
  - [[pickle]]中用到
  - 一般读写文件`with open('file.txt', 'r') as f: ...`用到
  - [[pytest]]
  - ```python
    >>> with pytest.raises(ZeroDivisionError):
    ...     1 / 0
    ...
    ```
- 比如确保即使中途出错也能关闭文件，释放[[share-lock]]等等
- 代替[[try-except]]结构的`finally`部分
- 可以多个，例如`with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2: ...`
- [参考](https://realpython.com/python-with-statement/)