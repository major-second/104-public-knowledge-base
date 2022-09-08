## 设置的常见坑
- 凡是软件工作不正常，第一时间想想
  - 做了设置没，设置对不对
  - 软件读取的是哪里的设置
  - 读取设置的格式、解析方法是否正确
- 设置具有优先级
  - 比如工作空间优先于用户级优先于系统级优先于默认
  - 例如[[vscode/settings]]中，打开的文件夹中`.vscode/settings.json`优先于用户级`settings.json`，又优先于默认设置
  - 例如[[config]]中，`git config --local`优先于`git config --global`
- 设置方法是否相同：
  - 比如，对于“代理”这一件事，有些地方用的是环境变量`$http_proxy`，有些地方用的是`gnome`系统设置，有些地方用的是自己的设置
- 格式、解析等：
  - 比如`apt`和`pip`不能正确解析`127.0.0.1:端口号`，但`curl`可以。`apt`需要写`http://127.0.0.1:端口号`（在[[configure]]有提到）
## 常见设置方法
1. 参考[[6-env]]，设置环境变量，乃至把设置环境变量的`export`命令放到`~/.bashrc`或`~/.zshrc`等（使得开终端时自动设置）
2. 编辑特定文件
   1. 比如Linux的`~/.bashrc`，`~/.condarc`，`/etc/ssh/sshd_config`
      1. 参考：[[server-config]]，[[client-config]]，[[software-management/source]]，[[condarc]]
   2. Windows的`known_hosts`
   3. [[vscode/settings]]：`settings.json`文件
   4. 有时还需要结合[[find-grep]]找到到底去哪里设置
      1. 比如franka机器人的`xacro`文件，参考[[franka-panda/limit]]
   5. `.d`的作用
      1. 比如`source.list`和`source.list.d`的关系
      2. 你可以放很多扩展名为`.list`的文件，文件名可以不同，也不一定为`source`，比如`1.list, 2.list, ...`
      3. 把它们放到`/path/to/source.list.d/`目录，相当于`/path/to/source.list`里具有多个文件的内容
      4. 所以直接在`.d`文件夹里加文件，其实等价于编辑某个特定文件，这在[[docker/source]]中有应用：添加到`/etc/apt/apt.conf.d/`中任意一个文件，相当于增加一部分内容到`/etc/apt/apt.conf`
      5. 删除也可以方便地删除一部分，这在[[software-management/source]]中就提到了：当gpg key出问题时，删除对应`.list`和gpg key，不影响其它`.list`
   6. 为了达成同一目的，可能有多个文件，之间可能具有“优先级”而出现一些值的覆盖，参考上一节“优先级”
3. 用命令
   1. 比如`git config`，参考[[config]]
   2. 比如`pip config set <key> <value>`命令，参考[[pip]]
      1. 注：不同版本可能具有的方式还不同。比如老[[version]] `pip`就没有`config`命令。需要装新版本。
   3. 用命令很多时候等价于封装了的方法2（直接编辑文件）
4. 用GUI设置。比如Windows的属性，或者Ubuntu的Settings等
5. 用一些定制好的界面（UI），修改文本文件，比如[[linux-kernel]]里的
   1. 本质上效果就是编辑文本。但是有界面，比较方便安全
6. 有意思的：windows10有Settings和Control Panel共存（历史遗留问题）
   1. 前者更现代，后者功能更强，能变更多细致东西（参考[[leaky-abstraction]]，[[aggregation]]）
## “临时设置”和其作用
主条目[[temp-solution]]