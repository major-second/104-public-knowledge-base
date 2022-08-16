- 前置[[settings-and-configurations]]
- `apt`是从软件源上下载软件的
  - `ubuntu`官方源，清华，阿里云等有一般、通用的软件
  - 而[[v2raya]]，[[ros/installation]]，[[docker/installation]]，[[vscode/command-line]]等可能不被这些官方收录
    - 所以需要自己添加
    - 再用`sudo apt update`更新
    - 之后即可以在新的源上获取软件
    - 这个添加的过程往往都在装软件的官方文档中写出
    - 添加之后，如果嫌之后每次`apt update`太慢，可以删掉不需要的
  - 除了添加`ubuntu`官方、软件开发者官方的源，还可能有一些个人维护的源，即“ppa”
- 默认源：安装ubuntu时选择where you are时选择中国，才能使用中国快的服务器
  - 这时别装外宾！否则慢的是你自己
  - 如果选错了，之后可以在ubuntu的设置中改
  - 当然，默认源也有可能不够好
    - 比如装[[ros/installation]]缺过包
    - 换阿里云搞定
- 更新软件源列表：`sudo apt update`
  - 这是安全的，和[[software-management/upgrade]]一定要区分开！`upgrade`千万谨慎执行！
- 换源可以命令行操作
  - 具体地：在文件`/etc/apt/sources.list`中。可参考[[settings-and-configurations]]
  - 也可以九个点 - Software & Updates换
## 举例
[参考](https://blog.csdn.net/sigmarising/article/details/84778296)
如阿里云（是`http`）
```text
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```
清华（是`https`，就可能出现证书问题）
```text
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```
## `ppa`
- 个人、非官方。对于不主流软件，不主流版本等可能需要添加`ppa`. 当然有安全风险
- 举例`apt install -y software-properties-common; add-apt-repository -y ppa:jonathonf/ffmpeg-4; apt update; apt install -y ffmpeg`
## troubleshooting
- 如果certificate（证书）出问题
  1. 重装`ca-certificates`试试
  - 如果可以正常重装，那就正常重装
  - 如果死锁了（重装`ca-certificates`本身需要证书
    - 则[参考这篇](https://blog.csdn.net/Chaowanq/article/details/121559709)
    - 这是用[[temp-solution]]思想（临时使用`http`而非`https`，装好了再换回`https`）
    - 当然如果适当舍弃安全，也可以一直用`http`而非`https`
  2. 如果重装`ca-certificates`无效，则可能是[[nat]]，[[proxy/usage]]等中间过程引起的问题，例如在docker容器中使用`apt`，或物理机通过[[nat]]服务，[[proxy/usage]]服务时，都会导致`Certificate verification failed: The certificate is NOT trusted.`
    - [参考](https://askubuntu.com/questions/1095266/apt-get-update-failed-because-certificate-verification-failed-because-handshake/1210812#1210812)
    - 此时，如果你信任你的源（例如在没有[[nat]]服务的机器上可以正常使用该源，说明其安全），就可以手动信任它
    - 即在`/etc/apt/apt.conf.d/99verify-peer.conf`（`.d`的含义参考[[settings-and-configurations]]）中增加一行`Acquire { https::Verify-Peer false }`
- `Conflicting values set for option Signed-By regarding source ...`问题参考[这个](https://askubuntu.com/questions/1329308/sudo-apt-get-returns-conflicting-values-set-for-option-signed-by-regarding-s)，只需要把出问题的`gpg`和`list`都删掉就可以了
  - 这是[[refresh]]的一个例子
  - 删除`某某.d/.list`文件的操作参考[[settings-and-configurations]]中涉及`.d`的部分进行理解
- `is configured multiple times in /etc/apt/sources.list:16 and /etc/apt/sources.list:20`
  - 字面意思
  - 无伤大雅，你重复写了两遍某一行就会这样
  - 反正只是个警告，看着不爽删掉就行
## 包管理器源
- `pip`，`conda`和`apt`类似，也是包管理器，当然也有源
- 设置方法参考[[condarc]]和[[pip]]