# 普通
- [安装过程](https://zhuanlan.zhihu.com/p/344887837)
- [官网下载](https://www.python.org/downloads/windows/)
  - 可选：带上[[pip]]
- 如果要[[powershell]]可用python命令，需要
  - 把`python.exe`所在路径加入[[windows/env-var#path]]，并优先级靠前
    - 否则[[powershell]]中输入`python`命令将会到安装界面，而不是正常启动！微软爹味，烦
# [[scoop]]
- 直接`scoop install python`
- 且可能他会运行一个`.reg`（参考[[regedit]]），使得直接可用`python`命令于[[powershell]]
