`git checkout <可选参数>`
- 其后紧跟的参数可能加tag, branch或者哈希值（可以只输入开头几位）等等
- 作用是切换版本到指定标记版本
  - 如果checkout [[git-basics/branch]]名，将check到本地的相应branch
  - 和`git pull`有区别
  - 注意：你本地是`a`分支，想切换成远程的`origin/b`分支，应该先本地`git checkout b`再`git pull origin b`，否则就是想拿远程`origin/b`更新`a`，往往造成conflict等
- 也可以用于检查版本

注意你可能需要[[stash]]之后才能顺利进行操作
checkout的原理参考[[hidden-files]]（把一些隐藏文件拿出来！）
[[detached]]时的checkout可能导致数据丢失