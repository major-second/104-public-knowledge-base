插件名`Markdown PDF`
目前官方教程有点问题（号称打开`.md`时自动开始下载chromium，其实没有）
所以我们自己[[下载安装chrome]]，然后指定`"markdown-pdf.executablePath"`(参考[[settings]])为`chrome.exe`的**含最后一步`chrome.exe`的**路径。例如`"markdown-pdf.executablePath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"`
现在可以右键`.md`文件导出，也可以`Ctrl + Shift + P`导出
不过目前暂时并不能使用数学公式等markdown preview enhanced才能用的非原生markdown功能