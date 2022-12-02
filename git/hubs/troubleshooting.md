# 数据传输
- `clone, fetch, push, pull`等涉及remote托管平台（即和在线平台进行数据传输），所以有一些和下载、联网有关的问题
- 参考[[https-ssh]]，[[known-hosts]]，[[personal-access-tokens]]，[[settings-and-configurations]]，[[proxy/basics]]等设置代理、ssh、token，排除坑
- 关于代理
  - 如果`git`命令行不能`push pull`（或不稳定），但浏览器可以，可能是命令行没设置代理但浏览器自动走了浏览器代理
  - 参考[[configure]]
  - `OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`或`gnutls_handshake() failed: The TLS connection was non-properly terminated.`：可能是代理[[node]]挂了，需要更换代理[[node]]
# conflict
- 典型场景是你和别人各自改了同一个文件
  - 对方push之后，你也想push
  - 或对方push之后，你想pull
- pull如果因为conflict不能执行，可以参考[[stash]]解决
- 接上，你想push，则典型过程是先pull别人写的代码，人工解决conflict（“保留哪一边的修改”），再push
  - 如果不先pull别人代码，可能的典型报错信息
```text
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to '<某>'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
- 而如果你想直接用别人的，放弃自己的修改
  - 那可以[[fetch]]但不`pull`. 先`git fetch`
  - 然后`git checkout origin/<name>; git branch -D <name>; git branch <name>; git checkout <name>`，参考[[git-basics/branch]]和[[checkout]]
- 关于大文件导致`push`不成功参考[[push-eliminate-big-files]]