插件名`Markdown PDF`
目前官方教程有点问题（号称打开`.md`时自动开始下载chromium，其实没有）
- 所以我们自己[[下载安装chrome]]
- 然后指定`"markdown-pdf.executablePath"`为`chrome.exe`的路径（以`chrome.exe`结尾）
  - 例如`"markdown-pdf.executablePath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"`
  - 参考[[vscode/settings]]
- 现在可以右键活动的`.md`编辑窗口，导出
  - 也可以`Ctrl + Shift + P`后找指定命令导出
- 不过，这种导出没有[[enhanced]] features
  - 如果要[[enhanced]] features（如公式）
  - 就得参考[[markdown-preview-enhanced]]中的导出方法
  - 即先预览再用[[markdown-preview-enhanced]]导出