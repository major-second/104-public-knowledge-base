- `~`与备份文件
  - [参考](https://www.cnblogs.com/Cccarl/p/6627421.html)
  - 查看
    - 参考[[find-grep]]
    - `ls -lR | grep '.*~'`
    - `find . | grep '.*~'`
  - 删除（务必小心）
    - `find . | grep '.*~' | xargs rm`