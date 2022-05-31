常用命令
```sh
git config --global user.name <名字>
git config --global user.email <邮箱>
# 这样之后才能commit. 加了--global意思是全局，而不是针对一个项目

git config --global http.proxy 127.0.0.1:端口
git config --global https.proxy 127.0.0.1:端口
# 设置代理

git config --list # 查看列表, 可以用q退出
```
注：如果`git`命令行不能`push pull`（或不稳定），但浏览器可以，可能是CLI没设置代理但浏览器自动走了浏览器代理
参考[[zoom]]，也有类似问题