前置
- `sudo apt install openssh-server`（否则没法用`ssh`登录）
  - 建议`systemctl enable sshd`（开机启动）

- 在`/etc/ssh/sshd_config`（区别于[[client-config]]）
- 注意其中说了带注释的是默认值
- 常见非平凡设置项：
  - `Port`改成你想要的端口
  - 如果想密码登录`root`（这当然不安全）
    - 首先用一个**有权限的账户**，`sudo passwd root`给`root`**设置初始密码**
      - 参考[[7-permissions]]
    - 改成`PermitRootLogin yes`
    - `systemctl restart sshd`重启服务
    - 之后即可ssh到root
  - 密钥登录：一般只需维持默认设置
    - 但是可能要变`AuthorizedKeysFile`字段
    - 之后根据此字段，把[[generate-key-pair]]中生成的`*.pub`（公钥）拷贝成为**指定路径，指定文件名**的文件
      - 默认文件名`authorized_keys`
    - 为了安全可以`PasswordAuthentication no`