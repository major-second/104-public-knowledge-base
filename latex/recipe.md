参考https://www.cnblogs.com/minor-second/p/15710893.html
常见两种`"tools"`列表（写到`vscode`的`json`文件里的。和命令也是对应关系）
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
- 如果你文中没有任何引用`\cite`，那么不可以使用`bibtex`（[参考](https://tex.stackexchange.com/questions/442519/truly-ignore-bibtex-error-no-citation-commands)）
    - 至少要有一个`\cite`，才可以使用`bibtex`
    - 举例：对比[[minimum-beamer/README]]和[[beamer-with-citations/README]]