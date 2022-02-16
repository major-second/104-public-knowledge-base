# 4.1
- `ps`：最基础：当前控制台，当前用户。一般输出很少
  - `PID`进程号（非常重要），`TTY`，运行时间等
- 三种风格参数，让人头痛！这就是[[compatibility]]的完美写照……
- 常用：`ps -ef`列出适当的信息量。`ps -ef --forest`列出森林
- 参考[[11-basic-scripting-partB]]的管道符号，有一个很实用的操作：
  - `ps -ef | grep 'python' | grep -v grep`（查找含有`python`的进程，但排除自己）
  - `ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`（进一步输出进程号）
- `watch 'ps -ef'`等等：每隔2秒输出一次
  - 比如`watch nvidia-smi`，也行。上面那些命令都可以组合上`watch`
## 实践
- 多进程和大括号的关系示例
分别尝试
```sh
sleep 3 & \
{
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  echo $pid
  sleep 2
  kill -9 $pid
}
```
```sh
{sleep 3; echo 1; sleep 3; echo 2} & \
{
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  echo $pid
  sleep 4
  kill -9 $pid
}
```