对于超过100M的大文件
- 报错the remote end hung up unexpectedly
- 或者this exceeds GitHub's file size limit of 100.00 MB，然后`remote rejected`

尝试删除大文件后push，仍然报错
原因：`git push`不止push当前版本，而是把所有[[commit]]但未被push的版本一并push上去！
解决方案： http://t.zoukankan.com/rixiang-p-12048849.html
使用git cherry查看push上去过的历史版本(如果没有记录，则用git log看本地历史版本)
[[reset]]取消该大文件版本及之后的版本记录（推荐用soft reset，保持目前的working copy）, 再`git add .`接着push即可