凡是软件工作不正常，第一时间想想：设置对不对。软件读取的是什么设置，读取设置的格式、解析方法是否相同！
- 比如，对于“代理”这一件事，有些地方用的是环境变量`$http_proxy`，有些地方用的是`gnome`系统设置，有些地方用的是自己的设置
- 比如`apt`和`pip`不能正确解析`127.0.0.1:端口号`，但`curl`可以。`apt`需要写`http://127.0.0.1:端口号`（在[[configure]]有提到）
## 总结一下常见的设置方法
1. 参考[[6-env]]，设置环境变量，乃至把设置环境变量的`export`命令放到`~/.bashrc`或`~/.zshrc`等（使得开终端时自动设置）
2. 编辑特定文件。比如`~/.bashrc`，`~/.condarc`，`/etc/ssh/sshd_config`，Windows的`known_hosts`
   1. `.d`的作用：比如`source.list`和`source.list.d`的关系，你可以放很多扩展名为`.list`的文件，文件名可以不同，也不一定为`source`，比如`1.list, 2.list, ...`，放到`/path/to/source.list.d/`目录，相当于`/path/to/source.list`里具有多个文件的内容
   所以直接在`.d`文件夹里加文件，其实相当于编辑某个特定文件。
3. 用命令。比如`git config`，参考[[config]]，`pip config set <key> <value>`命令（很多时候等价于封装了的方法2.）
   1. 注：不同版本可能具有的方式还不同。比如老版本`pip`就没有`config`命令。需要装新版本。
4. 用GUI设置。比如Windows的属性，或者Ubuntu的Settings等
5. 用一些界面，设置文本文件，比如[[linux-kernel]]里的。本质上效果就是编辑文本。但是有界面，比较方便安全
## “临时设置”和其作用
主条目[[temp-solution]]