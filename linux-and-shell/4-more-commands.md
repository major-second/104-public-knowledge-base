# 4.1
- `ps`：最基础：当前控制台，当前用户。一般输出很少
  - `PID`进程号（非常重要），`TTY`，运行时间等
- 三种风格参数，让人头痛！这就是[[compatibility]]的完美写照……
- 常用：`ps -ef`列出适当的信息量。`ps -ef --forest`列出森林
- 参考[[11-basic-scripting-partB]]的管道符号，有一个很实用的操作：
  - `ps -ef | grep 'python' | grep -v grep`（查找含有`python`的进程，但排除自己）
  - `ps -ef | grep python | grep run`这种：两个关键词的查询
  - `ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`（进一步输出进程号）
  - 出来一个列表之后，`| xargs kill -9`：大屠杀！参考[[xargs]]
- `watch 'ps -ef'`等等：每隔2秒输出一次
  - 比如`watch nvidia-smi`，也行。上面那些命令都可以组合上`watch`
## 实践
- 多进程和大括号的关系示例
分别尝试
1. 正常查杀
```sh
sleep 3 & \
{
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  echo detected: $pid
  sleep 2
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  kill -9 $pid
}
```
2. 刻舟求剑
```sh
{ 
  sleep 3; echo 1; sleep 3; echo 2
} & \
{
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  echo detected: $pid
  sleep 4
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  kill -9 $pid
}
```
3. 金蝉脱壳（`echo 2`还是有）
```sh
{ 
  sleep 3; echo 1; sleep 3; echo 2
} & \
{
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  sleep 4
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  echo detected: $pid
  sleep 1
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  kill -9 $pid
}
```
- 注：其实父进程的命令是`/usr/bin/bash`这样的。所以你`grep 'sleep 3'`找不着
4. 连坐制
```sh
{ 
  sleep 3; echo 1; sleep 3; echo 2
} & \
{
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  sleep 4
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  pid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $2}')
  ppid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $3}')
  echo detected: $pid, $ppid
  sleep 1
  echo $(ps -ef | grep 'sleep 3' | grep -v grep)
  kill -9 $pid $ppid
}
```