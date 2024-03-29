设置快捷方式（如桌面快捷方式），并使用快捷键等进一步便捷化
## 设置方法
- `Alt`拖拽文件或文件夹到指定位置比如桌面，设置快捷方式
- 资源管理器窗口（或桌面）中，直接右键新建快捷方式
- （可能管理员权限）[[windows-cmd]] `mklink`命令，在[[keybase#git]]中用到
## 可能的内容
- 某个本地文件或文件夹
  - 不一定是可执行文件
  - 如果不是可执行文件，需要提前设定打开方式，参考[[file-format]]
  - 最典型的：手动设置`.ps1`脚本的打开方式，参考[[ise]]
- 网页（一般使用资源管理器或桌面直接右键新建，输入网址）
- “非平凡”内容
  - 例如[[vmware]]加上命令行参数的运行
    - 直接右键新建快捷方式，目标设置为`"<文件名>.exe" "<文件名>.vmx"`（注意引号）
    - 这样按一组快捷键即可启动vmware并选指定的`.vmx`虚拟机
  - 当然，“非平凡”内容其实也就是一条powershell命令，所以复杂度最高的还是参考[[ise]]
- 所以典型应用：一个快捷方式打开某网页/打开某程序/用指定程序打开某文件/执行某复合操作/执行某[[powershell]]脚本等
  - 创建快捷方式指定快捷键：todo
    ```powershell
    $WshShell = New-Object -ComObject WScript.Shell
    $desktopPath = [Environment]::GetFolderPath("Desktop")

    $links = @(
        @{
            TargetPath = "https://chat.openai.com/chat"
            Hotkey = "Ctrl+Alt+1"
        },
        @{
            TargetPath = ("$PSScriptRoot/my.ps1")
            Hotkey = "Ctrl+Alt+I"
        }
    )
    foreach ($link in $links) {
        $linkPath = "$desktopPath\dummy_$($link.Hotkey).lnk"
        if (Test-Path $linkPath) {
            Remove-Item $linkPath
        }
        $shortcut = $WshShell.CreateShortcut($linkPath)
        $shortcut.TargetPath = $link.TargetPath
        $shortcut.Hotkey = $link.Hotkey
        $shortcut.Save()
    }
    ```
## 快捷键
- “属性”处，设置快捷键
  - 只能设置`Ctrl+Alt+某某`，例如`Ctrl+Alt+1`, `Ctrl+Alt+A`等
  - 一种典型操作：在桌面上按qwerty键盘顺序排快捷方式图标，对应位置的快捷方式就使用对应`Ctrl+Alt+某某`快捷键，方便查阅
    - 这样当然需要去除查看中的“自动排列”选项
- 用法：上一节“典型应用”都可以一键化。比如一键上邮箱，一键运行某脚本等
- 快捷键可能被占用
  - 例如vscode [[vscode-extensions]]中一些插件
  - 例如[[tencent-meeting]]开录屏就会占用
- 删除和新设快捷键有时需要重启（例如去除“vmware加命令行参数运行”快捷键遇到过需要重启生效的情况）
- 有时莫名其妙失效，需要重启[[file-explorer]]
- 和[[taskbar]]可以形成互补
  - 对于经常需要“打开已有”而不是“新打开”的东西，适合放任务栏而不是设置这样的快捷键
    - 比如资源管理器、vscode等
    - 当然，[[keybase]], [[wechat-tips]], win10和11的设置这种“单例”可以不放任务栏，反正你“新打开”也还是一个东西
  - 这时快捷键：`Win+数字`，参考[[taskbar]]
  - 还有些没法创建这种快捷方式，只能创建任务栏图标
  - 比如[[wsa]]设置界面，camera，等