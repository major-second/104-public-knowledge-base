- [参考文档](https://docs.python.org/zh-cn/3.9/library/multiprocessing.html)
- 进程相比“线程”，能充分利用多核！
## 最小唯象例子（利用`Pool`并行）
- 参考`minimum.py`
  - 这就说明可以简单做并行
  - 典型输出
```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
1.602008581161499
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
0.5942842960357666
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
2.041583776473999
```
- 注
  - 参考[[availability]]，由于不能pickle太复杂的东西，所以这里的`f`不能用`lambda`定义
  - 不能不写`if __name__ == "__main__":`这行“保护”，否则多进程时会“导入模块”，引发副作用，导致`Runtime Error`，参考[文档](https://docs.python.org/3.9/library/multiprocessing.html#multiprocessing-programming)
- 如果你使用[[launch]]，打个断点可以看到`Pool(5)`后左侧[[call-stack]]就出现5个进程及相应进程号
  - 如果在`if __name__`一句打断点，则可以进入子进程的[[call-stack]]如图
  - ![](subprocess-call-stack.png)
  - 即
    - 可看到`exec(code, run_globals)`这句，从而说明`minimum.py`在让子进程运行自己
    - 可以看到这时`__name__`是`__mp_main__`了
    - 参考`minimum_name_mp_main.py`更加明确`if __name__`一句的作用
- 可以用`os.getpid()`和`os.getppid()`得到进程号/父进程号