- 在使用`git`管理的项目中，`git clone`下来的文件表面只有HEAD的，但实际上有一个分支的所有版本
  - 非HEAD的版本都存放在一些隐藏的地方（`.git`）。[[checkout]]可以显现
  - 当然Git不是傻傻存全部，而是增量存的。[[push-pull]]中也有提到
- 如何看到？
  - vscode用[[vscode-keyboard-shortcuts]]中的`Ctrl + P`可以看到这些隐藏文件，其路径有一些hash码
  - 用[[view-git-log#git history]]的compare也能看到
- 这些隐藏文件和你自己工作区里的文件不是一个东西
  1. 修改它们不能修改你工作区的文件
     - 也就是，在[[view-git-log#git history]]处比较时无法很方便地修改
     - 相比之下
       - vscode资源管理区ctrl选择两个文件compare可以方便修改
       - vscode在`Ctrl + Shift + G`区预览时也可以
  2. 它们没有正常功能（因为没有其[[dependencies]]路径的其它东西）
     1. 比如markdown`![](图片)`无法显示图片