- 生成密钥对：
`ssh-keygen -t rsa`生成`id_rsa`和`id_rsa.pub`
- 静默[[silent]]生成：
`ssh-keygen -t rsa -N '' -f <path>/id_rsa`
- 公钥放到指定位置：接下来为了在`<username>`账户使用私钥`id_rsa`登录，需要把`id_rsa.pub`复制到`/home/<username>/.ssh`下作为`authorized_keys`文件，不然在私钥登录时会提示`Permission denied (Publickey)`.
  - 多个用户可以共用一个公钥。
- 私钥的使用：把私钥拷到需要的设备上，然后例如使用[[client-config]]或者`-i`参数等等都能使用。注意权限问题：[[private-key-permissions]]