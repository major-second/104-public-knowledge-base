- 前置
  - [[11-basic-scripting-partB#数学运算基础]]
  - [[python]]
  - [[float]]
- `bc`
  - 尝试（逐行）输入
    ```bc
    scale=3
    3.44 / 5
    ```
  - 利用`echo`和管道，可以使用解释器`bc`解释指定命令。例如
    - `echo 1 + 1 | bc`输出`2`
    - `echo "scale=1; 1.1/1.2" | bc`输出`.9`
  - 注意“输入”和“参数”是不一样的。`echo 1 | bc`不等价于`bc 1`
  - 内联输入重定向适合`bc`解释连续多行
    - 注意这些命名是在局部的
  - 参考例子
    - `curr_limit_memory=$(echo "$curr_limit_memory_ratio * $available_memory * 1000" | bc)`
- 再例如`python3`
  - 以下需要已安装`python3`，且版本高于3.6
  - 然后尝试（逐行）输入
    ```python
    x = 1
    y = 0.8
    z = x/y
    print(f'z = {z:.1f}') # 1位小数
    ```
- 一般解释器中的`Ctrl + C`是停止，`Ctrl + D`才是退出
  - 或者`python3`的`exit()`，`bc`的`quit`