[参考](https://medium.com/@shrirammano/understanding-git-stash-and-using-it-easily-in-vscode-7da049160097)
- 注意
  - 对于新建文件如果untracked（没有`add`到index，参考[[git-basics/basics]]），那么`git stash`没用。需要先`add`才行！
  - 相比之下，修改文件是可以直接`git stash`存起来的
- 常见应用
1. [[push-pull]]如果因为conflict不能执行，可以
   1. 先把当前working copy `add`到index
   2. 再`git stash`存起来
   1. 再`git pull`远程结果
   3. 再`git stash pop`并解决conflict
2. 基于hard-[[reset]]，“微调远程remote上的当前commit”
   - 实际工程中不太建议，特别是和别人合作时
   - 自己的[[git-basics/branch]]可以
   1. 先把当前working copy `add`到index
   2. 再`git stash`存起来
   3. hard [[reset]]回上个commit
   4. 参考[[push-pull]]，用`--force`参数`push`，这样远程也回滚了
   5. `git stash pop`出刚刚的文件，进行调整
   6. `git push`调整后的结果