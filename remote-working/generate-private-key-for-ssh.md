`ssh-keygen -t rsa`生成用户的`id_rsa`和`id_rsa.pub`

注意要在`/home/user/.ssh` 下 `cp id_rsa.pub authorized_keys`，不然在私钥登录时会提示`Permission denied (Publickey)`
