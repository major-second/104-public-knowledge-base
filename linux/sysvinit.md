参考[[systemd]]
sysvinit和systemd是并列关系，[参考](https://www.cnblogs.com/a5idc/p/13752839.html)
docker中常用sysvinit命令，因为没有`systemd`，典型报错`System has not been booted with systemd as init system (PID 1). Can't operate.`
如`service ssh start`，`service ssh restart`等，参考[[docker/ssh]]