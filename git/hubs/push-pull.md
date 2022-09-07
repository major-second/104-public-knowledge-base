- 前置[[hubs/troubleshooting]]
# 四种push的方法
1. On Github (website), directly click `add a file` and add a file, it will automatically generate command to pull, commit, and push.
2. Download `Github Desktop` and clone a image of your repo to your own host, your changes on your own host will be regarded as `changes`, and you can commit and push them to Github by clicking some buttons.
3. Do the same things as `Github Desktop` on `VSCode`, [reference](https://blog.csdn.net/qq_25367937/article/details/114271010?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2)
4. Use command such as"init","pull","clone","commit -m", and"push", [reference](https://blog.csdn.net/weixin_42449339/article/details/112410926)
# 其它
- 一般来说不要为了看起来舒服就[[reset]]再`push --force`，因为[看起来一堆commit并不占多少空间](https://segmentfault.com/q/1010000003089251)
- `git push --tags`可以让远程能看到tags
- `git push origin <branch_name>`到指定分支
- `git pull`命令变种
  - `--recursive`选项：可递归pull [[submodule]]
  - [pull所有分支](https://blog.csdn.net/wu1169668869/article/details/83345633)
- 如果你有多个分支，那需要指定`git pull origin main`这种，才把本地的`main`也同步到对应`origin/main`的位置