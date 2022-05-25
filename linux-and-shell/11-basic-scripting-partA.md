---
title: 构建基本脚本（上）
type: operations
---

[toc]
# 11 构建基本脚本（上）
前置：
- [[6-env]]
- [[7-permissions]]
- [[10-editting]]

本篇是[[linux-and-shell/0-metadata]]读书笔记第11章上半部分。
我们大致了解 #Linux 的 #shell 脚本的编写方式，方便做自动化提高 #工作效率
本篇包括基本的脚本文件编写知识（例如变量、三种引号、重定向等）
## 11.1 使用多个命令
简单的顺序结构（连续使用多个命令）：`<命令>; <命令>`
一行不能超过255个字符
如果要换行：比如这个片段
```sh
echo "
channels:
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/peterjc123/
custom_channels:
 pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
" >> ~/.condarc; \
apt update; \
apt-get install -y vim curl openssh-server \
ffmpeg;
```
可以看到一些典型的换行的使用方式
- 引号未配对，则会等待配对
- `; \`表示命令写完了，换行，下一条命令
- `\`表示命令没写完。这样可以写一行特别长的命令。比如`apt-get install <一大堆包名>`
- `; \`和` && \`的区别（todo）

这样的“连续使用命令”可以直接粘贴到终端，回车执行。效果类似这样
![](11/multiple-cmd.png)
就不需要创建`.sh`文件再执行
==一个坑==：
```sh
echo 1; \ # echo 1
echo 2
```
这样是不行的（即：注释只能写在最后一行，不能写在中间）
- 为什么需要`; \`：你**在`sudo ls`能提示你输入密码时，也就是最近一小段时间没有输入过密码时**直接复制

```bash
echo 1
sudo ls
<你的密码>
echo 3
```
并粘贴到`bash`，就发现问题了（[[zsh]]行为不一样）
总之直接回车的多行不一定会被按顺序当作命令依次执行
## 11.2 创建shell脚本文件
用[[10-editting]]创建文本文件，将命令（逐行）输入到文件中
第一行`#!`指定要使用的shell，而其它`#`用于注释
写好`.sh`脚本文件，怎么运行？`./<.sh文件名>`表示当前目录下的（一般这么用）。不想加`./`，想直接文件名运行的话，就需要设定`PATH`环境变量
为了可以运行，还需要参考[[7-permissions]]加权限（当然如果确定使用的是bash，也可以直接`bash <文件名>.sh`）
## 11.3 显示消息
- 一般字符串直接`echo`
- 引号相关初步
  - 只有一种引号（比如单引号）就用另一种括起来（比如双引号）
    - 例如[[wc]]中的`find . -type f -name "*.mp4" | wc`如果需要`watch`（每两秒看一次），那就用单引号，即`watch 'find . -type f -name "*.mp4" | wc'`
  - 若末尾需要空格，那也需要引号括起来，例如[[sudo]]有应用这种引号
- `-n`参数可以不换行
  - 应用：`echo -n 'date: '; date`
## 11.4 使用变量
- `set`：显示所有环境变量（参考[[6-env]]）
- `$<变量名>`：使用变量（可以是环境变量）
  - `${<变量名>}`很常见，更明显标出变量名
- 双引号中的`$`仍表示变量。`\$`才是原始的符号`$`
  - 单引号中的`$`就是原始符号
- 区分大小写，数字字母下划线组成，长度不超过20
- 自己的变量？
  - 定义变量不需要`$`（取用需要）
    - 例如`y=$x`
  - 等号赋值
  - 等号前后无空格
  - 脚本运行结束时自动删除
### 11.4.3 命令替换
- <code>&#96;&#96;</code>包裹，或是`$()`包裹，都可以把命令的结果当成字符串，赋值给变量。典型：<code>testing=&#96;date&#96;</code>
- `date +%y%m%d`这样可以指定日期格式
- “子shell（subshell）”不能用外层名字空间的变量名问题
  - 比如`x=1; echo $x`，能输出1，但下面的两个例子中
```sh
x=1; \
echo "echo $x" > ./a.sh; \
chmod a+x ./a.sh; \
./a.sh; \
rm ./a.sh
```
上面这个能输出`1`（注意双引号）
```sh
x=1; \
echo 'echo $x' > ./a.sh; \
chmod a+x ./a.sh; \
./a.sh; \
rm ./a.sh
```
这个不能
## 11.5 重定向输入和输出
- `>`：重定向到文件（没有则新建，有则覆盖所有内容）
- `>>`：追加（没有则新建）
- `<`：读入文件内容（重定向输入）。例如`wc`计数
- `<<`：内联输入重定向
- 例如**手动逐行输入**下面几行（不要直接粘贴）
```sh
wc << EOF
  11
  22
  33
  EO
  EOF
# 本来wc是用来统计文件的。可以自己试试
```
结果是`4 4 12`
`EOF`可以是任何你想要的字符串
注意输完第一行后，后面的提示符改成了“次提示符”，例如`$`变成了`>`
- 例如`cat > file.txt << EOF`
## 转义专题
https://www.cnblogs.com/loki717/p/7358125.html
> 在双引号内，不被忽略的符号：` $ \

应用：[[ssh-env-var]]中需要往文件输入
```sh
for item in `cat /proc/1/environ | tr '\0' '\n'`
do
 export $item
done
```
那么你可以
```sh
echo "for item in \`cat /proc/1/environ | tr '\\0' '\\n'\`
do
 export \$item
done" >> /etc/profile
```