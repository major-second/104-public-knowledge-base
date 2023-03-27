- 前置[[git-installation]]
- [参考文档](https://git-scm.com/docs/git-init)
- 初始化一个git库的几种方法
  1. 在`github`或者[[other-hubs]]在线新建库，然后`git clone`到本地
  2. 直接vscode任意打开一个文件夹，然后`Ctrl+Shift+G`，看到init按钮
  3. 命令行操作：直接在目标文件夹执行命令`git init`
- 创建之后常见紧接着的步骤
  - 如方法3.后，直接`git add .`，`git commit -m <信息>`，把当前文件夹所有文件添加到[[commit]]
  - 之后不一定要[[push-pull]]，可以就用git在本地管理。常见于公司有保密协议不能传到github时