https://blog.csdn.net/Asukaaaa/article/details/83341075
总结：
- 排查网络故障时，如果域名不通，ip通，就要检查dns！
- linux
  - `/etc/nsswitch.conf`定顺序
  - `/etc/resolv.conf`表示一般去哪里解析（比如`114.114.114.114`）
  - `/etc/hosts`手动解析
    - 如`bilibili.com`解析成`127.0.0.1`防止摸鱼
    - 比如[[hosts]]作翻墙的[[temp-solution]]
- windows
  - ![](network-config-0.png)
  - Network & Internet settings - Change adapter* - 单击图标 - 上方出现菜单栏选Change settings* - 选择条目IPv4 - Properties
  - ![](network-config-1.png)
- ios
  - 可能只有wifi状态才能改dns