- 列表
`find . -type f -print0 | sort -z | xargs -0 md5sum`
- 列表后再做`md5sum`，即可以递归核对整个文件夹
`find . -type f -print0 | sort -z | xargs -0 md5sum | md5sum`
  - 注意`find <文件夹>`和`cd <文件夹>`进去再`find .`结果不相同！
- 针对`git`库的`md5sum`结果仅供一台机器的参考。不同机器重复同样动作可能不同
- 对于`conda`这种官网给的`*latest*.sh`脚本嘛，官方一更新自然就不同了嘛。否则就相同。所以为了稳定可以不使用带`latest`的url