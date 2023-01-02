- 列表
`find . -type f -print0 | sort -z | xargs -0 md5sum`
- 列表后再做`md5sum`，即可以递归核对整个文件夹
`find . -type f -print0 | sort -z | xargs -0 md5sum | md5sum`
  - 注意`find <文件夹>`和`cd <文件夹>`进去再`find .`结果不相同！思考：为什么？（可以去掉最后一个`| md5sum`，进行探究）
  - 注：如果两个文件夹用这条命令对比`md5`不一致，那就不妨回到刚刚第一条命令“列表”，看看到底哪里出了差错
  - 结果中出现的`-`字样表示标准io流，参考[[curl-wget]]也有类似的`wget -O -`
- 针对`git`库的`md5sum`结果仅供一台机器的参考。不同机器重复同样动作可能不同
- 对于`conda`这种官网给的`*latest*.sh`脚本嘛，官方一更新自然就不同了嘛。否则就相同。所以为了稳定可以不使用带`latest`的url
- 拓展用法：结合[[find-grep]]，出现`find . -type f -print0 | sort -z | xargs -0 md5sum | grep -v <去除的文件名> | md5sum`这种，不看一部分文件