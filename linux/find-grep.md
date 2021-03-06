- 基本用法
  - `grep <内容> <文件名> `，文件中找内容
    - `-e`[[regex]]，`-i`不区分大小写，`-v`反向（“不匹配”）
    - 参考[[11-basic-scripting-partB]]的经典句子`ps -ef | grep 'python' | grep -v grep | awk '{print $2}'`
  - `find <目录>`把目录下文件列成表
  - `find <目录> -name "*.txt"`找所有`.txt`文件，列成表（注意引号）
- 结合用法
  - `find <目录> | grep <字符串>`，找文件/文件夹名包含某某的
  - `find <目录> -name dummy.txt | xargs grep <内容>`
  - 刚刚后两者都是把（单个或多个）文件给`grep <内容>`，参考[[11-basic-scripting-partB]]的管道记号
    - 直接管道记号是把那个文件名列表（标准输入`-`）整个作为（一个）文本文件（“metadata”的感觉）
      - 所以标准输入（管道）进入`md5sum`会出现`-`字符
    - [[xargs]]是传多个文件
      - 完整（懒人最少bug版）的`xargs`命令用法：参考[[md5sum]]的`find . -type f -print0 | sort -z | xargs -0`
      - 一是排序，让`md5sum`有确定性
      - 二是人为指定分隔符，避免空格出问题
- 其它`grep`用法
  - `-C`看上下文（比如[[fsck]]的emergency mode中救命，可关键了）
  - 使用[[regex]]
    - 比如`nvidia-smi | grep '[4-7]\s\+T'`只看后4张卡
      - 注意引号
    - 比如`du -h | grep '[0-9]G\s'`只看较大的文件夹