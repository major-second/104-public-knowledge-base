基础：https://zhuanlan.zhihu.com/p/114033550
使用环境变量和参数：https://www.jianshu.com/p/ae634ffb21ff
## `SHELL`命令
用于改变`RUN`用的是什么SHELL，以及是否`--login`
其中使用`SHELL ["/bin/bash", "--login", "-c"]`前
参考
https://blog.csdn.net/stupidNameLimit/article/details/89331694
需要加入
`RUN sed -i -e 's/mesg n .*true/tty -s \&\& mesg n/g' ~/.profile`
来忽略一个tricky错误