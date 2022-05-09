对于超过100M的大文件
- 报错the remote end hung up unexpectedly
- 或者this exceeds GitHub's file size limit of 100.00 MB，然后`remote rejected`

尝试删除大文件后push，仍然报错
原因：`git push`不止push当前版本，而是把所有[[commit]]但未被push的版本一并push上去！[[hidden-file]]和[[push]]都有提到
- [解决方案](http://t.zoukankan.com/rixiang-p-12048849.html)
    - 看本地历史[[commit]]（比如用[[git-history]]）
    - [[reset]]取消大文件版本及之后的版本记录
      - 推荐用soft reset，保持目前的working copy
    - 删除大文件
    - 再正常stage，commit，push等