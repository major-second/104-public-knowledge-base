- 前置[[hubs/troubleshooting]]
# 四种push的方法
1. On Github (website), directly click `add a file` and add a file, it will automatically generate command to pull, commit, and push.
2. Download `Github Desktop` and clone a image of your repo to your own host, your changes on your own host will be regarded as `changes`, and you can commit and push them to Github by clicking some buttons.
   1. 这类是属于github提供的客户端，倒不是git本身的东西
   2. hhhh，甚至手机还有github app，可以出门应急呢。可能用到[[android]]代理之类的
3. Do the same things as `Github Desktop` on `VSCode`, [reference](https://blog.csdn.net/qq_25367937/article/details/114271010?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2)
4. Use command such as"init","pull","clone","commit -m", and"push", [reference](https://blog.csdn.net/weixin_42449339/article/details/112410926)
   1. 也可以先[[init]], [[commit]]，先没有任何remote，之后再加，参考[[remote]]
   2. 这里特别注意是否加`-u`或`--set-upstream`，参考[[remote]]
# 其它
- [[reset]]再`push --force`
  - 可以减少显示的[[commit]]的数量
  - 一般来说不要为了看起来舒服就这么做
    - 因为[看起来一堆commit并不占多少空间](https://segmentfault.com/q/1010000003089251)
  - 因为有不良后果：别人[[push-pull]]时如果没有对此做心理准备，就会结果不正常，不在预期
    - 所有出现库的地方都[[refresh]]删除重下一定是能解决的，但你这也太搞笑了
  - 但自己一个人的项目在明确后果时可以这么做
    - 你自己个人的[[git-basics/branch]]也可以这么做
- `git push --tags`可以让远程能看到tags
- `git push origin <branch_name>`到指定分支
  - 注意前提是[[checkout]]到你想要的[[git-basics/branch]]
  - 这时往往可加`--set-upstream`参数：关联本地branch和远程branch，之后就只需`git push`即可，在[[git-basics/branch]]也提到了
  - `git pull`也是同理（包括`checkout`，`--set-upstream`等逻辑）
- `git pull`命令变种
  - `--recurse-submodule`选项：可递归pull [[submodule]]
  - [pull所有分支](https://blog.csdn.net/wu1169668869/article/details/83345633)
- 如果你有多个分支，那需要指定`git pull origin main`这种，才把本地的`main`也同步到对应`origin/main`的位置