参考[[recipe]]，必须使用`bibtex`命令，且总共是指定的4个命令序列，才能正常显示参考文献
和[[minimum-beamer/README]]的区别：
- `\usepackage[bookmarks=true]{hyperref}`使得可使用`hyperref`跳转
- 最后加上
```tex
\bibliography{ref}
\bibliographystyle{plain}
```
- 中途至少加上一个参考文献`\cite`，否则不允许`bibtex`
- 有一个`ref.bib`，对应的是`\bibliography{ref}`中的`ref`，里面包含参考文献信息