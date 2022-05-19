https://www.cnblogs.com/zwcry/p/9602756.html
- `sudo systemctl stop ...`停止服务
    - 例如当[[v2raya]]服务正在运行时，`vim`修改`/etc/resolv.conf`可能总是提示`WARNING: The file has been changed since reading it!!! Do you really want to write to it (y/n)?`，也就是没法人工变[[dns]]
- `sudo systemctl start ...`开始服务
- `restart`重启，`enable`开机启动，`disable`开机不启动，参考[[v2raya]]
  - `man systemctl`中提到`enable`和`start`是正交（orthogonal）的