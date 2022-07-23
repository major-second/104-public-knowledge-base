# 四种push的方法
1. On Github (website), directly click `add a file` and add a file, it will automatically generate command to pull, commit, and push.
2. Download `Github Desktop` and clone a image of your repo to your own host, your changes on your own host will be regarded as `changes`, and you can commit and push them to Github by clicking some buttons.
3. Do the same things as `Github Desktop` on `VSCode`, [reference](https://blog.csdn.net/qq_25367937/article/details/114271010?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2)
4. Use command such as"init","pull","clone","commit -m", and"push", [reference](https://blog.csdn.net/weixin_42449339/article/details/112410926)
# troubleshooting
- push和pull涉及remote托管平台（即和在线平台进行数据上传下载），所以有一些和下载、联网有关的问题
  - 可以参考[[https-ssh]]，[[personal-access-tokens]]，[[settings-and-configurations]]等设置代理、ssh、token，排除坑
  - 注：如果`git`命令行不能`push pull`（或不稳定），但浏览器可以，可能是CLI没设置代理但浏览器自动走了浏览器代理
    - 参考[[configure]]
  - `OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`可能是代理[[node]]挂了，需要更换代理[[node]]
- `clone`，[[fetch]]等需要下载，很多时候和`pull`共享一些相同的trouble
  - 也有一些自己的技巧
  - 例如`git clone --depth=1`可以避免`clone`全部历史
  - 例如[[fetch]]的断点续传
- 关于conflict
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
- 关于大文件导致`push`不成功参考[[push-eliminate-big-files]]
# 其它
- 一般来说不要为了看起来舒服就[[reset]]再`push --force`，因为[看起来一堆commit并不占多少空间](https://segmentfault.com/q/1010000003089251)
- `git push --tags`可以让远程能看到tags
- `git pull`命令变种
  - `--recursive`选项：递归pull [[submodule]]
  - [pull所有分支](https://blog.csdn.net/wu1169668869/article/details/83345633)