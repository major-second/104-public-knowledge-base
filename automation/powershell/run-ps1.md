一个`.ps1`里run其他的？
- 直接`<路径>`即可
- 如果需要[[refresh]]（比如[[configure]]中的），那就`Start-Process powershell.exe -NoNewWindow -Wait -ArgumentList <路径>`这样新起一个进程