- `echo hello world`
- `echo -n no newline; echo -n no newline`
- `echo -e "\033[35m colorful \033[0m colorful"; echo -e "\033[32m colorful \033[0m colorful"`
  - 注意`echo -e \n; echo -e "\n"`效果当然不同
  - 前者：还没来得及作为`echo`的参数就已经被转义[[escape]]了（trivially转义，`\n`还是`n`）
  - 所以颜色那个例子也可以`echo -e \\033\[35m`这样，这里`\[`是为了兼容[[zsh]]，不用引号是减少外层所需[[escape]]，比如在[[wsl-command]]中
- 重定向`>`, `>>`、`echo`多行：参考[[11-basic-scripting-partA]]
- 拓展：需要[[7-permissions]]时：
  - `echo 1 | sudo tee <file>`
  - `echo 1 | sudo tee -a <file>`（追加）
  - 比如[[wsl-command]]就有用到
- 把其它地方来的输入重定向过来，不要空行：比如`ls | xargs echo -n`