https://blog.csdn.net/Asukaaaa/article/details/83341075
总结：
- 排查网络故障时，如果域名不通，ip通，就要检查dns！
- `/etc/nsswitch.conf`定顺序
- `/etc/resolv.conf`表示一般去哪里解析（比如`114.114.114.114`）
- `/etc/hosts`手动解析（例如把`bilibili.com`解析成`127.0.0.1`防止摸鱼）
  - 比如[[hosts]]作翻墙的[[temp-solution]]