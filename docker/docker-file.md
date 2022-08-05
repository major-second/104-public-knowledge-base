基础：https://zhuanlan.zhihu.com/p/114033550
使用环境变量和参数
- https://www.jianshu.com/p/ae634ffb21ff
- 并参考[[docker/env-var]]
## `SHELL`命令
用于改变`RUN`用的是什么SHELL，以及是否`--login`
其中使用`SHELL ["/bin/bash", "--login", "-c"]`前
参考
https://blog.csdn.net/stupidNameLimit/article/details/89331694
需要加入
`RUN sed -i -e 's/mesg n .*true/tty -s \&\& mesg n/g' ~/.profile`
来忽略一个tricky错误
## 转义
用`# escape=`指定转义字符
如果转义造成麻烦，可以索性写个小文件，然后`cat 文件名 >> 文件名`解决
## troubleshooting
- 出现交互式时区设置？如何使得其[[silent]]？
Dockerfile加上
```docker
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
```
## `COPY`命令
复制文件。典型用途
1. 前面说过了，有时转义烦了，不如直接拷文件
2. 保持文件[[7-permissions]]，例如[[ssh]]需要`600`权限
3. 在文件有多行时，直接`VAR=$(cat ...)`，再传给[[docker/env-var]]会导致不再是多行，此时复制文件靠谱！