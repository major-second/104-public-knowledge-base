- 下方窗口的下方有一列tab（`Git, Run, Debug`等）
- 该列的级别比下方窗口的上方tab高
  - 比如[[pycharm-debug]]时，自动跳入下方窗口的下方`Debug` tab，此时上方可以选择`Debugger`或`Console`
    - `Debugger`处可以监视、监视区右键添加新的监视等
    - `Console`就类似vscode的[[debug-console]]，断点时，可以在此界面输入表达式、执行语句等（当然可能有一定延迟）
  - 如果不是debug而是直接运行，自动跳入`Run`，可以看到输出结果（只读）
  - `Terminal`是终端可输入`shell`命令，如`echo 1`输出`1`
  - `Python Console`可输入`python`命令（交互式），如`1+1`输出`2`