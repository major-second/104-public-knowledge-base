- 开始菜单以管理员运行
![](administrator-start-menu.png)
- vscode中powershell以管理员运行：[参考](https://blog.csdn.net/Cloud1209/article/details/120390525)
- 获得权限
  - `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
    - 给单个进程获得运行权限
  - `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
    - 给当前用户获得运行权限
    - 参考[[settings-and-configurations]]