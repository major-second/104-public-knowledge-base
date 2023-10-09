## 添加和初始化
- 添加
  - 前提：submodule至少有一个[[commit]]，否则是[[general-principles/special-case]]，时至2022.12会出现奇怪错误
  - 命令：`git submodule add <repo-link>`
- 初始化
  - 时机
    - 刚刚添加（`submodule add`）后
    - 在别的地方使用子模块，则可能也需要初始化
      - 例如对于只有外层库，没有内层submodule的情况
        - 如[[github-codespaces]]中的默认状态
  - 方法
    - `git submodule update --init --recursive`（在主模块运行）
      - 这个可能需要前提：[[https-ssh]], [[known-hosts]]
      - 即可递归地初始化！
  - 效果
    - 可以看到`.gitmodules`文件，以及递归初始化了的各个子模块
- [[commit]], [[push-pull]]更新
  - [[commit]], [[push-pull]]等，即可同步“增加了子模块”这一信息到相应的（主模块）git库当前[[git-basics/branch]]
    - 当然，经过相应的[[commit]]，就有可能有的[[git-basics/branch]]有子模块，有的没有
  - 注意：一般推荐在子模块的情况"clean"时提交主模块
    - 例如子模块有些没commit的，主模块这边可能出现[[commit]]时总是留着子模块无法[[commit]]
    - 之后[[clone]], [[push-pull]]都会相应引发麻烦，例如子模块变为[[detached]]状态需要重新[[checkout]]才能正常使用
  - 具体解说
    - 观察到有时出现![](submodule-update.png)这种情况
    - 这种就可能是子模块（自己作为独立的模块）更新了，但父模块没更新子模块版本。也可能是子模块还在dirty中，父模块刚刚[[commit]]但还是留着这个change
    - 你现在显示这样，那么之后在**其它地方**`git clone --recursive`时或`git pull`时就不能得到最新版本子模块，甚至有可能是[[detached]]版本
## 之后使用
- `git clone --recursive <链接>`
  - 如果最外层忘了`--recursive`，那么对于内层模块，就需要如刚刚所说初始化
  - At this moment the submodule may be at a [[detached]] status. You should [[checkout]] it. （刚刚提过）
- 父模块是最新的，子模块不一定也是最新的。父模块完好，子模块也不一定完好
  - 更新：可以单独`cd`进去`pull`，或者`--recurse-submodule`
  - 检查：可以单独`cd`进去`checkout`，或者`--recurse-submodule`
- 父模块并不是记录子模块在哪个[[git-basics/branch]]，而是记录在哪个[[commit]]
  - 因此直接[[push-pull]]后，子模块如果不[[checkout]]就会是[[detached]]状态
  - 此时如果子模块[[commit]]但一直保持[[detached]]，下次再[[push-pull]]后子模块修改丢失！
## [[CRUD]]
### 查询
`git submodule status`
### 删改
- https://www.jianshu.com/p/ed0cb6c75e25
- win操作可能需要[[administrator-powershell]]
- 删除
   - `git submodule deinit <子模块目录> # 执行后子模块目录被清空`
   - `git rm --cached <子模块目录>`，参考[[git-rm]]
   - 当然也需要[[commit]], [[push-pull]]等更新
- 修改
  - 修改`.gitmodules`，然后`git submodule sync`
## 问题
- 有子模块经常会带来杂七杂八麻烦
  - 比如[[settings-json]]中提到的`authentication`相关
  - 比如[[github-codespaces]]不能自动得到，需要手动初始化一下
## 典型应用
和[[fork-private]]以及[[pip]]中`pip install -e .`结合，使得可以修改并使用第三方源码