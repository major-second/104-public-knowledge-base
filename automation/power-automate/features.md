前置：
- 对power automate总体已经上手（比如[[my-first-flow]]，[[power-automate/var]]，[[selector-builder]]等）

这里收集一些power automate能做的feature
- 可以运行[[powershell/basics]]脚本，比如`mv`移动文件，`rm`删除文件等操作
  - 应用：由于[[git/installation]]中可以把powershell自动弄得可以使用`git`命令，所以可以使用powershell命令来定期同步github和[[other-hubs]]的镜像（todo）
  - 可以用`scp, ssh`等
  - 可以输出东西作为[[power-automate/var]]存起来
    - 输出的一般带回车，所以在输出之后需要在power automate中trim
    - powershell里trim没用的！
- 可以使用[[xbox-bar]]的`Win+Alt+R`录屏
  - 不过要考虑[[focus]]问题
  - 并且有时会玄学没反应，按第二次`Win+Alt+R`就行（真的玄学）
- `Display message`可以给出一个小窗口（可以自行消失，可以和`Wait`结合使用）
- 可以`zip, unzip`文件或文件夹
  - 发邮件时很好用。直接发一个压缩包过去