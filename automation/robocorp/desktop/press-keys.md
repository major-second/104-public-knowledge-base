- 官方文档
  - [简单示例](https://robocorp.com/docs/libraries/rpa-framework/rpa-desktop/keywords#press-keys)
  - 功能键：[去这](https://robocorp.com/docs/libraries/rpa-framework/rpa-desktop)
    - 搜索`function keys`
    - 看到各个键盘键的名称
    - 不区分大小写
    - 可以带一个空格，如`page up`
    - windows徽标键是`cmd`
- 注意：如果只输入文本可以使用`Type text`
- 如何尽可能少使用鼠标？
  - [[settings/keyboard-shortcuts]]，[[fn]]，[[editting]]，[[built-in-keyboard-shortcuts/window]]，[[misc]]等等快捷键
  - `cmd`键打开开始菜单，输入程序名来打开
  - 这时需要[[化归]]防止输入法带来麻烦（即切换为英文输入，参考[[automation/trivial-mistakes]]中的）
  - 例如
```robotframework
    Log               Setting English typing.
    TRY
        Wait For Element    image:zhong.png
        Press Keys    shift
    EXCEPT  TimeoutException: No matches found for: image:zhong.png
        Log           Now already using English typing
    END
    Type Text         proxy settings
```
其中`zhong.png`是右下角托盘中文状态的“中”字
- 参考例子：`104-public-knowledge-base\automation\robocorp\example\desktop\turn-off-proxy`
- 目前`alt + space`快捷键功能不正常，原因未知，但可以通过[[built-in-keyboard-shortcuts/window]]的`win + 方向键`凑合一下
  - 这就是[[workaround]]的思想