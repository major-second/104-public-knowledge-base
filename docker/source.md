- 前置
  - [[software-management/source]]
  - [[settings-and-configurations]]
- 我们可以修改`docker`中`/etc/apt/sources.list`这种设置文件改变其使用的软件源
  - 例如在[[docker-file]]中写`COPY host_files/sources.list /etc/apt/`复制宿主机的设置文件
- 外部能用的软件源，容器内部未必能用
  - 例如涉及代理的一个tricky问题
    - 现象导致`Hash Sum mismatch`错误
    - [解决方法](https://github.com/jenkinsci/docker/issues/543)
    - 参考[[settings-and-configurations]]中的`.d`
  - `https`也可能导致问题`Certificate verification failed: The certificate is NOT trusted.`
    - 参考[[software-management/source]]解决
    - 即临时使用`http`源安装`apt install ca-certificates`