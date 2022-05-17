`torch.utils.file_baton`，去里面可以看具体是干嘛。
大致是通过管理一个文件（作为“锁”[[lock]]），让一些操作不同时进行引起混乱
可能引起问题：锁残留没被删，导致之后运行时无限循环卡住。这种问题的反映：`Ctrl+C`停止，看到Trace中有这种字样
```python
  File "<路径>/torch/utils/file_baton.py", line 42, in wait
    time.sleep(self.wait_seconds)
```
解决方法：在卡住的行（`time.sleep`）打断点，用[[debug-console]]`print`出锁文件的路径，手动删除