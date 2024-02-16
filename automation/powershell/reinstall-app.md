重装删除了的内置应用（以应用商店为例）
- [[administrator-powershell]]权限运行powershell
- 运行命令`Get-AppxPackage -allusers | Select Name, PackageFullName | Select-String WindowsStore`
  - `Select`选择字段，参考[[powershell]]
  - `Select-String`后可跟[[regex]]，参考[[powershell/string]]
- 找到名称（形如`PackageFullName=Microsoft.WindowsStore_<某某>`）
- 复制
- `Add-appxpackage -register "C:\Program Files\WindowsApps\Microsoft.WindowsStore_<某某>\appxmanifest.xml" -disabledevelopmentmode`