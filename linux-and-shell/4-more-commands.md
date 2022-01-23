# 4.1
- `ps`：最基础：当前控制台，当前用户。一般输出很少
  - `PID`进程号（非常重要），`TTY`，运行时间等
- 三种风格参数，让人头痛！这就是[[compatability]]的完美写照……
- 常用：`ps -ef`列出适当的信息量。`ps -ef --forest`列出森林
- `watch 'ps -ef'`等等：每隔2秒输出一次
  - 比如`watch nvidia-smi`，也行
- 参考[[11-basic-scripting-partB]]的管道符号，有一个很实用的操作：