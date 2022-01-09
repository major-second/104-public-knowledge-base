对于windows10，在`C:\Users\<用户名>\.ssh`下有一个`known_hosts`文件，用记事本可以打开。里面记录的是本地信任的远程主机
当你`ssh`服务器或者`git`上传下载时，都可能需要更新这个
- 例如`ssh -T git@github.com`，使得`git`可以上传下载
- 例如第一次`ssh`某个服务器时有一个警告，说你添加了新的主机到`known_hosts`
- 例如远程 #docker 镜像`rm`掉重新建之后，你需要删除`known_hosts`的对应行，否则会不给你连