- 前置
  - [[settings-and-configurations]]
  - 首先打开代理客户端，比如[[linux-proxy-client]]，[[windows-proxy-client]]
[toc]
# 一般原则
- 打开代理之后还需要配置才能让应用实际走代理，而不是走直连
  - [[settings-json]]，[[tools/zoom]]等等都有提到
  - 相比之下[[vpn]]就是傻瓜式，hhh（不过往往也有坏处，如不灵活，常常“全局”）
- 有一些[[settings-and-configurations]]一般原则适用。比如“优先级”等
  - 例如浏览器可以使用系统设定代理也可以自己设定ip和端口号，覆盖系统的
# 设置方法
## 系统设定
- 比如
  - ubuntu的九宫格-齿轮（Settings）
    - 注意这个和终端代理[[6-env]]不同。浏览器看的一般是这个而不是终端
  - Win10
    - 开始菜单搜索proxy
    - 或者会[[powershell]]可以
      - `Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name "ProxyEnable" -Value 1`
      - `Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name "ProxyServer" -Value "192.168.1.1:9912"`
      - 虽然这个在[[refresh]]之前可能直接用powershell没法直接验证，但是你可以`curl -Proxy <ProxyServer> <URL>`变相验证
      - 也可以`Start-Process powershell.exe -NoNewWindow -Wait -ArgumentList <路径>`这样新起一个进程验证！这是[[refresh]]思想
        - 参考[[run-ps1]]
- 有些翻墙客户端如`geph`能自动帮你设置这个地方的代理
  - 但这时就不灵活，没法自己灵活切换用“哪边的”代理等
## 环境变量相关
### linux环境变量，终端走代理
[[6-env]]
在`~/.bashrc`（当然如果用[[zsh]]就是`~/.zshrc`）中加上
```sh
export https_proxy="localhost:<端口号>"
export http_proxy="localhost:<端口号>"
```
然后重启终端或`source ~/.bashrc`一下，就好了
（也就是[[6-env]]中说的的添加环境变量）
- 注：环境变量和ubuntu系统设定是两回事
- 注：临时要关就`unset http_proxy https_proxy`
- 拓展：可以在[[shrc]]写一些简单脚本，处理不同情况
  - [[wsl]]得到`$host_ip`的核心代码：`host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")`
  - 需要了解[[13-loop]], [[12-condition]], [[curl-wget]]等等
  - 举例片段
```sh
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
for port in 9910 9911
do
 export ALL_PROXY="http://$host_ip:$port"
 echo trying $ALL_PROXY
 if curl -fsSL --max-time 2 https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore
 then
  echo "\n$ALL_PROXY is on"
  break
 fi
done
```
- 一些特殊情况
  - [[pip]]走代理
    - `pip`自动读取环境变量中的代理设置
    - 但要求`~/.bashrc`里的`$http_proxy`等等变量以`http://`开头，而不是上节那样直接`127.0.0.1`开头
    - 上节那样会报错，且在报错信息中可以看到应该怎么改
  - [[curl-wget]]提到`curl`可以使用`ALL_PROXY`，但`wget`只能用`http_proxy`和`https_proxy`（还区分大小写）
### win环境变量
参考[[windows/env-var]]，[[powershell-var]]
典型：`$env:http_proxy="http://127.0.0.1:<端口号>"`
有些软件比如[[robocorp]]会用到
## 其它
### 虚拟机和子系统
- 很多时候找主机ip，使用主机ip的相应露出端口即可
  - 例如[[wsl]]，要点`host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")`（bash）
  - 例如[[wsa]]，前提[[wsl]]
    - 要点`$WinNetIP=$(Get-NetIPAddress -InterfaceAlias 'vEthernet (WSL)' -AddressFamily IPV4)`（powershell）
    - [[aida64]]的network部分也能看到
- 反过来主机用[[wsl]]的[[v2raya]]：linux中`ifconfig`看到ip
  - 别忘了linux中改Inbound（[[v2raya]]：开启端口分享）
  - 别忘了这下绕过的ip除了`localhost`，还有相应的这个内网ip
### 其它读取自己独立设置的软件
- 有些软件读取自己设置而非系统设置。参考[[cmake]]，[[ros/installation]]，[[git-config]]
  - 有时嫌改这种设置太麻烦，可以改[[hosts]]或[[dns]]作[[temp-solution]]
- 有些软件默认读系统设置或环境变量，但自己也可以独立设置，例如[[curl-wget]]中`curl -x`
  - 参考[[settings-and-configurations]]
# 验证配置成功
- linux终端
  - `curl cip.cc`看结果
  - `curl ipinfo.io`看结果
  - `curl https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore`看结果（参考[[zsh]]）
- 浏览器浏览
  - `cip.cc`看结果
  - `ipinfo.io`看结果
  - `www.google.com`看能不能上
  - `cip.cc`好处是中文且墙内较快
  - `cip.cc`有时由于未知原因用不了，就试试`ipinfo.io`呗
- powershell
  - 比如`curl ipinfo.io | select content | select-string country`，比linux麻烦些，参考[[powershell/string]]
- 注：`cip.cc`, `ipinfo.io`结果不同：可能是自动分支了墙内墙外，非全局，参见下文
# 举例
- [[push-pull]], [[tools/zoom]]等中都出现了一些东西成功配置了代理，另一些没有配置，结果导致一些途径成功另一些失败
- [[wsa]]不用代理则不需要[[wsl]]，但用的话就可能需要，比较麻烦
# troubleshooting
## 是否使用全局模式
代理客户端中往往有是否global（全局）的设置
- global优点
  - 所有网站流量都走境外，避免一些规则不匹配导致上不了
  - 有些网站墙内能上但是墙内ip无法提供服务，例如2022.12的币安，OpenAI，这就必须要全局模式
- global缺点
  - 有些网站必须墙内身份才能上，参考[[proxy-basics]]
  - 有些网站墙内比墙外稳定/速度快
  - 浪费代理流量
## Inbound设置
- 监听：`127.0.0.1`只有自己，`0.0.0.0`也可以给别人用（包括虚拟机等）
- 不同客户端设置方法不同
  - clash有General - Allow LAN一键开关比较方便
- 在[[wsl]]中用代理就需要
## 格式、解析等
- 参考[[settings-and-configurations]]
  - 比如`apt`和`pip`不能正确解析`127.0.0.1:端口号`，但`curl`可以。`apt`需要写`http://127.0.0.1:端口号`
  - 有些要写`http://`，有些不用，以及端口号怎么写……