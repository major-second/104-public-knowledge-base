- 如何run我的第一个`ps1`？
  - 没有权限
    - 参考[[administrator-powershell]]，以及其中的`ExecutionPolicy`相关设置命令
  - 不能双击运行？从而[[windows-link]]也不方便一个快捷键运行？
    - [[file-format]]打开方式选择`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`这种东西
- 一个`.ps1`里run其他的？
  - 直接`<路径>.ps1`即可
    - 对比[[bash]]：那个需要`./<file>.sh`，或者加入[[6-env]]
  - 如果需要[[refresh]]，加载[[windows/env-var]]
    - 比如[[configure-proxy]]中的
    - 那就`Start-Process powershell.exe -NoNewWindow -Wait -ArgumentList <路径>`这样新起一个进程