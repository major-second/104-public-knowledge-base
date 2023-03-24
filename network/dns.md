https://blog.csdn.net/Asukaaaa/article/details/83341075
# dns污染
- 排查网络故障时，如果域名不通，ip通，就要检查dns！
  - 例如中国防火墙墙[[github]]就是这样（2023.3），被“污染”
  - 能翻墙的[[proxy-basics]]和不被污染的dns往往是单向推出关系，即你可以翻墙，那么自然就会使用正常的dns服务器
    - 除非你在用公司内网，[[vpn]]等等，会劫持
- 表现
  - 比如`git` [[push-pull]]时
    ```text
    kex_exchange_identification: Connection closed by remote host
    Connection closed by 20.248.137.48 port 22
    ```
    - 这个ip不对
    - 参考[[hosts]]
    - [参考这里查正确ip](https://ipaddress.com/website/github.com)
  - 比如`ipinfo.io`直接跳转“国家反诈中心”（2023/3出现）
# dns解析
- [参考](https://zhuanlan.zhihu.com/p/39406412)
  - 一般来说直接改`114.114.114.114`就挺好
  - 但是有时有风险（比如反向代理[[proxy-basics]]了），不放心的话可以直接改hosts
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
  - 当然也可以手动改hosts
- ios
  - 可能只有wifi状态才能改dns