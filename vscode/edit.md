`vscode`毕竟本体还是编辑器，当然要掌握常见编辑技巧
- 可以参考[[general-win-editting-keys]], [[vim-keys]]
- 有个Editor Playground教你常用技巧
  - 比如`Alt`多光标，`Alt+上下`移动行，`Alt+Shift+上下`复制行
    - 节省[[copy-paste]]剪贴板使用很好用
  - 进阶
    - `Alt`多光标，然后`Shift + End`选中一系列东西，参考[[vim-keys]]
      - 笔记本`End`可能和fn键共用，参考[[fn-keys]]
    - `Ctrl+Alt+方向键`使多光标出现在开头，然后按一次`End`到各自结尾
      - 或者`下, 左`到结尾（前提是下面至少还有一行）
- `Ctrl+F`查找，`Ctrl+H`替换
  - 替换的常见操作：`Ctrl+H, <原字符串>, Tab, <新字符串>`，鼠标点击上下按钮移动到指定位置
  - 焦点在上下按钮时，回车是“下一个”
  - 焦点在编辑器时，回车是换行
  - 焦点在替换文本框时，回车是“替换并下一个”
- `ctrl+I`
  - 一般代码中trigger提示，当然[[markdown]]中斜体
- 选中一部分文本后，试着按有些键，就会把文本包起来而非替换文本
  - 在需要`'被包裹部分', (被包裹部分), **被包裹部分**`这种时很实用
  - 如`*`，`(`等在`.md`文件中可以这么用
  - `$`在latex中可以（但markdown不行）
  - 各种代码文件中也有各自可用的这种操作
- `.md`中，剪贴板里是链接（`http://`开头）时，选中文本按`Ctrl+V`不会覆盖而是“给它加上链接”
  - 联想[[paste-image]]的选中文本按`Ctrl+Shift+V`
- win: shift alt f formatting