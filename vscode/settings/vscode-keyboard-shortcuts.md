## 总述
- File - Preferences - Keyboard Shortcuts看列表（快捷键`Ctrl+K Ctrl+S`）
  - 此处
    - 可以搜索，可以[[CRUD]]快捷键
    - 这里可以看到自定义了的快捷键但看不到已经删除默认的
  - 但![](keybindings-json.png)这个右侧按钮看`json`可以看所有自己修改过的（包括增删改）
  - 比如本文件夹的`keybindings.json`就是一个实际例子
  - 比如一个较简短的例子如下
```json
// Place your key bindings in this file to override the defaultsauto[]
[
    {
        "key": "ctrl+shift+alt+h",
        "command": "git.viewHistory"
    },
    {
        "key": "ctrl+shift+alt+t",
        "command": "python.launchTensorBoard"
    },
    {
        "key": "ctrl+b",
        "command": "-workbench.action.toggleSidebarVisibility"
    }
]
```
注：这里`Ctrl+B`删掉是为了防止和[[tmux]]冲突
- `Ctrl+K`后接别的键的快捷键称为chord快捷键
  - 如果接的是单字母，那么在中文输入法或者只读编辑窗口会用不了。比如`Ctrl+K U`关闭所有已保存的标签
  - 所以不妨把这类快捷键自定义修改了
- `Ctrl+Alt+Shift`一起按的往往都给你留着了
## 调试相关
- `Ctrl + Shift + D`到调试面板
  - 此时默认在左上角绿色播放按钮处。可以按右键，再按上下键，调整使用的`launch`设置，然后直接`F5`（纯键盘操作，爽！）
- `F5`运行或断点状态下继续（请结合[[launch]]使用，最大化效率。达到“一键启动”效果）
  - 还可以结合断点，直接`F5`到指定位置
- `F10`单步
- `F11`进入
- `Shift+F11`跳出当前（函数等等）
- <code>Ctrl + &#96;</code>终端
- `Ctrl + Shift + Y` [[debug-console]]
## 搜索
- `Ctrl + Shift + P`搜索命令（称为Command Palette）
  - 参考[[extensions/general]]，安装插件可能出现新的命令
- `Ctrl + P`搜索文件名
  - 搜索文件夹名时这个可能出来优先级很低
    - 此时需要`Ctrl+Shift+E`资源管理器中`Ctrl+F`（或不按`Ctrl+F`直接输入查找）
- `Ctrl + Shift + F`全文查找
  - 不过这个有时会被占用。比如![](keyboard-ubuntu.png)
  - 右键，把所有复选框去掉勾并删除字母`f`就能去掉这一快捷键
- 当然文档里普通的`Ctrl+F`查找还是有的
- `Ctrl + P`这个实用快捷键还有个作用：打断其它“上方跳出界面”
  - 在其它界面没有正确设置退出条件（也就是你鼠标左键点外面，它还在上面占空间这种）时
  - 你可以`Ctrl + P`把“上方跳出界面”变成查找文件界面，然后鼠标左键点外面就出来了
## 其它实用快捷键
- 闲的没事干逛逛`Ctrl+K Ctrl+S`有惊喜
- [[terminal]]中有很多好用的
- 编辑窗口
  - `ctrl+数字`选哪组窗口
    - 已经2组，则`Ctrl+3`还能新增一组
- `Ctrl`按住，`KJ`展开，`KJK1`展开再关闭到第一层，`KJK2`以此类推
  - 当然，当前光标所处的不会被关闭
  - 实用例子：比如你在写[[minimum-beamer/README]]这种文档，那么`\section`是第二层，`\frame`是第三层，所以`Ctrl`然后`KJK3`就可以看到所有frame标题
## troubleshooting
一些特殊地方可能会用不了快捷键
- 比如[[tensorboard]]在vscode中的窗口
- 比如vscode-pdf预览窗口