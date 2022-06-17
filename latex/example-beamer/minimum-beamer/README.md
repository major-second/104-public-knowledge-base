参考[[recipe]]：该文件编译不可以使用`bibtex`命令
- beamer中使用`\verb`需要`\begin{frame}[fragile]{标题}`
  - 注意这个`[fragile]`并不是`{frame}`的option，不要写到`{frame}`前面
- 使用中文：把开始的`\documentclass{beamer}`改成`\documentclass{ctexbeamer}`