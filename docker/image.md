前置
- [[docker/installation]]

内容
- image相当于面向对象编程中的类，[[container]]相当于对象
- 标识符格式举例：`nvidia/cuda:10.0-cudnn7-devel`
  - `nvidia`提供，名字是`cuda`，版本是`10.0-cudnn7-devel`
  - 有些时候可以`:latest`表示最新
- 举例
  - [[docker/installation]]中的`sudo docker run hello-world`在你本地没有此image时会自动下载并实例化成container，再运行
  - `docker pull`可以下载image，且只要你不删除，一次下载以后都可以用
    - 例如`docker pull nvidia/cuda:10.0-cudnn7-devel`