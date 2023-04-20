`~/.ssh`是常见的存放和ssh有关文件的地方
- 比如
  - [[server-config]]中可以看到`authorized_keys`就在这
  - 自己生成的`id_rsa`私钥，`id_rsa.pub`公钥，[[https-ssh]]用的`id_ed25519`等都常常放这
    - [[private-key-permissions]]
  - [[known-hosts]]
- 该文件夹的权限必须合适（比如设成`777`就会导致无法连接。此时可以删除重新创建）