前置：
- 对power automate总体已经上手（比如[[my-first-flow]]，[[power-automate/var]]，[[selector-builder]]等）

这里收集一些power automate能做的feature
- 可以运行[[powershell/basics]]脚本，比如`mv`移动文件，`rm`删除文件等操作
  - 应用：由于[[git/installation]]中可以把powershell自动弄得可以使用`git`命令，所以可以使用powershell命令来定期同步github和[[other-hubs]]的镜像（todo）
- 可以使用[[xbox-bar]]的`Win+Alt+R`录屏
  - 不过需要Focus Window，录屏才能录到指定的窗口
    - 失败了？可以尝试重新`Win+Alt+R`，或者尝试等待一下等等。所以这里可能需要[[control]]中的无限循环和`Exit loop`命令
    - 即：直到看到录制的小红点为止
  - 且在调试模式会录power automate的窗口。不过正常运行时是正常的
- `Display message`可以给出一个小窗口（可以自行消失，可以和`Wait`结合使用）