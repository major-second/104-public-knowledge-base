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
用`# escape=`指定转义[[escape]]字符
如果转义造成麻烦，可以索性写个小文件，然后`cat 文件名 >> 文件名`解决
## troubleshooting
- 出现交互式时区设置？如何使得其[[silent]]？
Dockerfile加上
```docker
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
```
## `COPY`命令
- 简述：复制文件（从主机目录到image中目录）
- 典型用途
1. 前面说过了，有时转义烦了，不如直接拷文件
2. 保持文件[[7-permissions]]，例如[[ssh]]需要`600`权限
3. 在文件有多行时，直接`VAR=$(cat ...)`，再传给[[docker/env-var]]会导致不再是多行，此时复制文件靠谱！
- 关于用法：重点注意是否以斜杠结尾
1. `COPY a/ /b/`，来源是`a`目录下所有文件，拷到容器中`/b`目录下。此时`a/`下有`c`文件则容器中出现`/b/c`，而不是`/b/a/c`
2. `COPY a /b`，把`a`拷贝成为`/b`文件，而不是`/b/a`
3. `COPY a a2 /b/`，把`a`和`a2`都拷到`/b/`目录（因为多于一个文件，所以`/b/`后面斜杠不写就不允许了）