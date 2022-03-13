`df`看到`overlay`太多东西占满了！怎么办
首先注意`docker rm`不会删除共享的文件夹
然后参考这个https://stackoverflow.com/questions/46672001/is-it-safe-to-clean-docker-overlay2
使用`docker prune`等

数据文件夹如果默认放到`/var`，那么会很容易满，参考[[dual-boot-partition]]
我们可以通过https://www.programminghunter.com/article/6570595622/
的方法修改