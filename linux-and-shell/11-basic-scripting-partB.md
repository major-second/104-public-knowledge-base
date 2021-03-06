---
title: 构建基本脚本（下）
type: operations
---

[toc]
# 11 构建基本脚本（下）
前置：
- [[11-basic-scripting-partA]]

本篇是[[linux-and-shell/0-metadata]]读书笔记第11章下半部分。
我们大致了解 #Linux 的 #shell 脚本的编写方式，方便做自动化提高 #工作效率
本篇包括管道记号`|`，数学运算，退出脚本
## 11.6 管道记号
管道记号：一个命令的输出直接作为下一个命令的输入，不需要缓冲区或者文件啥的
例如：
- `set | sort | more`（连续使用2次），表示把`set`的结果排序，并且显示时不一次显示完，而是按回车可以往下走那样
- `set | sort > <文件>`：先管道再重定向，写给文件
- 实用应用：
  - `ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`
  - `python_pid=$(ps -ef | grep 'python' | grep -v grep | awk '{print $2}')`
  - `find . -type f -print0 | sort -z | xargs -0 md5sum | md5sum`，参考[[md5sum]]
## 11.7 执行数学运算
### `expr`整数运算
- `expr 2 \* 3`：注意转义和空格
- 也有一些前缀表达式，例如`expr index aaba b`这样（找**字符**，不是子串）
- `expr index + index d`（把关键字解释成字符串）
- `var1=$(expr 2 + 3)`：赋值（需要`$()`包裹）
- 上面的是Bourne Shell历史遗留，未必方便。
  - 方便的：`var1=$[3 * 4]; var2=$[$var1 * 5]; echo $[$var2 * 6]`输出`360`
### 利用交互式解释器做浮点运算
- `bc`，然后尝试（逐行）输入
```bc
scale=3
3.44 / 5
```
- 再例如`python3`（需要已安装`python3`，且版本高于3.6），然后尝试（逐行）输入
```python
x = 1
y = 0.8
z = x/y
print(f'z = {z:.1f}') # 1位小数
```
- 一般解释器中的`Ctrl + C`是停止，`Ctrl + D`才是退出（或者`python3`的`exit()`，`bc`的`quit`）这种
- 利用`echo`和管道，可以使用解释器`bc`解释指定命令。例如
  - `echo 1 + 1 | bc`输出`2`
  - `echo "scale=1; 1.1/1.2" | bc`输出`.9`
- 注意“输入”和“参数”是不一样的。`echo 1 | bc`不等价于`bc 1`
- 内联输入重定向适合`bc`解释连续多行
  - 注意这些命名是在局部的
## 11.8 退出脚本
`$?`：最后一条指令的退出状态码
比如`0`正常，`127`没找到命令，`130`通过`Ctrl+C`终止，等
`exit <自定义退出码>`：以指定退出码立即退出脚本（注意超过255会溢出）