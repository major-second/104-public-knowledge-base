- 基本的字符串操作：
  - `"1|2".split("|")`
  - `"1|2".split("|")[0]`
  - `" 1 ".trim()`
  - 脚标当然可以有负数，类似python
  - 应用
    - [[power-automate/features]]
    - 结合[[powershell-var]]，例如`$PSScriptRoot.split("\")[-1]`
- `| Select-String`
  - 参考[[11-basic-scripting-partB]]的管道记号
  - 类比[[find-grep]]
  - 可搜[[regex]]
  - 例如[[reinstall-app]]用到`Get-AppxPackage -allusers | Select Name, PackageFullName | Select-String WindowsStore`
  - 例如验证[[configure-proxy]]可以用`curl ipinfo.io | select content | select-string country`
- `-`开头的运算符
  - `-match`是[[regex]]匹配
  - `-contains`是全字匹配
  - `-like "*substring*"`是匹配子串，和[[find-grep]]常用做法一致
```powershell
PS > (echo Ubuntu-18.04) -match ".*Ubuntu.*"
True
PS > (echo Ubuntu-18.04) -contains ".*Ubuntu.*"
False
PS > (echo Ubuntu-18.04) -contains "Ubuntu"
False
PS > (echo Ubuntu-18.04) -like "*Ubuntu*"
True
PS > (echo Ubuntu-18.04) -contains "Ubuntu-18.04"
True
PS > (echo My Ubuntu-18.04) -contains "Ubuntu-18.04"
True
```