前置
- [[generate-key-pair]]
- [[server-config]]
- 了解[[docker/image]], [[container]]
- [[sysvinit]]（docker中用的不是[[systemd]]，但两者很多东西共通）

# 方法一：对于已有的image
对于已有的image，希望得到基本相同，但允许使用`ssh`密钥登录的[[container]]
参考以下过程
注
- 这样的container一般就不要`rm`掉了，否则又要重新操作
- 如果`stop`了，重开时不一定还能连，除非你参考[[server-config]]开机启动
1. 静默创建公钥私钥对[[generate-key-pair]]
`ssh-keygen -t rsa -N '' -f <path>/id_rsa`
2. 运行时往容器传入环境变量
    - `docker run -it -e AUTHORIZED_KEYS="$(cat <path>/id_rsa.pub)" <其它选项> <镜像名> <命令>`
    - 举例：例如[[container]]中有一个最简单的交互式容器示例`docker run -it ubuntu bash`，那么我们就改成`docker run -it -e AUTHORIZED_KEYS="$(cat <path>/id_rsa.pub)" ubuntu bash`
      - 即此处没有`<其它选项>`
3. 现在进入容器了，`apt update; apt install -y openssh-server`
   1. 参考[[server-config]]
4. 在容器里面`echo $AUTHORIZED_KEYS`，重定向（参考[[11-basic-scripting-partA]]）到你想要的容器内部的文件
   1. 例如：`mkdir ~/.ssh`然后`echo $AUTHORIZED_KEYS > ~/.ssh/authorized_keys`
5. 修改容器内`/etc/ssh/sshd_config`，把`AuthorizedKeysFile`字段指定文件名
   1. 如果刚刚重定向到`~/.ssh/authorized_keys`，则此步可以省略，参考[[server-config]]. 因为这是默认！
6. `service ssh restart`
7. 容器外
`ssh -i <path>/id_rsa <其它内容>`
即可登录
   - `<其他内容>`指的是`ssh`连接中指定用户名、ip、端口等。反正正常的ssh怎么用公钥连你就怎么连