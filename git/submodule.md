常用命令
- 首先
`git submodule add -b <branch> <repo-link>`
- 然后
`git submodule update --init --recursive`（在主模块运行），即可递归地初始化！
- 可以看到`.gitmodules`文件，以及递归初始化了的各个子模块