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
  - `docker rmi`删除image
    - 后面参数可以是
      - hash码的一部分或全部
      - “类标识符”如`hello-world:latest`
    - 前提：没有利用该image的[[container]]存在
    - 所以可能需要先`docker stop`和`docker rm`一下