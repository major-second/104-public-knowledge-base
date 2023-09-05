## 优劣
是开源的
- 好处
  - 方便运行，分享，复制等
  - 一行命令`tagui <某>`即可执行，也可自动定时执行，双击图标执行等
  - 可以不联网运行（所以可以用来做排查网络的bot）
  - 不像商业的[[my-first-flow]]那样有很多限制
- 坏处
  - ocr识别率极度低下
  - 功能少
  - `hover`, `click`命令会漂移，需要连续发几个才会逐渐“收敛”。比如`hover -> hover -> click`
## 安装
https://tagui.readthedocs.io/en/latest/setup.html
文档很清楚了
一些关键
- 其安装依赖于chrome, java等（其懒人installer会装依赖）
- 对于windows，请安装到无需管理员的文件夹，否则可能需要[[administrator-powershell]]权限的powershell才能用`tagui`命令，烦
- 安装后vscode当然需要[[refresh]]（关掉窗口再重启）才能用命令
- `cmd`命令提示符和[[powershell-basics]]都能用
## 使用要点
- 用`using ocr`使用ocr（但成功率不高且不支持中文）
- `hover`可以当作[[wait-for]]使用
- `timeout <秒数>`决定`hover, exist`等多种行为的等待时间
- `tagui <某> -n`无需浏览器
- 由于`hover`的漂移和`ocr`不太行，所以只能多使用找图和键盘操作。参考本文件夹的连接wifi机器人
- 可以作为[[bootstrap]]的[[temp-solution]]，用它定时启动/双击启动一些商业RPA如[[my-first-flow]]
- 举例：本文件夹的`connect-wifi`可用于在win11连接第一个wifi