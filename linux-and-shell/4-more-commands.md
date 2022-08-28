# 4.1
- `ps`：最基础：当前控制台，当前用户。一般输出很少
  - `PID`进程号（非常重要），`TTY`，运行时间等
- 三种风格参数，让人头痛！这就是[[compatibility]]的完美写照……
- 常用：`ps -ef`列出适当的信息量。`ps -ef --forest`列出森林
- 参考[[11-basic-scripting-partB]]的管道符号和[[find-grep]]等，有一些很实用的操作：
  - `ps -ef | grep 'python' | grep -v grep`（查找含有`python`的进程，但排除自己）
  - `ps -ef | grep python | grep run`这种：两个关键词的查询
  - `ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`（进一步输出进程号）
    - 注：`awk`也可以换成适当的`cut -c`命令（切出指定位置的字符）
  - 出来一个列表之后，`| xargs kill -9`：大屠杀！参考[[xargs]]
  - 注：这里`ps -ef`给出列表，然后不断管道进行操作，最后一起[[xargs]]，具有[[functional-programming]]的[[map-reduce]]思想
- `watch 'ps -ef'`等等：每隔2秒输出一次
  - 比如`watch nvidia-smi`，也行。上面那些命令都可以组合上`watch`
  - `-n <数字>`指定多少秒一次
- 顺带：其它和监视有关的指令[[monitor]]
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
- 这里花括号里面包含的`sleep 3; echo 1;`的ppid相同，但每句pid都不同
3. 金蝉脱壳
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
- 现象
  - `echo 2`还是有。也就是`;`分开的前面被杀不影响后面
  - 而且`&`标记后台运行的进程能正常`Done`
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
- 现象：没有`echo 2`了，也没有`Done`了，而是显示`Killed`