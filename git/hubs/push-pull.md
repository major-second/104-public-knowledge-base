# 四种push的方法
1. On Github (website), directly click `add a file` and add a file, it will automatically generate command to pull, commit, and push.
2. Download `Github Desktop` and clone a image of your repo to your own host, your changes on your own host will be regarded as `changes`, and you can commit and push them to Github by clicking some buttons.
3. Do the same things as `Github Desktop` on `VSCode`, [reference](https://blog.csdn.net/qq_25367937/article/details/114271010?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2)
4. Use command such as"init","pull","clone","commit -m", and"push", [reference](https://blog.csdn.net/weixin_42449339/article/details/112410926)
# troubleshooting
- push和pull涉及remote托管平台，所以可以参考[[https-ssh]]，[[personal-access-tokens]]，[[settings-and-configurations]]等设置代理、ssh、token，排除坑
- `OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`可能是代理[[node]]挂了，需要更换代理[[node]]
- 没有先pull，可能不给你push
  - 需要先pull别人写的代码，人工解决conflict（参考pull一节），再push
  - 典型报错信息：
```text
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to '<某>'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
- pull如果因为conflict不能执行，可以参考[[stash]]
# 其它
- 一般来说不要为了看起来舒服就[[reset]]再`push --force`，因为[看起来一堆commit并不占多少空间](https://segmentfault.com/q/1010000003089251)
- `git push --tags`可以让远程能看到tags
- `git pull`命令变种
  - `--recursive`选项：递归pull [[submodule]]
  - [pull所有分支](https://blog.csdn.net/wu1169668869/article/details/83345633)