### 开头出现交互式时区设置解决
Dockerfile 开头加上
```docker
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
```