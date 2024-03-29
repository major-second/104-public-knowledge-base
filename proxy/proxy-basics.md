- 代理的用途
    - 对方能上某些网（比如外网，比如校园内网），你不行，你就让他帮你
    - 所以有时需要内翻外，有时需要外翻内，有时需要翻到学校公司网里……
    - 总之你有几套身份，当上不了一些网时就尝试换身份
    - 注：[[vpn]]原理和代理大不同，但结果往往是类似的，就是可以让别人帮你访问你访问不了的东西
- 需要的身份汇总

|网站|需要的身份|原因
|-|-|-
|YouTube, Google, [[download-resource]]中许多网站|翻墙（[[vpn]]或代理都行）|中国政府GFW（强力阻挡，肯定被阻挡）
|[[github]]|ios不用翻墙，其它平台不翻墙有[[dns]]污染不稳定|同上，但阻挡不那么强力
|学校内网，如学院的一些网页|校园网或学校[[vpn]]|组织安全政策
|公司内网，如公司服务器、远程桌面|公司网或公司[[vpn]]|组织安全政策
|一些出版商（下载论文）|校园网或学校[[vpn]]|版权/商业限制
|一些流媒体、视频音乐等网站[[spotify]]|特定国家地区，可能中国内地/美国/香港……|版权/商业限制
|公司相关，例如：`Windows开始菜单 - Access work or school` / Teams企业版|有些不能开代理|可能未对复杂情况处理
|连接公用（机场酒店等）wifi的登录|不能开代理|可能未对复杂情况处理
|[[wsa]]安装时|不能代理（否则可能操作复杂），但需要翻墙，一般用[[vpn]]|GFW+复杂情况
|支付宝[[alipay]]|中国内地|未知
|被特定算法或名单保护的网站。如被cloudflare保护等|换个身份说不定就行了（比如校园网ip显然在论文ddl前对overleaf流量特别大可能被ban）|
|一些每天限额下载，限额使用的网站|换个身份说不定就行了|
|[[spotify]]|每14天用指定国家ip登录，可用 cip.cc 查询地址等，参考[[configure-proxy]]
|[[chatgpt]]|不翻墙可上，但不变ip用不了，所以可能需要[[configure-proxy]]全局代理。可能不能使用公司内网，有法务问题。一些公交车[[node]]可能被[[chatgpt]] ban
- 如何使用
  - [[node]]，可以是免费羊毛（这种可能有公安请喝茶风险，是蜜罐），学长送的，学校给的，实验室给的，自己买的
  - 客户端，如[[windows-proxy-client]], [[linux-proxy-client]], [[v2raya]]等
    - 有些客户端如`geph`集成了[[node]]
  - [[configure-proxy]]使得使用上刚刚说的[[node]]和客户端
  - 傻瓜式全集成软件（往往收费/有政治目的）
    - `getflix`
    - `geph`
    - 翻回国
      - [穿梭](https://www.transocks.com/)
- 坏处
  - 开代理有时会造成安全风险，导致一些东西不给你用。比如公司账号无法登录等
  - 代理比直连有时候会慢，[[vpn]]由于照顾公司，那就更慢。所以：可以不用代理那就不用呗
    1. 有些时候改[[hosts]]即可，不一定非得正儿八经挂代理。其作用参见[[hosts]]
      - 原理是墙分为多种，有的是直接打死，有的只是[[dns]]污染
    2. 有些时候可以通过[[channel]]，[[pip]]设置，[[package-managers-source]]等，通过[[settings-and-configurations]]使用国内[[mirror]]镜像或源，而不用国外的源
  - 所以一定要熟练开关代理，设置是否全局，参考[[configure-proxy]]