参考[github issue](https://github.com/microsoft/debugpy/issues/102)，如果不调低防护级别，可能无法使用attach功能
```sh
sudo sed -i 's/kernel.yama.ptrace_scope = 1/kernel.yama.ptrace_scope = 0/g' /etc/sysctl.d/10-ptrace.conf; \
sudo sysctl -p /etc/sysctl.d/10-ptrace.conf
```
（即：先编辑再更新）