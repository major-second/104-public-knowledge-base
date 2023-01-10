- 前置[[texlive]]
- 典型1：无需引用
  - `xelatex -synctex=1 -interaction=nonstopmode -file-line-error src.tex`
- 典型2：需要引用
```sh
function myxe { 
    xelatex -synctex=1 -interaction=nonstopmode -file-line-error src.tex
}
function mybib { 
    bibtex src.aux
}
myxe; mybib; myxe; myxe
```
注意`bibtex`参数写的是`.aux`
- 如果你文中没有任何引用`\cite`，那么不可以使用`bibtex`
  - 也就是至少要有一个`\cite`，才可以使用`bibtex`
    - 是不是有点诡异（
  - [参考](https://tex.stackexchange.com/questions/442519/truly-ignore-bibtex-error-no-citation-commands)）
  - 举例：对比[[minimum-beamer/README]]和[[beamer-with-citations/README]]