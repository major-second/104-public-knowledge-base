---
title: 使用结构化命令
type: operations
---

[toc]
# 12 使用结构化命令
前置：
- [[11-basic-scripting-partB]]

本篇是[[0-metadata]]读书笔记第12章。
我们大致了解 #Linux 的 #shell 脚本的条件结构，方便做自动化提高 #工作效率
## 12.1 使用`if-then`语句
```sh
if command
then
    commands
fi
```
（或者`if command; then`，可少用一行）
`command`正常以0退出（参考[[11-basic-scripting-partB]]），则执行`then`中的
- 举例：`echo 11 | grep 2; echo $?`，输出1. 即`grep`找不到会“非正常退出”
## 12.2 `if-then-else`语句
只需
```sh
if command
then
    commands
else
    commands
fi
```
即可
## 12.3 嵌套`if`
可以在语句块中嵌套使用`if`，也不妨`elif`
例如
```sh
if command
then
    commands
elif commend
then
    commands
else
    commands
fi
```
## 12.4 `test`命令
把`if`改成`if test`，就可以根据表达式的值控制（也就是把表达式“转化成”对应的`test`命令了）
- `if test <变量名>`（需要加`$`），存在且非空则“真”
- `if test n1 -eq n2`：中缀表达式，判断数值关系
- `if [ n1 -eq n2 ]`：更方便（注意`[`右侧和`]`左侧空格）
- 浮点数比较？不支持！
- 字符串：
  - `=, !=, \>, \<`二元中缀运算符（注意转义）
    - 相等的标准：大小写，标点全部相等
    - 排序标准：`sort`和`test`可能标准不同（关于大小写），可能非常tricky
    - 区分`\>`和`-ge`：一个是文本比较，一个是数值比较
  - 以及`-n, -z`一元（分别表示“是否长非0，是否长为0”）
- `if test $var1`和`if set | grep var1`的结果未必一样（对于定义了`var1=''`的情形）
- 关于文件：常用的：`-d`是否存在为目录，`-e`是否存在，`-f`是否存在为文件。还有些权限相关和二元“新旧”比较等
  - 比如一般用户的`if [ -r /etc/shadow ]`就不为真（但`root`为真，参考[[7-permissions]]）
  - `-G`：注意只看默认组
  - `-nt`：注意需先验证存在。注意相对路径问题
## 12.5 复合条件测试
`[ <条件1> ] && [ <条件2> ]`（逻辑与）
（以及`||`：或）
## 12.6 `if-then`的高级特性
- 双圆括号：使用更多数学表达式。可以用于赋值，也可用于比较
- 双方括号：例如`[[ r1 == r*]]`这样的正则表达式

不同shell间有 #差异化 ，不是所有shell都支持和bash相同的特性
## 12.7 `case`命令
不能说有点丑，只能说非常丑
```sh
case $var1 in
pattern1 | pattern2) commands1;;
pattern3) commands3;;
*) commands;;
esac
```
什么`)`，`;;`，`esac`，丑爆了