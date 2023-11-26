- 前置[[file-handler]]
- [参考](https://zhuanlan.zhihu.com/p/139842746)
- 按行
  - ```python
    with open(fname) as file:
        for line in file:
            ...
    ```
- 无换行符，按一定块
  - ```python
    with open(fname) as fp:
        while True:
            chunk = fp.read(block_size)
            # 当文件没有更多内容时，read 调用将会返回空字符串 ''
            if not chunk:
                break
    ```