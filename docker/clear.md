`df`看到`overlay`太多东西占满了！怎么办
首先注意`docker rm`不会删除共享的文件夹
然后参考这个https://stackoverflow.com/questions/46672001/is-it-safe-to-clean-docker-overlay2
使用`docker prune`等