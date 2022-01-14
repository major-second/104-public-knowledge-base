凡是软件工作不正常，第一时间想想：设置对不对。软件读取的是什么设置！
比如，对于“代理”这一件事，有些地方用的是环境变量`$http_proxy`，有些地方用的是`gnome`系统设置，有些地方用的是自己的设置
总结一下常见的设置方法
1. 参考[[6-env]]，设置环境变量，乃至把设置环境变量的`export`命令放到`~/.bashrc`或`~/.zshrc`等，开机启动
2. 编辑特定文件。比如`~/.bashrc`，`~/.condarc`，`/etc/ssh/sshd_config`，Windows的`known_hosts`
   1. `.d`的作用：比如`source.list`和`source.list.d`的关系，你可以放很多扩展名为`.list`的文件，文件名可以不同，也不一定为`source`，比如`1.list, 2.list, ...`，放到`/path/to/source.list.d/`目录，相当于`/path/to/source.list`里具有多个文件的内容
   所以直接在`.d`文件夹里加文件，其实相当于编辑某个特定文件。
3. 用命令。比如`git config`，`pip config set`命令（很多时候等价于封装了的方法2.）
4. 用GUI设置。比如Windows的属性，或者Ubuntu的Settings等