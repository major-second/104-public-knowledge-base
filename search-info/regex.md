https://www.runoob.com/regexp/regexp-syntax.html
（不能全信，比如`grep`中有[这种麻烦](https://stackoverflow.com/questions/53867329/why-cant-i-use-s-with-grep)）
语法举例
- 想找两个空格，但不能有更多空格：<code>[^ ]&nbsp;&nbsp;[^ ]</code>
- 只看后4张卡占用：`grep '[4-7]\s\+T'`

使用
- 参考[[11-basic-scripting-partB]]中的“管道记号”
- [[find-grep]]中用，比如
  - `nvidia-smi | grep '[4-7]\s\+T'`
  - `du -h | grep '[0-9]G\s'`
- [[powershell/string]]中的`| Select-String`
- vscode全文搜索，看最右侧按钮![](vscode-regex.png)