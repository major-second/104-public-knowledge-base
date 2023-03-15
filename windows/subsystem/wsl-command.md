[toc]
# 基础
## 概述
- 前置
  - [[powershell/basics]]
  - [[escape]]
  - [[wsl]]
  - [[shell-type]]
    - 也就是如果需要[[shrc]]，可能需要用`bash -ic`替代下文`bash -c`
- windows的[[powershell/basics]]中，`wsl`命令（不是linux系统中的命令）
  - 可用于[[silent]]操作[[wsl]]，特别是[[silent]]地[[refresh]]重启WSL，非常方便
## 基础举例
- 例：直接`wsl`
    - 这可以和[[windows-link]]结合，从而在桌面一个快捷键直接进入linux终端
    - 参考本文件夹`wsl.ps1`
- 例：`wsl -e echo 1`
  - 注意`wsl -e 'echo 1'`不行（可能被当成整体了）
  - `wsl -e bash -c 'echo 1'`可以
- 例：`wsl --set-default Ubuntu-20.04; wsl --list; wsl -e uname -a`
- 例：需要通配符[[glob]]时
  - `wsl -e bash -c "dos2unix ~/*.sh"`
  - 不能直接`wsl -e dos2unix ~/*.sh`
  - 因为`bash`支持[[glob]]，`wsl`默认不支持[[glob]]，除非设置一下（略）
# 进阶
## 多行
```powershell
wsl -e bash -c '
for (( i = 0; i < 5; i++))
do
 expr $i \* 5
done
'
```
## [[escape]]转义
- `wsl -e bash -c 'echo -e [boot]\\nsystemd=true | sudo tee /etc/wsl.conf'`
  - 直接一键[[wsl-systemd]]
  - 当然也可以进行其它[[silent]]操作
- `wsl -e bash -c 'echo -e \\033[35m $(uname -a) \\033[0m'`
  - [[echo]]彩色的
- 以上两个例子都是[[escape]]2次
- 这和powershell特性无关，只和[[echo]]特性有关
## [[powershell/basics]]和shell两种[[escape]]转义混合
- 基本[[powershell/basics]]例子：<code>wsl -e bash -c "a=1; echo &#96;$a"</code>
- 两种转义`\`, <code>&#96;</code> 混合例子
  - <code>wsl -e bash -c "ifconfig | grep 'inet\s' | grep -v '127.0' | awk '{print &#96;$2}'"</code>
  - 极度实用！在windows访问linux端口就需要！例如[[v2raya]]
## 使用文件
- 使用文件，减少[[escape]]
- 比如windows中`cd`到本文件夹，然后
- `wsl -e bash "$(wsl -e pwd)/wsl-command.sh"`
- 输出非常好，是
```text
echo 172.某某...
172.某某...
I can use `, ' and " here
```
- 确实，在[[awk-cut]]时单引号`'{print $2}'`方便，在[[11-basic-scripting-partA]]重定向时需要用[[6-env]]则双引号方便，想要[[aggregation]]时，你就不能疯狂[[escape]]. 这时还是文件香！