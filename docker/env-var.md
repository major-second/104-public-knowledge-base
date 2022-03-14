- build时用`ARG`标记build期变量，命令行`docker build`时可传入
- `ENV`则是build时和run时都可用
- `docker run -e`是这次run能用

- 关于`ssh`清除变量解决方法：[[ssh-env-var]]