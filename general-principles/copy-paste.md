# 日常使用中的复制粘贴
## 快捷键
- [[general-win-editting-keys]]的`Ctrl+C, Ctrl+V`（最常见）
  - 还有[[win-key#win-v]]高级剪贴板
- [[jupyter-hotkeys]]的`C, V`
- shell中的`Ctrl+Shift+C, Ctrl+Shift+V`
  - 注意`Ctrl+C`是停止，这很坑
  - 参考[[jupyter-basics]]
- [[mobaxterm]]中`shift+insert`
## 涉及公司内网
- 参考[[file-transfer]]
- 需要探索一下哪些地方，哪些方向可以复制粘贴等
- 为了合规，很有可能外网能贴进来，反过来不行
- 有些host互通，有些host不互通。自己探索公司的workspace软件！
## 格式、场合
- [[set-paste]]防止vim粘贴格式乱
- 粘贴多行时，若没有`; \`，结果可能在bash中不符合预期，参考[[11-basic-scripting-partA]]“换行拓展”
- 复制东西时前后可能有一些空格、回车等，粘贴时有时会导致麻烦
  - 登录网站时显示用户名错误
  - [[generate-key-pair]]中提到少复制空行
    - 所以整个文件复制比较靠谱这时。文件作为一种“抽象”
## 其它
[[vscode/edit]]中的快捷键（如`Alt+上下`移动行，`Alt+Shift+上下`复制行）可以节省剪贴板使用