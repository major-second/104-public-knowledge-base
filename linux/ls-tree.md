- `ls --help`一下，注意`-a, -A -d`都挺有用的
  - `ls -al ~/.ssh`
  - `ls -d $(pwd)/*`显示带绝对路径，但不递归
    - 递归绝对路径适用`find ... | grep`, 参考[[find-grep]]
  - `ls -l`，`ll`，`ls -lR`在[[ln-s]]中用于检查
  - 常和[[regex]] `grep`结合使用
- `sudo apt install tree`
  - 递归[[general-principles/recursion]]可视化高级`ls`
  - `tree -L 2`限制层数
  - `tree -P ...`找pattern
  - `tree --filelimit 10`超过指定文件数就不显示
  - [参考](https://linuxsimply.com/tree-command-in-linux/)