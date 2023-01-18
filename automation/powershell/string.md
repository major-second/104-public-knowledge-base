- 基本的字符串操作：
  - `"1|2".split("|")`
  - `"1|2".split("|")[0]`
  - `" 1 ".trim()`
  - 这在[[power-automate/features]]中有重要作用
  - 脚标当然可以有负数，类似python
- `| Select-String`
  - 参考[[11-basic-scripting-partB]]的管道记号
  - 可搜[[regex]]
  - 例如[[reinstall-app]]用到`Get-AppxPackage -allusers | Select Name, PackageFullName | Select-String WindowsStore`
  - 例如验证[[configure]]可以用`curl ipinfo.io | select content | select-string country`
- `| Where-Object`
这个有点坑，`-match`才是[[regex]]匹配，`-contains`竟然是要完全匹配，而不是[[find-grep]]或者`Select-String`那样
```powershell
echo Ubuntu-18.04 | Where-Object { $_ -match ".*Ubuntu.*" }
echo Ubuntu-18.04 | Where-Object { $_ -contains ".*Ubuntu.*" }
echo Ubuntu-18.04 | Where-Object { $_ -contains "Ubuntu" }    
echo Ubuntu-18.04 | Where-Object { $_ -contains "Ubuntu-18.04" }
```