常用命令
```sh
# 这样之后才能commit. 加了--global意思是全局，而不是针对一个项目
git config --global user.name <名字>
git config --global user.email <邮箱>

# 设置代理
git config --global http.proxy http://127.0.0.1:端口
git config --global https.proxy http://127.0.0.1:端口

git config --list # 查看列表, 可以用q退出
```