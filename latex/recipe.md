# 前置
- [[vscode-latex]]插件
- 参考[[latex/command-line]]，有对应关系
    - 像[[minimum-beamer/README]]和[[beamer-with-citations/README]]对比这种也要了解
# 内容
参考https://www.cnblogs.com/minor-second/p/15710893.html
常见两种`"tools"`列表
- 是写到`vscode`的[[settings-json]]文件里的
- 和[[latex/command-line]]也是对应关系
- 需要引用参考文献时是以下指定的4个
```
"xelatex",
"bibtex",
"xelatex",
"xelatex"
```
- 不需要引用参考文献时是
```
"xelatex"
```