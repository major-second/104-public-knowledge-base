- [wiki](https://en.wikipedia.org/wiki/Pipeline_(Unix))
- 参考
  - [[standard-streams]]
  - anonymous: maybe [[functional-programming]]
# 功能
管道记号：一个命令的输出直接作为下一个命令的输入，不需要缓冲区或者文件啥的
例如：
- `set | sort | more`（连续使用2次），表示把`set`的结果排序，并且显示时不一次显示完，而是按回车可以往下走那样
- `set | sort > <文件>`：先管道再重定向，写给文件
- 实用应用：
  - `ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`
  - `python_pid=$(ps -ef | grep 'python' | grep -v grep | awk '{print $2}')`
  - `find . -type f -print0 | sort -z | xargs -0 md5sum | md5sum`，参考[[md5sum]]
# 性能
- [[buffer]]相关
  - 可能不需要全部算完再下一步，这样会更快