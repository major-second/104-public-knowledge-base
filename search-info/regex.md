https://www.runoob.com/regexp/regexp-syntax.html
（不能全信，比如`grep`中有[这种麻烦](https://stackoverflow.com/questions/53867329/why-cant-i-use-s-with-grep)）
语法举例
- 想找两个空格，但不能有更多空格：<code>[^ ]&nbsp;&nbsp;[^ ]</code>
- 只看后4张卡占用：`grep '[4-7]\s\+T'`

使用
- [[find-grep]]中用，比如`nvidia-smi | grep '[4-7]\s\+T'`（注意双引号）
- vscode全文搜索，看最右侧按钮![](vscode-regex.png)