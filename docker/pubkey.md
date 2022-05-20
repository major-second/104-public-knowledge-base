前置
- [[generate-key-pair]]
- [[ssh-server-config]]

docker的密钥登录参考（模仿以下命令）
1. 静默创建公钥[[generate-key-pair]]
`ssh-keygen -t rsa -N '' -f <path>/id_rsa`
2. 运行时往容器传入环境变量
<code>docker run -it -e AUTHORIZED_KEYS="$(cat <path>/id_rsa.pub)" <其它选项> <镜像名></code>
3. 在容器里面`echo $AUTHORIZED_KEYS`，重定向[[11-basic-scripting-partA]]到你想要的容器内部的文件
4. 修改`/etc/ssh/sshd_config`，把`AuthorizedKeysFile`字段指定文件名
5. 容器外
`ssh -i <path>/id_rsa <其它内容>`
登录