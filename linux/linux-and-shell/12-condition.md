[toc]
# 12 使用结构化命令
前置：
- [[11-basic-scripting-partB]]

本篇是[[linux-and-shell/0-metadata]]读书笔记第12章。
我们大致了解 #Linux 的 #shell 脚本的条件结构，方便做自动化提高 #工作效率
## 12.1 使用`if-then`语句
```sh
if command
then
    commands
fi
```
（或者`if command; then`，可少用一行）（否则就必须要换行）
`command`正常以0退出（参考[[11-basic-scripting-partB]]），则执行`then`中的
- 举例：`echo 11 | grep 2; echo $?`，输出1
  - 即`grep`找不到时会是“非正常退出”，返回值非零
- `if-then`常用场景：如果运行环境不是想要的，就`exit`退出该脚本
  - 比如`if echo 11 | grep 2; then echo ok; fi`无输出
  - `if echo 11 | grep 1; then echo ok; fi`有2行输出
  - `if echo 11 | grep 1 > /dev/null; then echo ok; fi`有1行输出
    - 参考[[linux-devices]]
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
elif command
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
  - `=, !=, \>, \<`二元中缀运算符
    - 注意转义[[escape]]`\<`，注意`=`不是`==`
    - 相等的标准：大小写，标点全部相等
    - 排序标准：`sort`和`test`可能标准不同（关于大小写），可能非常tricky
    - 区分`\>`和`-ge`：一个是文本比较，一个是数值比较
    - 有空格的字符串需要双引号 [[shell-quotes#单双引号]]
  - 以及`-n, -z`一元（分别表示“是否长非0，是否长为0”）
    - 可用于确认参数是否存在
- `if test $var1`和`if set | grep var1`的结果未必一样（对于定义了`var1=''`的情形）
- 关于文件
  - `-d`是否存在为目录，`-e`是否存在，`-f`是否存在为文件
    - 拓展：`-L`和[[ln-s]]软链接有关。损坏的软链接不能`-e`
  - 还有些权限相关和二元“新旧”比较等
  - 比如一般用户的`if [ -r /etc/shadow ]`就不为真（但`root`为真，参考[[7-permissions]]）
  - `-G`：注意只看默认组
  - `-nt`：注意需先验证存在。注意相对路径问题
## 12.5 复合条件测试
- `[ <条件1> ] && [ <条件2> ]`：与
- `||`：或
- `if ! [ -d a ]; then echo 2; fi`，`if ! [ 1 -ge 2 ]; then echo 2; fi`：非
- 当然也可以`if ! cd /a`，不用`test`或方括号
  - 如果`cd /a`成功了，那就成功了，不成功就输出错误，很好用
  - 特别常见：`if ! cd $1; then return 1; fi`
## 12.6 `if-then`的高级特性
- 双圆括号：使用更多数学表达式。可以用于赋值，也可用于比较
- 双方括号：例如`[[ r1 == r* ]]`这样的正则表达式

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
每个情况中如果有多行，写法也是类似的，结束时`;;`

```sh
case $var1 in
pattern1 | pattern2) 
commands1
commands11
;;
pattern3) commands3;;
*) commands;;
esac
```