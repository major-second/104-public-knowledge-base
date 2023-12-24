---
title: 理解Linux文件权限
type: operations
---

[toc]
# 7 理解Linux文件权限
前置：
- Linux系统

本篇是[[linux-and-shell/0-metadata]]读书笔记第7章部分。
我们大致了解 #Linux 的 #权限 系统。避免权限不够无法运行程序/写入下载数据，或者权限太强导致私钥用不了等问题
## 7.1 Linux的安全性
- `cat /etc/passwd`
的结果：
登录用户名:用户密码（用占位符`x`表示）:UID:GID:备注:`home`目录位置:默认shell
典型：
`root:x:0:0:root:/root:/bin/bash`
- **7.1.3 添加新用户**处值得注意的
	- `HOME=/home`会导致`~`表示的是`/home/<name>`
	- `/etc/skel`里的东西会被复制（比如典型的`~/.bashrc`）
	- `useradd`如果不跟“用户名”参数，而是`useradd -D -s /bin/tsch`这样，就会用于改变（之后新增用户时的）默认值，而不是创建一个具体的新用户
这可以方便之后创建用户
	- 当然`useradd -D`是查看当前的默认值
	- [参考](https://blog.csdn.net/qq_42341984/article/details/120949451#:~:text=%E5%88%9B%E5%BB%BA%E6%96%B0%E7%94%A8%E6%88%B7%E5%B9%B6%E6%B7%BB%E5%8A%A0sudo%E6%9D%83%E9%99%90%201%201%20%E5%88%9B%E5%BB%BA%E6%96%B0%E7%94%A8%E6%88%B7%20%E4%B8%80%E9%94%AE%E6%B7%BB%E5%8A%A0%20useradd%20-d%20%2Fdata%2Fuser%2Fgyb,this%20file.%20...%203%203%20%E5%88%A0%E9%99%A4%E7%94%A8%E6%88%B7%20linux%E5%9F%BA%E7%A1%80%E5%91%BD%E4%BB%A4%E2%80%93userdel%20%E5%88%A0%E9%99%A4%E7%94%A8%E6%88%B7%E5%B8%90%E6%88%B7%E5%92%8C%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6)
- 删除用户可能有残留（即使`-r`）
### 实践
我们记住`cat /etc/passwd`的最后一行
并参考https://help.ubuntu.com/community/TransmissionHowTo
安装`transmission`
`add-apt-repository ppa:transmissionbt/ppa`
`apt update`
`apt install transmission-gtk transmission-cli transmission-common transmission-daemon
`
再次`cat /etc/passwd`，发现最后一行是新增的一个系统账户，名为`debian-transmission`
## 7.2 使用Linux组
- Ubuntu默认一个用户一个同名的组。可以`cat /etc/group`和`grep <name> /etc/group`进行确认
- 有些组没有列出用户，是因为`/etc/passwd`里已经指定了默认组，`/etc/group`就不写
- 增加到组后需要重新登录
- 一个用户可以属于多个组，一个组可以有多个用户
	- 某种程度上，“标签”也许比“组”贴切
	- 但话说回来，用户有唯一的“默认组”。默认组有特殊之处，比如不写在`/etc/group`，比如和`usermod -g`参数有关，比如创建新文件时和属组有关，等。
## 7.3 理解文件权限
用八进制表示权限。比如`777`表示所有人可以做所有操作
`umask`是掩码。从全权限减去它（的后三位）之后才是创建新文件的默认权限
注：这个说“减”并不妥当。这里只是粗略说法。可以`umask 011`试试什么效果
### 实践
`ls -l /dev/null`，空设备，输出结果是`crw-rw-rw-`，即类型是字符型设备，只能读写，不能运行
对于挂载了的硬盘，尝试`ls -l /mnt/data_disk01 # 这是我指定的挂载目录`，有可能的输出结果是`drwx------ root root`，即类型是目录，且只有属主`root`可以读写运行
因此如果你让`transmission`默认下载到这里，因为`transmission`用的是`debian-transmission`用户，故可能观察到现象
- `transmission`下载会报错权限不够
- 但是`root`自己手动创建文件，或者`root`用`wget`，就权限够
## 7.4 改变安全性设置
`chmod 777`这种直接改
`chmod a+x`这种“增量”修改。可以对`u`用户，`g`组，`o`其它，`a`所有
`ls -lF`：显示结果中，对有执行权限的加星号
`chmod -R`：递归地作用
`chmod`也可以使用通配符一次作用多个文件
`chown <属主>.<属组>`，注意`<属主>.`是特殊用法，在用户名有默认的匹配的组名时非常好用
### 实践
- 一般来说，`mkdir /aaa`不行，需要`sudo mkdir /aaa`
  - 但此时如果不`sudo chmod 777 -R /aaa`，那之后别人又不能在里面创建
- 在一个一般的地方（比如普通用户的`~`），`sudo mkdir test`，那之后那个普通用户也不能在里面创建东西
## 7.5 共享文件
- 为了某目录中新建文件以目录的属组（而不是创建者的默认组）为属组，需要设置SGID位
- SUID的典型例子：`ls -l /usr/bin/passwd`. 可以看到其`-rwsr-xr-x root root`，`s`表示其它用户调用这个程序时“临时获得”`root`的权限，以便修改密码。
- SBIT（黏着位）其实和前两个关系不大
## 总结与问答练习
0. Q: 俗话说的好：[[CRUD]]。那么怎么增删改查用户呢？
A: `cat /etc/...`（7.1.1和7.1.2）相当于查（在这里改太危险了）
`useradd`是增，`userdel`是删
`usermod`、`passwd`等几个命令（在7.1.5）是改
1. Q: 用户组的增删改查和用户的有何异同？
A: 不要直接通过修改`/etc/group`文件添加用户到一个组（注：你可以认为向组添加用户属于**用户的改**，而不是**用户组的改**。需要`usermod -G`）
其实常见的要修改的组信息很少，也就是GID或组名。安全权限基于GID
删除组并不是特别常见，书中没有写出（请特别小心）。是用`groupdel`命令
2. Q: 做一个实验，说明书中省略的SBIT位的作用
A:
> In computing, the sticky bit is a user ownership access right flag that can be assigned to files and directories on Unix-like systems.
There are **two definitions**: one for files, one for directories.
For files, particularly executables, superuser could tag these as to be **retained in main memory**, even when their need ends, to minimize swapping that would occur when another need arises, and the file now has to be reloaded from relatively slow secondary memory. This function has become **obsolete** due to swapping optimization.
For directories, when a directory's sticky bit is set, the filesystem treats the files in such directories in a special way so only the file's owner, the directory's owner, or root user can rename or delete the file. Without the sticky bit set, any user with write and execute permissions for the directory can rename or delete contained files, regardless of the file's owner. Typically this is set on the /tmp directory to prevent ordinary users from deleting or moving other users' files. (wikipedia)

所以我们只关注第二种用途
初始是一个一般用户（不是`root`）。执行命令
`sudo mkdir a && sudo chmod +t a && sudo ls -l`
可以看到`a`具有`t`标记
`cd a && touch hello # 没有权限`
`sudo touch hello`
`ls`
`rm hello # 无法删除`
`ls`
`sudo rm hello`
`ls`
`cd .. && sudo rm -rf ./a`
`ls`
3. Q: 天天权限不够，那权限是越高越好吗？
A: 不是。首先会导致危险，其次[[private-key-permissions]]和[[dot-ssh]]都提到了有时系统会强制让太高权限的用不了
## setfacl
- 例子
  - `sudo mkdir /home/shared_a_b && sudo setfacl -m u:a:rwx /home/shared_a_b && sudo setfacl -m u:b:rwx /home/shared_a_b && sudo setfacl -m o::--- /home/shared_a_b`
- `-R`递归
- 注：出现[[ln-s]]时可能有坑：[[ln-s]]的源处绝对路径每一层都要有权限！
## getfacl
- 直接用，`getfacl <...>`