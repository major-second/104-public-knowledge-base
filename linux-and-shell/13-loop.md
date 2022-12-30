---
title: 使用结构化命令
type: operations
---

[toc]
# 13 使用结构化命令
前置：
- [[12-condition]]

本篇是[[linux-and-shell/0-metadata]]读书笔记第13章。
我们大致了解 #Linux 的 #shell 脚本的循环结构，方便做自动化提高 #工作效率
循环结构是最典型的利用脚本做自动化的结构。比如批量重命名，打包解包，调整目录等等
## 13.1 `for`命令
`for`命令和`if`命令对比，体现了shell的丑陋
```sh
if ...
then
    ...
fi
```
```sh
for var in list
do
    ...
done
```
确实是太丑了。`if`和`fi`配对，但`do`和`done`配对……地位完全不对等
- `list`具体可能的定义方式
  - 可以直接`for test in a b c`（注意这里的`test`是被赋值，所以不用加`$`，和`if`中的对比）
    - 注意碰到引号可能要用另一种引号包裹（或者转义）
    - 注意遇到空格需要双引号把一个整体包裹
  - 可以把一个列表存到一个变量里。也可以做列表拼接
    - 例如`list='1 2 3'; for var in $list 4 $list; do echo $(expr $var * 2); done`输出7个数字
    - 例如`list='1 2 3'; for var in $list" 4 "$list; do echo $var; done`却输出5行（注意`"`导致的tokenize结果变化）
  - 可以使用`$()`包裹`cat`或`ls`等输出的结果
    - 注意对于`cat`输出文件中的内容作为表，空格可能导致麻烦
  - 整数：`for i in {1..10}`，左右都包含
```sh
$ cat 1
1 2 3
4

$ for var in `cat 1`; do echo $var; done
1
2
3
4
```
- 临时改变字段分隔符(internal field separator)可以解决上面说的空格导致的麻烦
  - 例如：临时改变`IFS=$'\n'`，就让只有换行导致被识别为新字段。
    - 注：`'\n'`和`"\n"`都是不行的。请仔细区分`''`，`""`，<code>&#96;&#96;</code>，以及`$''`
  - 更改请备份，例如`IFS.OLD=$IFS`. 临时变完之后再变回去
  - 可以考虑不（只）使用空白符号做IFS，而是`:`等等，方便做一些场景数据处理
  - 有趣的是：`echo $IFS`一定输出全空，你需要`echo "$IFS"`做验证！
- 使用通配符的例子：`for file in /home/<用户名>/test/*.a /home/<用户名>/newtest/*.b`（可以“多个”目录通配符）
  - 文件名可以有空格，所以后续处理时需要`"$file"`
- 实用示例：结合[[find-grep]]对所有某类型文件做处理。比如对所有视频统一做某些处理（参考[[ffmpeg]]）
`for CLIP in $(find data/long_term_anticipation/clips_hq -name "*.mp4"); do ffmpeg -y -i $CLIP -c:v libx264 -crf 28 -vf "scale=320:320:force_original_aspect_ratio=increase,pad='iw+mod(iw,2)':'ih+mod(ih,2)'" -an data/long_term_anticipation/clips/$(basename $CLIP); done`
## 13.2 C语言风格的`for`命令
C语言的`for`命令:
```C
for (i = 0; i < 10; i++)
{
  printf("%d\n", i);
}
```
bash中的C语言风格：
```sh
for (( i = 0; i < 10; i++))
do
    echo $i
done
```
两者区别：bash中使用`(())`，且语句体仍是`sh`的`do, done`等
不过可以不遵守之前的一些规定。比如赋值的空格，判断条件中不以`$`开头，算式不用`expr`算式等
- 可以`for ((a=1, b=10; a<=10; a++, b--))`. 总之只有判断条件是只能一个，其余的都可以用逗号连接多个
## 13.3 `while`命令
```sh
while test command
do
  commands
done
```
和`if`类似，看`test command`返回的状态码是否为0
- 注意`test command`区可能多条。且最后失败的那一次也会执行完这多条。这可能导致预料之外结果
- `while [[ 1 -eq 1 ]]; do sleep 1; echo 1; done`：无限循环
## 13.4 `until`命令
把刚刚`while`改成`until`，语义是退出状态码非0就做循环，否则出循环（即：和刚才恰好相反）
## 13.5 嵌套循环
没什么特殊的，只不过混用`until`和`while`有时降低可读性
## 13.6 循环处理文件数据
典型：处理`/etc/passwd`，需要两种IFS，一种是空行，一种是冒号
（逗号分隔符`.csv`文件也类似）
## 13.7 控制循环
`break`跳出最内层循环
`break n`跳出`n`层循环
`continue`略过本次循环之后的动作（小心有没有把增量略过）
`continue n`也可以多层
- 结合`while`无限循环的例子：`while [[ 1 -eq 1 ]]; do sleep 1; date; if date | grep ':.9'; then break; fi; done`
## 13.8 处理循环的输出
把整个循环看成整体，在后面加上重定向
也可以把整个循环的结果管道接给下一个命令（比如`sort`）
## 循环的应用
比如你文件夹下有特别多特别多图片（`.jpg`），直接`rm ./*.jpg`，报错参数过多，你就可以
<code>for file in &#96;ls&#96;; do if &#91;&#91; &#36;file == *jpg &#93;&#93;; then rm &#36;file; fi; done</code>