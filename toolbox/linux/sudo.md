- 没有`sudo`命令？常见于服务器。可以`apt install sudo`
- `sudo ll`不行？参见[[alias]]原理，即只替换第一个“单词”。可以`'sudo '`（引号作拼接）解决，参见[[11-basic-scripting-partA]]
- `sudo -u <用户名> <命令>`可以以指定用户跑。可以`sudo -u <别人> passwd`看效果。需要`alias`的话，同理刚刚的引号
- `su`和`sudo su`的区别：`su`是以root身份登录，然后在进行别的操作，需要root的密码
`sudo su`是用户以root身份运行`su`提权，只需要输入用户的密码

## todo
- 有[[anaconda]]时
```sh
sudo -u `whoami` `which python`
```
才行
原因todo
- `sudo -u <用户名> -i` todo!（子命名空间问题）