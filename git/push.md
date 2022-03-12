## 不要reset已经push的
[不要为了看起来舒服就reset再push. 看起来一堆commit并不占多少空间](https://segmentfault.com/q/1010000003089251)
## tags
`git push --tags`可以让远程能看到tags
## 取消保存用户名密码
我们的项目需要在github上备份一份，于是仿照教程
https://www.cnblogs.com/shenggang/p/12133049.html
建立自己的私有库，直到push一步遇到问题：remote: repository not found，但明明GitHub上有这个repo！

检查后发现是credential helper的问题, git自动记住了以前输过的用户名密码，但是以前的用户名密码不是我这个仓库的用户名密码！
使用git config --global --unset credential.helper取消保存即可
## 去除大文件
又报错the remote end hung up unexpectedly网络不稳定，重试后发现是有超过100MB的大文件，上传报错。

尝试删除大文件后push，仍然报错，即使大文件被删除仍然被push上去了。
搜索后发现git push不止push当前版本，而是把所有未被push的版本一并push上去！
解决方案： http://t.zoukankan.com/rixiang-p-12048849.html
使用git cherry查看push上去过的历史版本(如果没有记录，则用git log看本地历史版本)，
git reset取消该大文件版本及之后的版本记录, 再git add .接着push即可
